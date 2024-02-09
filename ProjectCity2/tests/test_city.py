from citymng.data import City

def test_constructor():
    c = City("Pau", 64)
    assert c is not None