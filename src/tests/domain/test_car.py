import pytest

from src.app.domain.car import Car
from src.app.domain.car_name import CarName


class TestCar:
    @pytest.fixture
    def test_car(self):
        return Car(CarName("Car"), 100, 100)

    def test_getter(self, test_car):
        expected = Car(CarName("Car"), 100, 100)
        assert test_car.get_name == expected.get_name
        assert test_car.get_width == 100
        assert test_car.get_height == 100
