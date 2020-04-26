#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-04-25 15:26:36
@LastEditors: yanyongyu
@LastEditTime: 2020-04-25 19:47:38
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

from fastapi import status, FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from form import Token, User
from authorization import authenticate_user, create_access_token, get_current_user

app = FastAPI()


@app.post("/api/login", response_model=Token)
async def login(*, form: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form.username, form.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/whoami")
async def whoami(*, user: User = Depends(get_current_user)):
    print(user)
    return user
