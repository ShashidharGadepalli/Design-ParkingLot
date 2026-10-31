from enum import Enum

class VehicleType(Enum):
    BIKE =1
    CAR =2
    TRUCK = 3


class Vehicle:

    def __init__(self,plate_id,vehicleType:VehicleType):

        self._plateId = plate_id
        self._vehicleType = vehicleType

    def get_vehiclePlate(self):
        return self._plateId

    def get_vehicleType(self):
        return self._vehicleType