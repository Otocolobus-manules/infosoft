import core.schemas.parking_schema as schemas


class ParkingService:
    def __init__(self, parking_repository):
        self.__parking_repository = parking_repository

    async def get_free_parking_spaces(
        self, time_schema: schemas.TimeDelta
    ) -> list[schemas.ParkingSpotBase]:
        return await self.__parking_repository.get_free_parking_spaces(time_schema)

    async def create_parking_spaces(self, count: int):
        return await self.__parking_repository.create_parking_spaces(count)

    async def reservation_parking_space(
        self, user, space: int, start_time, end_time
    ) -> schemas.ReserveParkingSpace:
        return await self.__parking_repository.reservation_parking_space(
            user, space, start_time, end_time
        )

    async def cancel_reservation_parking_space(
        self, user, space: int
    ) -> schemas.CancelReserveParkingSpace:
        return await self.__parking_repository.cancel_reservation_parking_space(
            user, space
        )
