from dataclasses import dataclass


@dataclass(init=True, frozen=True, slots=True)
class CarHeight(object):
    car_height: int

    @property
    def car_height(self) -> int:
        return self.car_height
