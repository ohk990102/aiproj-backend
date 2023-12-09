from fastapi import APIRouter
from routers.models import router as models_router
from routers.scans import router as scans_router

main_router = APIRouter(prefix="/api/v1", tags=["api"])
main_router.include_router(models_router)
main_router.include_router(scans_router)
