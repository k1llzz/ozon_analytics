from fastapi import APIRouter, status, Request
from starlette.responses import FileResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()


@router.get("/health")
def health():
    return status.HTTP_200_OK
