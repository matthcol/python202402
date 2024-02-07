import pytest

from city import City

def test_equals_ok_same():
    city = City("Pau", 77_000, 64)
    assert city == city
    assert not city != city

def test_equals_ok_copy():
    city = City("Pau", 77_000, 64)
    cityClone = City("Pau", 77_000, 64)
    assert city == cityClone
    assert not city != cityClone    

def test_equals_ko_other_not_a_city():
    city = City("Pau", 77_000, 64)
    other = "Pau" 
    assert not city == other
    assert not other == city
    assert city != other
    assert other != city
    
@pytest.mark.parametrize(
    ["otherName", "otherPopulation", "otherDepartment"],
    [
        ("Aup", 77_000, 64),
        ("Pau", 77_001, 64),
        ("Pau", 77_000, 65),
        ("Toulouse", 470_000, 31),
    ],
    ids=[
        "different_name",
        "different_population",
        "different_department",
        "different_completly"
    ]
)
def test_equals_ko(otherName, otherPopulation, otherDepartment):
    city = City("Pau", 77_000, 64)
    other = City(otherName, otherPopulation, otherDepartment)
    assert not city == other
    assert not other == city
    assert city != other
    assert other != city