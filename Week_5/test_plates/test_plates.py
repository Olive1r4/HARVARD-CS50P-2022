from plates import is_valid

def test_is_valid():
    assert is_valid("Abcd1234") == False
    assert is_valid("AAA22A") == False
    assert is_valid("A1234") == False
    assert is_valid("AA02") == False
    assert is_valid("AA1#2") == False

