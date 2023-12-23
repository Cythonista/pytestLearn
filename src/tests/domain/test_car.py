from pytest import fixture

from src.app.domain.car import Car
from src.app.domain.car_name import CarName
from src.app.domain.car_width import CarWidth
from src.app.domain.car_height import CarHeight


class TestCar:
    @fixture
    def target(self):
        return Car(CarName("Car"), CarWidth(100), CarHeight(100))

    def test_get_car_name(self, target):
        """
        get_car_name関数のテスト
        getterから値を取得できること

        :param target:
        :return:
        """
        expected = Car(CarName("Car"), CarWidth(100), CarHeight(100))
        assert target.get_car_name == expected.get_car_name

    def test_get_car_width(self, target):
        """
        get_car_width関数のテスト
        getterから値を取得できること

        :param target:
        :return:
        """
        expected = Car(CarName("Car"), CarWidth(100), CarHeight(100))
        assert target.get_car_width == expected.get_car_width

    def test_get_car_height(self, target):
        """
        get_car_width関数のテスト
        getterから値を取得できること

        :param target:
        :return:
        """
        expected = Car(CarName("Car"), CarWidth(100), CarHeight(100))
        assert target.get_car_height == expected.get_car_height
