from datetime import date

from fastapi import APIRouter, Request, Depends

from app.bookings.dao import BookingDAO
from app.exceptions import RoomCannotBeBookedException
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(prefix="/bookings",
                   tags=["Bookings"],)

@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)): # -> list[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)

@router.post("")
async def add_booking(
        room_id: int,
        date_from: date,
        date_to: date,
        user: Users = Depends(get_current_user)):
    booking = await BookingDAO.add(
        user.id,
        room_id,
        date_from,
        date_to)
    if not booking:
        raise RoomCannotBeBookedException
    return booking

@router.delete("/{booking_id}")
async def remove_booking(
        booking_id: int,
        user: Users = Depends(get_current_user)):
    await BookingDAO.delete(id=booking_id, user_id=user.id)