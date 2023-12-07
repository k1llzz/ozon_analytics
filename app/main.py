from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.api.routes import router


def get_application() -> FastAPI:
    application = FastAPI()
    application.mount("/ozon_analytics", StaticFiles(directory="./frontend/html/main_page", html=True), name="main_page")
    application.mount("/auth", StaticFiles(directory="./frontend/html/auth", html=True), name="auth")
    application.mount("/entry", StaticFiles(directory="./frontend/html/entry", html=True), name="entry")
    application.mount("/calc_page", StaticFiles(directory="./frontend/html/calc_page", html=True), name="calc_page")
    application.mount("/my_goods", StaticFiles(directory="./frontend/html/my_goods", html=True), name="my_goods")
    application.include_router(router)
    return application


app = get_application()
