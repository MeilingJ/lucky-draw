from fastapi import APIRouter

from view.lucky_draw_running import router as running_router
from view.lucky_draw_setting import router as setting_router


api_v1_router = APIRouter()

api_v1_router.include_router(running_router, tags=["running"])
api_v1_router.include_router(setting_router, tags=["setting"])


