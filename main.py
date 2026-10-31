from vehicle import Vehicle, VehicleType
from parkingspot import ParkingSpot
from parkingfloor import ParkingFloor
from parkinglot_with_floors import ParkingLotWithFloors
from pricingStrategy import HourlyPricing
from parkinglot import ParkingLot

spots = [
    ParkingSpot(1, VehicleType.CAR),
    ParkingSpot(2, VehicleType.BIKE),
    ParkingSpot(3,VehicleType.CAR),
    ParkingSpot(4, VehicleType.BIKE),
    ParkingSpot(5,VehicleType.TRUCK)
]

car1 = Vehicle('dx456',VehicleType.CAR)
car2 = Vehicle('WCR53',VehicleType.CAR)
car3 = Vehicle('Pxq53',VehicleType.CAR)

bike1 = Vehicle('MX098',VehicleType.BIKE)
bike2 = Vehicle('ER578',VehicleType.BIKE)

truck1 = Vehicle('BVC98',VehicleType.TRUCK)

lot = ParkingLot(spots,HourlyPricing())

tick1 = lot.park(car1,0)
tick2 = lot.park(car2,0)
for tick in [tick1,tick2]:
    print(tick.get_ticket_id(),tick.get_spot().get_spot_id(),tick.get_start_time(),tick.get_vehicle().get_vehiclePlate())

print(lot.availaible_spots(VehicleType.CAR))
try:
    tick3 = lot.park(car3,0)
except Exception as error:
    print(f"Unable to park {car3.get_vehiclePlate()}: {error}")

price = lot.unpark(tick1.get_ticket_id(),7000)
print(price)
tick3 = lot.park(bike1,3000)
price = lot.unpark(tick3.get_ticket_id(),10000)
print(price)


# The same ParkingLot behavior can use multiple floors through the adapter.
floor1 = ParkingFloor(
    1,
    [
        ParkingSpot(101, VehicleType.CAR),
        ParkingSpot(102, VehicleType.BIKE),
    ],
)
floor2 = ParkingFloor(
    2,
    [
        ParkingSpot(201, VehicleType.CAR),
        ParkingSpot(202, VehicleType.TRUCK),
    ],
)

floor_lot = ParkingLotWithFloors([floor1, floor2], HourlyPricing())

floor_car = Vehicle("F-CAR-1", VehicleType.CAR)
floor_truck = Vehicle("F-TRUCK-1", VehicleType.TRUCK)

floor_car_ticket = floor_lot.park(floor_car, start_time=0)
floor_truck_ticket = floor_lot.park(floor_truck, start_time=0)

assert floor1.get_floorNum() == 1
assert floor2.get_floorNum() == 2
assert floor_lot.availaible_spots(VehicleType.CAR) == 1
assert floor_lot.availaible_spots(VehicleType.BIKE) == 1
assert floor_lot.availaible_spots(VehicleType.TRUCK) == 0

print(
    "Car parked on floor",
    floor1.get_floorNum(),
    "at spot",
    floor_car_ticket.get_spot().get_spot_id(),
)
print(
    "Truck parked on floor",
    floor2.get_floorNum(),
    "at spot",
    floor_truck_ticket.get_spot().get_spot_id(),
)
print("Floor parking fee:", floor_lot.unpark(floor_car_ticket.get_ticket_id(), 3600))
print("Floor parking fee:", floor_lot.unpark(floor_truck_ticket.get_ticket_id(), 3600))