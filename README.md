Ozon_Analytics

Для корректной работы с проектом, нужно предпринять следующие шаги:
1) Склонировать репозиторий
2) Создать базу данных Postgres и прописать настройки для нее в alembic.ini, а также поменять пути к ней в app/db/tables/*
3) Вписать команду alembic upgrade head, для того, чтобы накатить миграции на БД
4) python cli.py - для запуска приложения
5) localhost/ozon_analytics - главная страница 