import datetime

from pydantic import BaseModel


class ParkingSpotBase(BaseModel):
    id: int
    floor: int | None = None

    class Config:
        from_attributes = True


class TimeDelta(BaseModel):
    start_time: datetime.datetime
    end_time: datetime.datetime

    class Config:
        from_attributes = True


class ReserveParkingSpace(ParkingSpotBase, TimeDelta):
    user_id: int

    class Config:
        from_attributes = True


class CancelReserveParkingSpace(ParkingSpotBase):
    user_id: int

    class Config:
        from_attributes = True
