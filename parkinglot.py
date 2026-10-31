from parkingspot import ParkingSpot
from vehicle import Vehicle, VehicleType
from pricingStrategy import Pricing
from ticket import Ticket
import time
class ParkingLot:

    def __init__(self,spots:list[ParkingSpot],pricing:Pricing):

        self._spots = spots
        self._pricing = pricing
        self._tickets = {}


    def park(self,vehicle:Vehicle,start_time=None):

        for spot in self._spots:

            if spot.is_spotFree() and spot.get_spot_type()==vehicle.get_vehicleType():
                spot.occupy()
                if start_time is None:
                    start_time = time.time()
                ticket = Ticket(spot,vehicle,start_time)
                self._tickets[ticket.get_ticket_id()]=ticket
                return ticket
        raise ValueError ("No Parking Spots available")

    def unpark(self,ticket_id,exit_time=None):

        if ticket_id not in self._tickets:
            raise ValueError(" Invalid TicektId")

        ticket = self._tickets[ticket_id]
        if exit_time is None:
            exit_time = time.time()

        entry = ticket.get_start_time()
        duration = exit_time-entry
        Vehicle = ticket.get_vehicle()
        spot = ticket.get_spot()
        spot.vacate()
        self._tickets.pop(ticket_id)
        return self._pricing.price(Vehicle,duration)



    def availaible_spots(self,vehicleType:VehicleType):
        
        count = 0
        for spot in self._spots:
            if spot.is_spotFree() and spot.get_spot_type() == vehicleType:
                count+= 1
        return count