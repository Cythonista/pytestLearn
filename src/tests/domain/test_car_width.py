from dataclasses import FrozenInstanceError

from pytest import fixture, raises

from src.app.domain.car_width import CarWidth


class TestCarWidth:
    @fixture
    def target(self):
        return CarWidth(100)

    def test_car_width(self, target):
        """
        get_car_width関数のテスト
        getterから値を取得できること

        :param target:
        :return:
        """
        expected = CarWidth(100)
        assert target.car_width == expected.car_width

    def test_dataclass_frozen(self, target):
        """
        dataclass frozenのテスト
        無理やりインスタンス変数の中身を変更しようとしてFrozenInstanceErrorが出ること
        :param target:
        :return:
        """
        with raises(FrozenInstanceError):
            target.car_width = CarWidth(120)

    def test_dataclass_slots(self, target):
        """
        dataclass slotsのテスト
        存在しないインスタンス変数に値を格納してTypeErrorが出ること

        :param target:
        :return:
        """
        with raises(TypeError):
            target.nothing_variable = CarWidth(100)
