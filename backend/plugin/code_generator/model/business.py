#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.common.model import Base, id_key

if TYPE_CHECKING:
    from backend.plugin.code_generator.model import GenColumn


class GenBusiness(Base):
    """代码生成业务表"""

    __tablename__ = 'gen_business'

    id: Mapped[id_key] = mapped_column(init=False)
    app_name: Mapped[str] = mapped_column(String(50), comment='应用名称（英文）')
    table_name: Mapped[str] = mapped_column(String(255), unique=True, comment='表名称（英文）')
    doc_comment: Mapped[str] = mapped_column(String(255), comment='文档注释（用于函数/参数文档）')
    table_comment: Mapped[str | None] = mapped_column(String(255), default=None, comment='表描述')
    # relate_model_fk: Mapped[int | None] = mapped_column(default=None, comment='关联表外键')
    class_name: Mapped[str | None] = mapped_column(String(50), default=None, comment='基础类名（默认为英文表名称）')
    schema_name: Mapped[str | None] = mapped_column(String(50), default=None, comment='Schema 名称 (默认为英文表名称)')
    filename: Mapped[str | None] = mapped_column(String(50), default=None, comment='基础文件名（默认为英文表名称）')
    default_datetime_column: Mapped[bool] = mapped_column(default=True, comment='是否存在默认时间列')
    api_version: Mapped[str] = mapped_column(String(20), default='v1', comment='代码生成 api 版本，默认为 v1')
    gen_path: Mapped[str | None] = mapped_column(String(255), default=None, comment='代码生成路径（默认为 app 根路径）')
    remark: Mapped[str | None] = mapped_column(
        LONGTEXT().with_variant(TEXT, 'postgresql'), default=None, comment='备注'
    )
    # 代码生成业务模型一对多
    gen_column: Mapped[list['GenColumn']] = relationship(init=False, back_populates='gen_business')
