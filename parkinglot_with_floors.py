from parkinglot import ParkingLot


class ParkingLotWithFloors(ParkingLot):

    def __init__(self, floors, pricing):
        spots = []
        for floor in floors:
            spots.extend(floor.get_totalspots())

        super().__init__(spots, pricing)
