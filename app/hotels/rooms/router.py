from datetime import date, datetime, timedelta
from fastapi import Query

from app.hotels.rooms.dao import RoomDAO
from app.hotels.router import router

@router.get("/{hotel_id}/rooms")
async def get_rooms_by_time(
    hotel_id: int,
    date_from: date = Query(..., description=f"For example, {datetime.now().date()}"),
    date_to: date = Query(..., description=f"For example, {(datetime.now() + timedelta(days=14)).date()}")
):
    rooms = await RoomDAO.find_all(hotel_id, date_from, date_to)
    return rooms