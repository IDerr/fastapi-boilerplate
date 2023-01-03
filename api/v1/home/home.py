from fastapi import APIRouter, Response, Depends
from core.fastapi.dependencies import PermissionDependency, AllowAll
from core.db.prisma import prisma
import ujson

home_router = APIRouter()

@home_router.get("/health", dependencies=[Depends(PermissionDependency([AllowAll]))])
async def home():
    return Response("OK", status_code=200)

