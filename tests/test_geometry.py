# pytest-tutorial/tests/test_geometry.py

import pytest
from pytest import mark
from project_folder.geometry import Rectangle

@pytest.fixture()
def length() -> int:
    return 22

@pytest.fixture()
def width() -> int:
    return 8

@mark.geometry
class geometryTests():
    @mark.init
    def test_geometry_rectangle_init(self,length,width):
        rec = Rectangle(length,width)
        assert rec.length == length, "length is initialized"
        assert rec.width == width, "width is initialized"

    @mark.area
    def test_geometry_rectangle_area(self,length,width):
        rec = Rectangle(length,width)
        assert rec.area() == length*width, "area is calculated"

    @mark.perimeter
    def test_geometry_rectangle_perimeter(self,length,width):
        rec = Rectangle(length,width)
        assert rec.perimeter() == 2*length+2*width, "perimeter is calculated"