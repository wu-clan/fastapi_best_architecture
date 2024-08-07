#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum
from enum import IntEnum as SourceIntEnum
from typing import Type


class _EnumBase:
    @classmethod
    def get_member_keys(cls: Type[Enum]) -> list[str]:
        return [name for name in cls.__members__.keys()]

    @classmethod
    def get_member_values(cls: Type[Enum]) -> list:
        return [item.value for item in cls.__members__.values()]


class IntEnum(_EnumBase, SourceIntEnum):
    """整型枚举"""

    pass


class StrEnum(_EnumBase, str, Enum):
    """字符串枚举"""

    pass


class MenuType(IntEnum):
    """菜单类型"""

    directory = 0
    menu = 1
    button = 2


class RoleDataScopeType(IntEnum):
    """数据范围"""

    all = 1
    custom = 2


class MethodType(StrEnum):
    """请求方法"""

    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATCH = 'PATCH'
    OPTIONS = 'OPTIONS'


class LoginLogStatusType(IntEnum):
    """登陆日志状态"""

    fail = 0
    success = 1


class BuildTreeType(StrEnum):
    """构建树形结构类型"""

    traversal = 'traversal'
    recursive = 'recursive'


class OperaLogCipherType(IntEnum):
    """操作日志加密类型"""

    aes = 0
    md5 = 1
    itsdangerous = 2
    plan = 3


class StatusType(IntEnum):
    """状态类型"""

    disable = 0
    enable = 1


class UserSocialType(StrEnum):
    """用户社交类型"""

    github = 'GitHub'
    linuxdo = 'LinuxDo'


class GenModelColumnType(StrEnum):
    """代码生成模型列类型"""

    BIGINT = 'BIGINT'
    BINARY = 'BINARY'
    BIT = 'BIT'
    BLOB = 'BLOB'
    BOOL = 'BOOL'
    BOOLEAN = 'BOOLEAN'
    CHAR = 'CHAR'
    DATE = 'DATE'
    DATETIME = 'DATETIME'
    DECIMAL = 'DECIMAL'
    DOUBLE = 'DOUBLE'
    DOUBLE_PRECISION = 'DOUBLE PRECISION'
    ENUM = 'ENUM'
    FLOAT = 'FLOAT'
    GEOMETRY = 'GEOMETRY'
    GEOMETRYCOLLECTION = 'GEOMETRYCOLLECTION'
    INT = 'INT'
    INTEGER = 'INTEGER'
    JSON = 'JSON'
    LINESTRING = 'LINESTRING'
    LONGBLOB = 'LONGBLOB'
    LONGTEXT = 'LONGTEXT'
    MEDIUMBLOB = 'MEDIUMBLOB'
    MEDIUMINT = 'MEDIUMINT'
    MEDIUMTEXT = 'MEDIUMTEXT'
    MULTILINESTRING = 'MULTILINESTRING'
    MULTIPOINT = 'MULTIPOINT'
    MULTIPOLYGON = 'MULTIPOLYGON'
    NUMERIC = 'NUMERIC'
    POINT = 'POINT'
    POLYGON = 'POLYGON'
    REAL = 'REAL'
    SERIAL = 'SERIAL'
    SET = 'SET'
    SMALLINT = 'SMALLINT'
    TEXT = 'TEXT'
    TIME = 'TIME'
    TIMESTAMP = 'TIMESTAMP'
    TINYBLOB = 'TINYBLOB'
    TINYINT = 'TINYINT'
    TINYTEXT = 'TINYTEXT'
    VARBINARY = 'VARBINARY'
    VARCHAR = 'VARCHAR'
    YEAR = 'YEAR'
