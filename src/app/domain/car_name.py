import dataclasses


@dataclasses.dataclass(frozen=True)
class CarName(object):
    car_name: str

    @property
    def get_car_name(self):
        return self.car_name
