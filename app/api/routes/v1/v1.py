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


@router.get("/get_good_max")
def get_goods_max():
    user_id = CurrentUser.user_id
    if user_id:
        with Session(autoflush=False, bind=engine) as db:
            goods = db.query(Goods).filter_by(user_id=user_id).all()
            try:
                max_profit_good = goods[0]
            except Exception:
                return RedirectResponse(
                    "/my_goods?good=Не+добавлено+товаров",
                    status_code=302)
            for good in goods:
                if int(good.profit) > int(max_profit_good.profit):
                    max_profit_good = good
            return RedirectResponse(
                f"/my_goods?good=Название+{max_profit_good.name}+Ссылка+{max_profit_good.url}+Прибыль+{max_profit_good.profit}",
                status_code=302)
    else:
        return RedirectResponse(
            "/my_goods?good=Вы+не+авторизованы",
            status_code=302)


@router.get("/get_good_min")
def get_goods_min():
    user_id = CurrentUser.user_id
    if user_id:
        with Session(autoflush=False, bind=engine) as db:
            goods = db.query(Goods).filter_by(user_id=user_id).all()
            try:
                min_profit_good = goods[0]
            except Exception:
                return RedirectResponse(
                    "/my_goods?good=Не+добавлено+товаров",
                    status_code=302)
            for good in goods:
                if int(good.profit) < int(min_profit_good.profit):
                    min_profit_good = good
            return RedirectResponse(
                f"/my_goods?good=Название+{min_profit_good.name}+Ссылка+{min_profit_good.url}+Прибыль+{min_profit_good.profit}",
                status_code=302)
    else:
        return RedirectResponse(
            "/my_goods?good=Вы+не+авторизованы",
            status_code=302)


@router.post("/post_good")
def post_good(user_id=CurrentUser.user_id,
              name=Form(), url=Form(),
              profit=Form()):
    user_id = CurrentUser.user_id
    if user_id:
        with Session(autoflush=False, bind=engine) as db:
            good = Goods(name=name, url=url, profit=profit, user_id=CurrentUser.user_id)
            db.add(good)
            db.commit()
            return RedirectResponse("/my_goods", status_code=302)
    else:
        return RedirectResponse(
            "/my_goods?good=Вы+не+авторизованы",
            status_code=302)
