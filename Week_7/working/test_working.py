from working import convert
import pytest

def test_convert():
    assert convert("12 AM to 11 PM") == "00:00 to 23:00"
    assert convert("1 PM to 12 AM") == "13:00 to 00:00"
    assert convert("01 AM to 1 PM") == "01:00 to 13:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_ValueError():
    with pytest.raises(ValueError):
        convert("13 PM")