from dataclasses import dataclass


@dataclass(init=True, frozen=True, slots=True)
class CarWidth(object):
    car_width: int

    @property
    def car_width(self) -> int:
        return self.car_width
