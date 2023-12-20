from src.app.domain.car_name import CarName


class Car(object):
    def __init__(self, car_name: CarName, width, height) -> None:
        self.__car_name = car_name
        self.__width = width
        self.__height = height

    @property
    def get_name(self) -> CarName:
        return self.__car_name

    @property
    def get_width(self) -> int:
        return self.__width

    @property
    def get_height(self) -> int:
        return self.__height
