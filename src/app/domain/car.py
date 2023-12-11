

class Car(object):
    def __init__(self, name, width, height):
        self.__name = name
        self.__width = width
        self.__height = height

    @property
    def get_name(self) -> str:
        return self.__name

    @property
    def get_width(self) -> int:
        return self.__width

    @property
    def get_height(self) -> int:
        return self.__height
