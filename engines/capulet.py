from engines.engine import Engine

class CapuletEngine(Engine):

    def __init__(self, last_service_mileage, current_mileage):
        self.__last_service_mileage = last_service_mileage
        self.__current_mileage = current_mileage

    def needs_service(self) -> bool:
        self.__current_mileage - self.__last_service_mileage > 30000
