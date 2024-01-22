from dataclasses import FrozenInstanceError

from pytest import fixture, raises

from src.app.domain.car_name import CarName


class TestCarName:
    @fixture
    def target(self):
        return CarName("TestCarName")

    def test_car_name(self, target):
        """
        get_car_name関数のテスト
        getterから値を取得できること

        :param target:
        :return:
        """
        expected = CarName("TestCarName")
        assert target.car_name == expected.car_name

    def test_dataclass_frozen(self, target):
        """
        dataclass frozenのテスト
        無理やりインスタンス変数の中身を変更しようとしてFrozenInstanceErrorが出ること

        :param target:
        :return:
        """
        with raises(FrozenInstanceError):
            target.car_name = CarName("Test")

    def test_dataclass_slots(self, target):
        """
        dataclass slotsのテスト
        存在しないインスタンス変数に値を格納してTypeErrorが出ること

        :param target:
        :return:
        """
        with raises(TypeError):
            target.nothing_variable = CarName("Test")
