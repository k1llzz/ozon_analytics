from fastapi import APIRouter

from app.api.routes.admin.v1 import router as admin_router
from app.api.routes.v1.auth import router as user_router
from app.api.routes.v1.v1 import router as calc_router

router = APIRouter()

router.include_router(admin_router, tags=["admin"], prefix="/admin")
router.include_router(user_router, tags=["user"], prefix="/user")
router.include_router(calc_router, tags=["v1"], prefix="/v1")

