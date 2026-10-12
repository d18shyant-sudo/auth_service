from auth_service.auth_routes.routes import router as account_router
from fastapi import APIRouter
router = APIRouter()
router.include_router(account_router)