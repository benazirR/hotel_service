from sqlalchemy import Column, String, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.database import Base

class Rooms(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, nullable=False)
    hotel_id = Column(Integer, ForeignKey('hotels.id'), nullable=False)
    name = Column(String,nullable=False)
    description = Column(String,nullable=True)
    price = Column(Integer,nullable=False)
    services = Column(JSON, nullable=True)
    quantity = Column(Integer,nullable=False)
    image_id = Column(Integer)

    hotel = relationship("Hotels", back_populates="rooms")
    bookings = relationship("Bookings", back_populates="room")

    def __str__(self):
        return f"Room #{self.name}"