#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-04-25 18:00:50
@LastEditors: yanyongyu
@LastEditTime: 2020-05-06 13:20:23
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

import databases
import sqlalchemy

from .config import DATABASE_URL

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

User = sqlalchemy.Table(
    "users", metadata,
    sqlalchemy.Column("id",
                      sqlalchemy.Integer,
                      primary_key=True,
                      autoincrement=True),
    sqlalchemy.Column("username",
                      sqlalchemy.String(20),
                      nullable=False,
                      unique=True),
    sqlalchemy.Column("password", sqlalchemy.String(255), nullable=False),
    sqlalchemy.Column("register_time",
                      sqlalchemy.DateTime,
                      server_default=sqlalchemy.text("CURRENT_TIMESTAMP")),
    sqlalchemy.Column("current",
                      sqlalchemy.Integer,
                      server_default="0",
                      index=True),
    sqlalchemy.Column("current_date", sqlalchemy.DateTime, index=True),
    sqlalchemy.Column("puzzle_1", sqlalchemy.DateTime),
    sqlalchemy.Column("puzzle_2", sqlalchemy.DateTime),
    sqlalchemy.Column("puzzle_3", sqlalchemy.DateTime),
    sqlalchemy.Column("puzzle_4", sqlalchemy.DateTime),
    sqlalchemy.Column("puzzle_5", sqlalchemy.DateTime),
    sqlalchemy.Column("puzzle_6", sqlalchemy.DateTime),
    sqlalchemy.Column("puzzle_7", sqlalchemy.DateTime),
    sqlalchemy.Column("puzzle_8", sqlalchemy.DateTime),
    sqlalchemy.Column("puzzle_9", sqlalchemy.DateTime),
    sqlalchemy.Column("puzzle_10", sqlalchemy.DateTime),
    sqlalchemy.Column("puzzle_11", sqlalchemy.DateTime))
