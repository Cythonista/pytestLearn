from dataclasses import dataclass

from src.app.domain.car_name import CarName
from src.app.domain.car_width import CarWidth
from src.app.domain.car_height import CarHeight


@dataclass(init=True, frozen=True, slots=True)
class Car(object):
    car_name: CarName
    car_width: CarWidth
    car_height: CarHeight

    @property
    def car_name(self) -> CarName:
        return self.car_name

    @property
    def car_width(self) -> CarWidth:
        return self.car_width

    @property
    def car_height(self) -> CarHeight:
        return self.car_height
