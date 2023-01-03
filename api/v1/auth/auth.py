
from fastapi import APIRouter, Response, Depends
from fastapi_keycloak import UsernamePassword
from core.auth.keycloak import idp

auth_router = APIRouter()

@auth_router.get("/login", tags=["Auth"])
def login(user: UsernamePassword = Depends()):
    return idp.user_login(username=user.username, password=user.password.get_secret_value())


@auth_router.get("/callback", tags=["Auth"])
def callback(session_state: str, code: str):
    return idp.exchange_authorization_code(session_state=session_state, code=code)


@auth_router.get("/logout", tags=["Auth"])
def logout():
    return idp.logout_uri
