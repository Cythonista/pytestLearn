import pytest

from src.domain.car import Car
from pytest_mock import MockerFixture


@pytest.fixture
def test_car():
    return Car("Car", 100, 100)


def test_getter(test_car):
    assert test_car.get_name == "Car"
    assert test_car.get_width == 100
    assert test_car.get_height == 100
