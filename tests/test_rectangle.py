# pytest-tutorial/tests/test_geometry.py
import pytest
from pytest import mark

from geometry.rectangle import Rectangle


@mark.geometry
class GeometryTests:
    @mark.perimeter
    def test_geometry_perimeter(self, length, width):
        rec = Rectangle(length, width)
        assert rec.area() == length * width, "area is calculated"

    @mark.area
    @mark.parametrize(
        "length,width,expected",
        [
            (1, 2, 2),
            (4, 100, 400),
            (3, 0, 0),
            (1, 999999999999999, 999999999999999),
            pytest.param(1, -1, 1, marks=pytest.mark.xfail),
        ],
    )
    def test_geometry_area_parametrized(self, length, width, expected):
        rec = Rectangle(length, width)
        assert rec.area() == expected, "area is calculated"
        assert rec.area() >= 0, "area is bigger than zero"

    @mark.area
    def test_geometry_area_error(self):
        with pytest.raises(ValueError):
            Rectangle(-1, 3).area()
        with pytest.raises(TypeError):
            Rectangle(-1, "String").area()
