from twttr import shorten

def test_shorten():
    # Check if acept uppercase, lowercase, pontuation and numbers
    assert shorten("hEllo1 World#!") == "hll1 Wrld#!"