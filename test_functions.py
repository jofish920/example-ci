from functions import add, subtract


# add the following imports in step 11
#  from functions import convert_fahrenheit_to_celsius as f2c
#  import pytest


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'


def test_subtract():
    assert subtract(2, 3) == -1


# uncomment the following test in step 11
# def test_convert_fahrenheit_to_celsius():
#    assert f2c(32) == 0
#    assert f2c(122) == pytest.approx(50)
#    with pytest.raises(AssertionError):
#        f2c(-600)
