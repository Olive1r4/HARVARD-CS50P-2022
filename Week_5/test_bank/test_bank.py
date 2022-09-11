from bank import value

def test_value():
    assert value("hello") == 0
def test_value2():
    assert value("Hello") == 0
def test_value3():
    assert value("Hey") == 20
def test_value4():
    assert value("What's up") == 100