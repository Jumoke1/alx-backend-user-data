#!/usr/bin/env python3
"""A module for authentication-related routines"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """converting the password to bytes"""
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password


class Auth:
    """auth class to interact with authentication database"""
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str):
        """ a method to register a user"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists")
            except NoResultFound:
                pass

    hased_password = self._hash_password(password)

    new_user = self._db.add_user(email=email, hashed_password=hased_password)

    return new_user
