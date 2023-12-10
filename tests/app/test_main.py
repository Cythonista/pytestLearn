from src.app import main
from pytest_mock import MockerFixture


def test_add():
    actual = main.add(1, 2)
    expected = 3

    assert actual == expected


def test_sub():
    actual = main.sub(3, 2)
    expected = 1

    assert actual == expected


def target_get_random():
    return 1


def test_get_random(mocker: MockerFixture):
    mocker.patch("src.app.main.get_random", target_get_random)
    actual = main.get_random()
    assert actual == 1
