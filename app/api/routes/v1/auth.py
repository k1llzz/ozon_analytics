from fastapi import APIRouter, Form

from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

from app.db.tables.auth import engine, User

router = APIRouter()


class CurrentUser:
    user_id = None


@router.post("/auth")
def auth(email=Form(), psw=Form()):
    if "@" not in email or len(psw) < 3:
        return RedirectResponse("/auth?error=Неверное+имя+пользователя", status_code=302)
    else:
        with Session(autoflush=False, bind=engine) as db:
            if db.query(User).filter_by(email=email).first():
                return RedirectResponse("/auth?error=Пользователь+с+таким+email+уже+существует", status_code=302)
            else:
                user = User(email=email, password=psw)
                db.add(user)
                db.commit()
                CurrentUser.user_id = db.query(User).filter_by(email=email).first().id
            return RedirectResponse("/ozon_analytics", status_code=302)


@router.post("/entry")
def entry(email=Form(), psw=Form()):
    with Session(autoflush=False, bind=engine) as db:
        user = db.query(User).filter_by(email=email).first()
        if not user:
            return RedirectResponse("/entry?error=Пользователя+с+таким+email+не+существует", status_code=302)
        else:
            if user.password != psw:
                return RedirectResponse("/entry?error=Неверный+пароль", status_code=302)
            else:
                CurrentUser.user_id = db.query(User).filter_by(email=email).first().id
            return RedirectResponse("/ozon_analytics", status_code=302)

