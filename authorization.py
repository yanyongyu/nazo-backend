#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-04-25 17:59:42
@LastEditors: yanyongyu
@LastEditTime: 2020-04-25 19:49:28
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

from datetime import datetime, timedelta

import jwt
from jwt import PyJWTError
from fastapi import status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from model import User
from form import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

# generated by openssl
# $ openssl rand -hex 32
SECRET_KEY = "dec9c7b435063f60f8b5022827d8caf1fe917fb8c915ba112eaf2d61c5c095f0"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def authenticate_user(username: str, password: str):
    user = User.get(username)
    if not user:
        user = User[username] = {"username": username, "password": password}
    if password != user["password"]:
        return False
    return user


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)):
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
    user = User.get(token_data.username)
    if user is None:
        raise credentials_exception
    return user
