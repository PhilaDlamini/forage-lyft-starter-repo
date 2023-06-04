from car_factory import *
import datetime

if __name__ == "__main__":
    factory = CarFactory()
    car = factory.create_calliope(datetime.date.today(), datetime.date.today(), 435345, 23233)
    print("Needs service:", car.needs_service())