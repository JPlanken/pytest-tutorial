# pytest-tutorial/tests/conftest.py

import pytest


@pytest.fixture()
def length() -> int:
    return 22


@pytest.fixture()
def width() -> int:
    return 8
