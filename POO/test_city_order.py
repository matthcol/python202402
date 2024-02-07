import pytest

from city import City

@pytest.fixture
def city():
    return City("Pau", 77_000, 64)

@pytest.mark.parametrize(
    ["otherName", "otherPopulation", "otherDepartment"],
    [
        ("Toulouse", 77_000, 64),
        ("Pau", 77_000, 65),
        ("Pau", 77_001, 64),
    ],
    ids=[
        "name_after",
        "same_name_department_greater",
        "same_name_and_department_population_greater",
    ]
)
def test_lessThan_ok(city, otherName, otherPopulation, otherDepartment):
    other = City(otherName, otherPopulation, otherDepartment)
    assert city < other
    assert not city > other 
    
@pytest.mark.parametrize(
    ["otherName", "otherPopulation", "otherDepartment"],
    [
        ("Pau", 77_000, 64),
        ("Bayonne", 77_000, 64),
        ("Pau", 77_000, 63),
        ("Pau", 69_999, 64),
    ],
    ids=[
        "equals",
        "name_before",
        "same_name_department_lesser",
        "same_name_and_department_population_lesser",
    ]
)
def test_lessThan_ko(city, otherName, otherPopulation, otherDepartment):
    other = City(otherName, otherPopulation, otherDepartment)
    assert not city < other

@pytest.mark.parametrize(
    ["otherName", "otherPopulation", "otherDepartment"],
    [
        ("Bayonne", 77_000, 64),
        ("Pau", 77_000, 63),
        ("Pau", 69_999, 64),
    ],
    ids=[
        "name_before",
        "same_name_department_lesser",
        "same_name_and_department_population_lesser",
    ]
)
def test_greaterThan_ok(city, otherName, otherPopulation, otherDepartment):
    other = City(otherName, otherPopulation, otherDepartment)
    assert city > other
    assert not city < other 
    
@pytest.mark.parametrize(
    ["otherName", "otherPopulation", "otherDepartment"],
    [
        ("Pau", 77_000, 64),
        ("Toulouse", 77_000, 64),
        ("Pau", 77_000, 65),
        ("Pau", 77_001, 64),
    ],
    ids=[
        "equals",
        "name_after",
        "same_name_department_greater",
        "same_name_and_department_population_greater",
    ]
)
def test_greaterThan_ko(city, otherName, otherPopulation, otherDepartment):
    other = City(otherName, otherPopulation, otherDepartment)
    assert not city > other

@pytest.mark.parametrize(
    ["otherName", "otherPopulation", "otherDepartment"],
    [
        ("Pau", 77_000, 64),
        ("Toulouse", 77_000, 64),
    ],
    ids=[
        "other_equals",
        "other_greater",
    ]
)
def test_lessOrEquals_ok(city, otherName, otherPopulation, otherDepartment):
    other = City(otherName, otherPopulation, otherDepartment)
    assert city <= other
    
@pytest.mark.parametrize(
    ["otherName", "otherPopulation", "otherDepartment"],
    [
        ("Bayonne", 77_000, 64),
    ],
    ids=[
        "other_lesser",
    ]
)
def test_lessOrEquals_ko(city, otherName, otherPopulation, otherDepartment):
    other = City(otherName, otherPopulation, otherDepartment)
    assert not city <= other
    
@pytest.mark.parametrize(
    ["otherName", "otherPopulation", "otherDepartment"],
    [
        ("Pau", 77_000, 64),
        ("Bayonne", 77_000, 64),
    ],
    ids=[
        "other_equals",
        "other_lesser",
    ]
)
def test_greaterOrEquals_ok(city, otherName, otherPopulation, otherDepartment):
    other = City(otherName, otherPopulation, otherDepartment)
    assert city >= other
    
@pytest.mark.parametrize(
    ["otherName", "otherPopulation", "otherDepartment"],
    [
        ("Toulouse", 77_000, 64),
    ],
    ids=[
        "other_greater",
    ]
)
def test_greaterOrEquals_ko(city, otherName, otherPopulation, otherDepartment):
    other = City(otherName, otherPopulation, otherDepartment)
    assert not city >= other
    
@pytest.mark.parametrize(
    ["other"],
    [
        ("Pau",),
        (64,),
        (True,),
    ],
    ids=[
        "str", 
        "int",
        "bool"
    ]
)
def test_comparison_ko_heterogenous(city, other):
    assert city.__lt__(other) is NotImplemented
    assert city.__le__(other) is NotImplemented
    assert city.__gt__(other) is NotImplemented
    assert city.__ge__(other) is NotImplemented