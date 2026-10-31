from vehicle import VehicleType

class ParkingSpot:

    def __init__(self,spot_id,spot_type:VehicleType):

        self._spotId = spot_id
        self._spotType = spot_type
        self._is_Free = True

    def get_spot_id(self):
        return self._spotId

    def get_spot_type(self):
        return self._spotType

    def is_spotFree(self):
        return self._is_Free

    def occupy(self):
        if not self._is_Free:
            raise ValueError(" Spot is not available")
        self._is_Free = False

    def vacate(self):
        self._is_Free = True

