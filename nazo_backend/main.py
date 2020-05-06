#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-04-25 15:26:36
@LastEditors: yanyongyu
@LastEditTime: 2020-04-30 17:49:29
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

from fastapi import status, FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from .answer import ANSWERS
from .model import database
from .query import get_simple_rank, get_rank, pass_puzzle
from .authorization import authenticate_user, create_access_token, get_current_user
from .form import TokenForm, UserForm, RankSimpleForm
from .form import StatusForm, RankForm, PuzzleInForm, PuzzleOutForm

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/api/login", response_model=TokenForm)
async def login(*, form: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form.username, form.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "Bearer"}


@app.get("/api/state", response_model=StatusForm)
async def status(*,
                 user: UserForm = Depends(get_current_user),
                 rank: RankSimpleForm = Depends(get_simple_rank)):
    return StatusForm(user=user, rank=rank)


@app.get("/api/rank", response_model=RankForm)
async def rank(*, rank: RankForm = Depends(get_rank)):
    return rank


@app.post("/api/puzzle/{puzzle_id}", response_model=PuzzleOutForm)
async def puzzle(puzzle_id: int,
                 *,
                 answer: PuzzleInForm,
                 user: UserForm = Depends(get_current_user)):
    if answer.answer == ANSWERS.get(puzzle_id):
        await pass_puzzle(puzzle_id, user)
        return PuzzleOutForm(passed=True)
    return PuzzleOutForm(passed=False)
