import pytest


def hello_world():
    print("hi")


@pytest.fixture()
def f_length() -> int:
    return 22


@pytest.fixture()
def f_width() -> int:
    return 8
