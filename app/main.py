from fastapi import FastAPI, Query, Depends

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users

app = FastAPI()

# Подключаем роутеры
app.include_router(router_users)
app.include_router(router_bookings)