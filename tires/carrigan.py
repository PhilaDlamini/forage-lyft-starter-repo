from tires.tire import Tire

class CarriganTire(Tire):

    def __init__(self, sensor_values):
        self.__sensor_values = sensor_values

    def needs_service(self) -> bool:
        for value in self.__sensor_values:
            if value >= 0.9: 
                return True
            
        return False
