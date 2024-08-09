#!/usr/bin/env python3
from flask import request
from typing import list, TypeVar


class Auth:
    def __init__(self)
    return self

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return false

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
