#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import platform
import socket
import sys

from datetime import datetime, timedelta
from datetime import timezone as tz

import psutil

from backend.utils.timezone import timezone


class ServerInfo:
    @staticmethod
    def format_bytes(size: int | float) -> str:
        """
        格式化字节大小

        :param size: 字节大小
        :return:
        """
        factor = 1024
        for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
            if abs(size) < factor:
                return f'{size:.2f} {unit}B'
            size /= factor
        return f'{size:.2f} YB'

    @staticmethod
    def fmt_seconds(seconds: int) -> str:
        """
        格式化秒数为可读的时间字符串

        :param seconds: 秒数
        :return:
        """
        days, rem = divmod(int(seconds), 86400)
        hours, rem = divmod(rem, 3600)
        minutes, seconds = divmod(rem, 60)

        parts = []
        if days:
            parts.append(f'{days} 天')
        if hours:
            parts.append(f'{hours} 小时')
        if minutes:
            parts.append(f'{minutes} 分钟')
        if seconds:
            parts.append(f'{seconds} 秒')

        return ' '.join(parts) if parts else '0 秒'

    @staticmethod
    def fmt_timedelta(td: timedelta) -> str:
        """
        格式化时间差

        :param td: 时间差对象
        :return:
        """
        total_seconds = round(td.total_seconds())
        return ServerInfo.fmt_seconds(total_seconds)

    @staticmethod
    def get_cpu_info() -> dict[str, float | int]:
        """获取 CPU 信息"""
        cpu_info = {'usage': round(psutil.cpu_percent(percpu=False), 2)}  # %

        try:
            # CPU 频率信息，最大、最小和当前频率
            cpu_freq = psutil.cpu_freq()
            cpu_info.update({
                'max_freq': round(cpu_freq.max, 2),  # MHz
                'min_freq': round(cpu_freq.min, 2),  # MHz
                'current_freq': round(cpu_freq.current, 2),  # MHz
            })
        except Exception:
            cpu_info.update({'max_freq': 0, 'min_freq': 0, 'current_freq': 0})

        # CPU 逻辑核心数，物理核心数
        cpu_info.update({
            'logical_num': psutil.cpu_count(logical=True),
            'physical_num': psutil.cpu_count(logical=False),
        })
        return cpu_info

    @staticmethod
    def get_mem_info() -> dict[str, float]:
        """获取内存信息"""
        mem = psutil.virtual_memory()
        return {
            'total': round(mem.total / 1024 / 1024 / 1024, 2),  # GB
            'used': round(mem.used / 1024 / 1024 / 1024, 2),  # GB
            'free': round(mem.available / 1024 / 1024 / 1024, 2),  # GB
            'usage': round(mem.percent, 2),  # %
        }

    @staticmethod
    def get_sys_info() -> dict[str, str]:
        """获取服务器信息"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sk:
                sk.connect(('8.8.8.8', 80))
                ip = sk.getsockname()[0]
        except socket.gaierror:
            ip = '127.0.0.1'

        return {
            'name': socket.gethostname(),
            'ip': ip,
            'os': platform.system(),
            'arch': platform.machine(),
        }

    @staticmethod
    def get_disk_info() -> list[dict[str, str]]:
        """获取磁盘信息"""
        disk_info = []
        for disk in psutil.disk_partitions():
            usage = psutil.disk_usage(disk.mountpoint)
            disk_info.append({
                'dir': disk.mountpoint,
                'type': disk.fstype,
                'device': disk.device,
                'total': ServerInfo.format_bytes(usage.total),
                'free': ServerInfo.format_bytes(usage.free),
                'used': ServerInfo.format_bytes(usage.used),
                'usage': f'{round(usage.percent, 2)} %',
            })
        return disk_info

    @staticmethod
    def get_service_info() -> dict[str, str | datetime]:
        """获取服务信息"""
        process = psutil.Process(os.getpid())
        mem_info = process.memory_info()
        start_time = timezone.f_datetime(datetime.utcfromtimestamp(process.create_time()).replace(tzinfo=tz.utc))

        return {
            'name': 'Python3',
            'version': platform.python_version(),
            'home': sys.executable,
            'cpu_usage': f'{round(process.cpu_percent(interval=1), 2)} %',
            'mem_vms': ServerInfo.format_bytes(mem_info.vms),  # 虚拟内存, 即当前进程申请的虚拟内存
            'mem_rss': ServerInfo.format_bytes(mem_info.rss),  # 常驻内存, 即当前进程实际使用的物理内存
            'mem_free': ServerInfo.format_bytes(mem_info.vms - mem_info.rss),  # 空闲内存
            'startup': start_time,
            'elapsed': ServerInfo.fmt_timedelta(timezone.now() - start_time),
        }


server_info: ServerInfo = ServerInfo()
