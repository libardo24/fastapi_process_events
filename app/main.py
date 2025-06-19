from fastapi import FastAPI
from app.routers import api_router
from app.core.config import get_settings

app = FastAPI(
    title=get_settings().app_name,
    debug=get_settings().debug,
    version="1.0.0",
)

app.include_router(api_router, prefix=get_settings().api_v1_prefix)
