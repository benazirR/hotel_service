from fastapi import APIRouter
from sqlalchemy import select

from app.bookings.models import Bookings
from app.database import async_session_maker

router = APIRouter(prefix="/bookings",
                   tags=["Bookings"],)

@router.get("")
async def get_bookings():
    pass

    # async with async_session_maker() as session:
    #     query = select(Bookings)  # Select * from bookings
    #     result = await session.execute(query)
    #     return result.mappings().all()
