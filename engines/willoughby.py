from engines.engine import Engine

class WilloughbyEngine(Engine):

    def __init__(self, last_service_mileage, current_mileage):
        self.__last_service_mileage = last_service_mileage
        self.__current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.__current_mileage - self.__last_service_mileage > 60000
