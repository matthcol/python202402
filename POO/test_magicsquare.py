import pytest

from magicsquare import magicSum

@pytest.mark.parametrize(
    ["n", "ms"], 
    [
        (1, 1), 
        (3, 15), 
        (5, 65),
        (12, 870)
    ]
)
def test_magicSum(n, ms):
    assert magicSum(n) == ms