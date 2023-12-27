from dataclasses import FrozenInstanceError

from pytest import fixture, raises

from src.app.domain.car_height import CarHeight


class TestCarHeight:
    @fixture
    def target(self):
        return CarHeight(100)

    def test_car_height(self, target):
        """
        car_height関数のテスト
        getterから値を取得できること

        :param target:
        :return:
        """
        expected = CarHeight(100)
        assert target.car_height == expected.car_height

    def test_dataclass_frozen(self, target):
        """
        dataclass frozenのテスト
        無理やりインスタンス変数の中身を変更しようとしてFrozenInstanceErrorが出ること
        :param target:
        :return:
        """
        with raises(FrozenInstanceError):
            target.car_height = CarHeight(120)

    def test_dataclass_slots(self, target):
        """
        dataclass slotsのテスト
        存在しないインスタンス変数に値を格納してTypeErrorが出ること

        :param target:
        :return:
        """
        with raises(TypeError):
            target.nothing_variable = CarHeight(100)
