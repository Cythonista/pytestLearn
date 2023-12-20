from pytest import fixture
from pytest import raises
from dataclasses import FrozenInstanceError

from src.app.domain.car_name import CarName


class TestCarName:
    @fixture
    def test_car_name(self):
        return CarName("TestCarName")

    def test_get_car_name(self, test_car_name):
        expected = CarName("TestCarName")
        assert test_car_name.get_car_name == expected.get_car_name

    def test_dataclass_frozen(self, test_car_name):
        with raises(FrozenInstanceError):
            test_car_name.car_name = "Test"

    def test_dataclass_slots(self, test_car_name):
        """
        dataclass slotsのテスト

        :param test_car_name:
        :return:
        """
        with raises(TypeError):
            test_car_name.test = "Test"
