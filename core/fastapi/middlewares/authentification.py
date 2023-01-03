from typing import Optional, Tuple

import jwt
from starlette.authentication import AuthenticationBackend
from starlette.middleware.authentication import (
    AuthenticationMiddleware as BaseAuthenticationMiddleware,
)
from starlette.requests import HTTPConnection
from fastapi_keycloak import OIDCUser

from core.config import config
from core.auth.keycloak import idp
from core.db.prisma import prisma
from ..schemas import CurrentUser


class AuthBackend(AuthenticationBackend):
    async def authenticate(
        self, conn: HTTPConnection
    ) -> Tuple[bool, Optional[CurrentUser]]:
        current_user = CurrentUser()
        authorization: str = conn.headers.get("Authorization")
        if not authorization:
            return False, current_user

        try:
            scheme, credentials = authorization.split(" ")
            if scheme.lower() != "bearer":
                return False, current_user
        except ValueError:
            return False, current_user

        if not credentials:
            return False, current_user

        current_user_function = idp.get_current_user()
        user: OIDCUser = current_user_function(
            token=credentials
        )
        # If user doesn't exist in DB, add it
        user_db = await prisma.user.upsert(where={
            "email": user.email
        }, data={
            "create": {
                "email": user.email
            },
            'update': {
                "email": user.email
            }
        })
        
        current_user.id = user_db.id
        current_user.email = user_db.email

        return True, current_user


class AuthenticationMiddleware(BaseAuthenticationMiddleware):
    pass