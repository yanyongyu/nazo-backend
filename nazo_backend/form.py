#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-04-25 16:28:53
@LastEditors: yanyongyu
@LastEditTime: 2020-05-06 13:20:42
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field


class TokenForm(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str


class UserForm(BaseModel):
    id: int
    username: str
    password: str
    register_time: datetime
    current: int = 0
    current_date: Optional[datetime] = None
    puzzle_1: Optional[datetime] = None
    puzzle_2: Optional[datetime] = None
    puzzle_3: Optional[datetime] = None
    puzzle_4: Optional[datetime] = None
    puzzle_5: Optional[datetime] = None
    puzzle_6: Optional[datetime] = None
    puzzle_7: Optional[datetime] = None
    puzzle_8: Optional[datetime] = None
    puzzle_9: Optional[datetime] = None
    puzzle_10: Optional[datetime] = None
    puzzle_11: Optional[datetime] = None


class UserOutForm(BaseModel):
    username: str
    register_time: datetime
    current: int = 0
    puzzle_1: Optional[datetime] = None
    puzzle_2: Optional[datetime] = None
    puzzle_3: Optional[datetime] = None
    puzzle_4: Optional[datetime] = None
    puzzle_5: Optional[datetime] = None
    puzzle_6: Optional[datetime] = None
    puzzle_7: Optional[datetime] = None
    puzzle_8: Optional[datetime] = None
    puzzle_9: Optional[datetime] = None
    puzzle_10: Optional[datetime] = None
    puzzle_11: Optional[datetime] = None


class RankSimpleForm(BaseModel):
    first: str = "虚位以待..."
    second: str = "虚位以待..."
    third: str = "虚位以待..."


class StatusForm(BaseModel):
    user: UserOutForm
    rank: RankSimpleForm


class RankForm(BaseModel):
    rank: List[UserOutForm] = []


class PuzzleInForm(BaseModel):
    answer: str = Field(min_length=1, max_length=50)


class PuzzleOutForm(BaseModel):
    passed: bool
