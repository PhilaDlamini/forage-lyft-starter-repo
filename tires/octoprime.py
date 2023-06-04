from tires.tire import Tire

class OctoprimeTire(Tire):

    def __init__(self, sensor_values):
        self.__sensor_values = sensor_values

    def needs_service(self) -> bool:
        sum = 0
        for value in self.__sensor_values:
            sum += value
            
        return sum >= 3
