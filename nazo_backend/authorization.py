#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-04-25 17:59:42
@LastEditors: yanyongyu
@LastEditTime: 2020-05-06 11:34:20
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

from datetime import datetime, timedelta

import jwt
from jwt import PyJWTError
from fastapi import status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from .config import SECRET_KEY
from .model import database, User
from .form import TokenData, UserForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 720


async def authenticate_user(username: str, password: str):
    query = User.select().where(User.c.username == username)
    user = await database.fetch_one(query)

    if not user:
        query = User.insert().values(username=username, password=password)
        id_ = await database.execute(query)
        user = UserForm(id=id_,
                        username=username,
                        password=password,
                        register_time=datetime.now())
    elif user.password != password:
        return None
    else:
        user = UserForm(**dict(zip(UserForm.__fields__.keys(), user)))

    return user


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except PyJWTError:
        raise credentials_exception
    query = User.select().where(User.c.username == token_data.username)
    user = await database.fetch_one(query)
    if user is None:
        raise credentials_exception
    return UserForm(**dict(zip(UserForm.__fields__.keys(), user)))
