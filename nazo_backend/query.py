#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-04-28 14:38:30
@LastEditors: yanyongyu
@LastEditTime: 2020-05-06 11:40:56
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

from datetime import datetime

from .model import database, User
from .form import RankSimpleForm, RankForm, UserForm


def _tuple2user(user: tuple) -> UserForm:
    return UserForm(**dict(zip(UserForm.__fields__.keys(), user)))


async def get_simple_rank() -> RankSimpleForm:
    query = User.select().where(User.c.current > 0).order_by(
        User.c.current, User.c.current_date).limit(3)
    rank = await database.fetch_all(query)
    return RankSimpleForm(**dict(
        zip(RankSimpleForm.__fields__.keys(), map(lambda x: x[1], rank))))


async def get_rank(limit: int = 10) -> RankForm:
    query = User.select().where(User.c.current > 0).order_by(
        User.c.current.desc(), User.c.current_date).limit(limit)
    rank = await database.fetch_all(query)
    return RankForm(rank=list(map(_tuple2user, rank)))


async def pass_puzzle(puzzle_id: int, user: UserForm) -> bool:
    # check level
    if puzzle_id > user.current + 1 or user.dict()[f"puzzle_{puzzle_id}"]:
        return False
    # commit pass
    query = User.update().where(User.c.id == user.id).values(
        **{
            "current": user.current + 1,
            "current_date": datetime.now(),
            f"puzzle_{puzzle_id}": datetime.now()
        })
    await database.execute(query)
    return True
