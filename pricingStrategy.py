from abc import ABC, abstractmethod
from vehicle import VehicleType
import math
class Pricing(ABC):

    @abstractmethod

    def price(self,vehicle,duration):
        pass


class HourlyPricing(Pricing):

    RATES = {
        VehicleType.BIKE: 10,
        VehicleType.CAR: 20,
        VehicleType.TRUCK: 30,
    }

    def __init__(self):
        self._rates = dict(HourlyPricing.RATES)

    def price(self, vehicle, duration):
        hours = max(1,math.ceil(duration/3600))

        return hours * self._rates[vehicle.get_vehicleType()]
