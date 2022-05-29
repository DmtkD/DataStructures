class Device:
    def __init__(self, type_of_device: str, name: str, year_of_manufacture: int, limit_of_measurement: int) -> None:
        self.__limit_of_measurement = limit_of_measurement
        self.__year_of_manufacture = year_of_manufacture
        self.__name = name
        self.__type_of_device = type_of_device

    def __str__(self) -> str:
        return f'Name: {self.__name}\n' \
        f'Type of device: {self.__type_of_device}\n' \
        f'Year of manufacture: {self.__year_of_manufacture}\n' \
        f'Limit of measurement: {self.__limit_of_measurement}\n'

    def get_limit_of_measurement(self):
        return self.__limit_of_measurement

    def get_year_of_manufacture(self) -> int:
        return self.__year_of_manufacture

    def __repr__(self) -> str:
        return self.__str__()
