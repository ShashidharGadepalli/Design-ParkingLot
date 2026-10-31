from parkingspot import ParkingSpot
from vehicle import Vehicle

import uuid
class Ticket:

    def __init__(self,spot:ParkingSpot,vehicle:Vehicle,start_time):
        self._ticketId = str(uuid.uuid4())
        self._spot = spot
        self._vehicle = vehicle
        self._startTime = start_time

    def get_ticket_id(self):
        return self._ticketId

    def get_spot(self):
        return self._spot

    def get_vehicle(self):
        return self._vehicle

    def get_start_time(self):
        return self._startTime

    