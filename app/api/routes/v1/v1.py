from fastapi import APIRouter, Form

from app.api.routes.v1.auth import CurrentUser
from app.db.tables.goods import Goods
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

from app.db.tables.auth import engine

router = APIRouter()


@router.post("/calculate")
def calculate(uan=Form(), count=Form(),
              weight=Form(), delivery=Form(),
              price_ozon=Form(), percent_ozon=Form(),
              u_r=Form(), s_r=Form()):
    try:
        price_rub = float(uan) * int(count) * float(u_r)
        delivery_rub = float(delivery) * float(s_r) * float(weight) * int(count)
        perc_ozon_rub = int(price_ozon) * (float(percent_ozon) / 100) * int(count)
        profit = float(price_ozon) - float(price_rub) - float(delivery_rub) - float(perc_ozon_rub)
        return RedirectResponse(f"/calc_page?result={profit}+₽", status_code=302)
    except Exception:
        return RedirectResponse("/calc_page?result=Неверный+ввод", status_code=302)


@router.get("/get_goods")
def get_goods(user_id=CurrentUser.user_id):
    if user_id:
        response_url = "/my_goods?="
        with Session(autoflush=False, bind=engine) as db:
            goods = db.query(Goods).filter_by(user_id=user_id).all()
            return response_url


