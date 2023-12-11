from typing import Optional

from fastapi import APIRouter, status, Request, HTTPException
from pydantic import Field
from sqlalchemy import delete
from sqlalchemy.orm import Session
from starlette.responses import FileResponse
from fastapi.templating import Jinja2Templates

from app.db.tables.auth import engine, User

router = APIRouter()


@router.get("/health")
def health():
    return status.HTTP_200_OK


@router.delete("/delete_user")
def delete_user(id: int):
    with Session(autoflush=False, bind=engine) as db:
        try:
            db.query(User).filter_by(id=id).delete()
            db.commit()
            return status.HTTP_202_ACCEPTED
        except Exception:
            raise HTTPException(status_code=404, detail="User not found")
