from seasons import get_birthday_date
import pytest
from datetime import date

def test_get_birthday_date():
    assert get_birthday_date("1984-05-15") == date(1984, 5, 15)


