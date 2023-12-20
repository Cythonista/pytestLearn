from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CarName(object):
    car_name: str

    @property
    def get_car_name(self) -> str:
        return self.car_name
