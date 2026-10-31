from parkingspot import ParkingSpot

class ParkingFloor:

    def __init__(self, floor_num, spots: list[ParkingSpot]):
        self._floornum = floor_num
        self._spots = spots

    def get_totalspots(self):
        return self._spots

    def get_floorNum(self):
        return self._floornum