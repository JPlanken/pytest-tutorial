# pytest-tutorial/tests/test_geometry.py
import pytest
from pytest import mark

from project_folder.geometry import Rectangle


@mark.geometry
class geometryTests:
    def test_geometry_perimeter(self, f_length, f_width):
        rec = Rectangle(f_length, f_width)
        assert rec.area() == f_length * f_width, "area is calculated"

    @pytest.mark.parametrize(
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

    def test_geometry_area_error(self):
        with pytest.raises(ValueError):
            Rectangle(-1, 3).area()
        with pytest.raises(TypeError):
            Rectangle(-1, "String").area()
