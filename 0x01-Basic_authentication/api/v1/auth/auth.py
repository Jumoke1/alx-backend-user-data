#!/usr/bin/env python3

from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the given path requires authentication.
        Currently returns False for all paths.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the value of the Authorization header if present.
        Currently returns None.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user based on the request.
        Currently returns None.
        """
        return None
