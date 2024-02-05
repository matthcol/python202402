import pytest

from euclide import gcd

def test_gcd_nominal():
    assert gcd(21, 15) == 3

def test_gcd_one_equals_1():
    assert gcd(1, 5) == 1

@pytest.mark.parametrize(
    ['a', 'b', 'expected_result'], 
    [
        (1, 1, 1),
        (1, 5, 1),
        (5, 1, 1),
        (15, 21, 3),
        (21, 15, 3),
        (5, 5, 5),
    ], 
    ids=[
        'all 1',
        'first 1',
        'second 1',
        'first lesser than second',
        'first greater than second',
        'all equals'
    ])    
def test_gcd(a, b, expected_result):
    assert gcd(a, b) == expected_result

@pytest.mark.skip('Errors not managed yet')
def test_gcd_one_negative_or_null():
    assert gcd(1, 0) == 'I dont know'
    

