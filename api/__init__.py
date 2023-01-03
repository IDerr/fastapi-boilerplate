from fastapi import APIRouter
# from api.user.v1.user import user_router as user_v1_router
# from api.auth.auth import auth_router
from api.v1.auth.auth import auth_router
from api.v1.home.home import home_router

router = APIRouter()
# router.include_router(user_v1_router, prefix="/v1/users", tags=["User"])
# router.include_router(auth_router, prefix="/v1/auth", tags=["Auth"])
router.include_router(home_router, prefix="/v1/home", tags=["Home"])
router.include_router(auth_router, prefix="/v1/auth", tags=["Auth"])

# Export router
__all__ = ["router"]
