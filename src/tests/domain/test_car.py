from pytest import fixture

from src.app.domain.car import Car
from src.app.domain.car_name import CarName
from src.app.domain.car_width import CarWidth
from src.app.domain.car_height import CarHeight


class TestCar:
    @fixture
    def target(self):
        return Car(CarName("Car"), CarWidth(100), CarHeight(100))

    def test_car_name(self, target):
        """
        car_name関数のテスト
        getterから値を取得できること

        :param target:
        :return:
        """
        expected = Car(CarName("Car"), CarWidth(100), CarHeight(100))
        assert target.car_name == expected.car_name

    def test_car_width(self, target):
        """
        car_width関数のテスト
        getterから値を取得できること

        :param target:
        :return:
        """
        expected = Car(CarName("Car"), CarWidth(100), CarHeight(100))
        assert target.car_width == expected.car_width

    def test_car_height(self, target):
        """
        car_width関数のテスト
        getterから値を取得できること

        :param target:
        :return:
        """
        expected = Car(CarName("Car"), CarWidth(100), CarHeight(100))
        assert target.car_height == expected.car_height
