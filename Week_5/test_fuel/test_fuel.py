from fuel import convert, gauge
import pytest

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_ValueError():
    with pytest.raises(ValueError):
        convert("Cat/Dog")

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/3") == 33



def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"