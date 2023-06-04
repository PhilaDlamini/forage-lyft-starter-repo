from batteries.battery import Battery

class NubbinBattery(Battery):

    def __init__(self, last_service_date, current_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self) -> bool:
        threshold_date = self.__last_service_date.replace(year=self.__last_service_date.year + 4)
        return threshold_date < self.__current_date
