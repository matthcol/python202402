import pytest

from euclide import gcd

def test_gcd():
    assert gcd(21, 15) == 3

def test_gcd_one_equals_1():
    assert gcd(1, 5) == 1

@pytest.mark.skip('Errors not managed yet')
def test_gcd_one_negative_or_null():
    assert gcd(1, 0) == 'I dont know'
    

