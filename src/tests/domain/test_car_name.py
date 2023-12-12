import pytest

from src.app.domain.car_name import CarName


class TestCarName:
    @pytest.fixture
    def test_car_name(self):
        return CarName("TestCar")

    def test_getter(self, test_car_name):
        expected = CarName("TestCar")
        assert test_car_name.get_car_name == expected.get_car_name
