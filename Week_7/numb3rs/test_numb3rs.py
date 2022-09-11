from numb3rs import validate

def test_validate():
    assert validate("275.1.1.1") == False
    assert validate("Cat") == False
    assert validate("198.cat.cat.cat") == False
    assert validate("1.521.512.512") == False

