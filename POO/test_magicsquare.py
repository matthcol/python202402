import pytest

# functions to test
from magicsquare import magicSum, \
    areAllNumbersInRange, areAllNumbersInRangeDetail
    
# square examples (TODO: use fixtures instead)
from squares import *

@pytest.mark.parametrize(
    ["n", "ms"], 
    [
        (1, 1), 
        (3, 15), 
        (5, 65),
        (12, 870)
    ],
    ids={
        "size_1",
        "size_3",
        "size_5",
        "size_12",
    }
)
def test_magicSum(n, ms):
    assert magicSum(n) == ms
    
        
@pytest.mark.parametrize(
    ["square", "n"], 
    [
        (square_ok_3, 3),
        (square_ko_3_row, 3),
        (square_ok_12_willem_barink, 12),
    ],
    ids=[
        "magic_square_3",
        "not_magic_square_but_ok_with_range_3",
        "magic_square_12",
    ]
)
def test_areAllNumbersInRange_ok(square, n):
    assert areAllNumbersInRange(square, n)
    

@pytest.mark.parametrize(
    ["square", "n"], 
    [
        (square_ok_4_albrecht_durer, 4),
        (square_ko_outOfRangeAbove, 3),
        (square_ko_outOfRangeUnder, 3),
    ],
    ids=[
        "missing_and_repeated_values",
        "missing_and_value_after_range",
        "missing_and_value_before_range",
    ]
)
def test_areAllNumbersInRange_ko(square, n):
    assert not areAllNumbersInRange(square, n)

@pytest.mark.parametrize(
    ["square", "n"], 
    [
        (square_ok_3, 3),
        (square_ko_3_row, 3),
        (square_ok_12_willem_barink, 12),
    ],
    ids=[
        "magic_square_3",
        "not_magic_square_but_ok_with_range_3",
        "magic_square_12",
    ]
)
def test_areAllNumbersInRangeDetail_ok(square, n):
    ok, errors =  areAllNumbersInRangeDetail(square, n)
    assert ok
    assert errors == {}
    
def test_areAllNumbersInRangeDetail_ko_repeatedValue():
    ok, errors =  areAllNumbersInRangeDetail(square_ko_4_josep_maria_subirachs, 4)
    assert not ok
    assert errors['duplicate'] ==  [14, 10]
    assert errors['missing'] == [5, 12]

@pytest.mark.parametrize(
    ["square", "n", "missing", "outOfRange"],
    [
        (square_ko_outOfRangeUnder, 3, [2], [-1]),
        (square_ko_outOfRangeAbove, 3, [3], [13])
    ],
    ids=[
        "number_before_range",
        "number_after_range"
    ]
)
def test_areAllNumbersInRangeDetail_ko_outOfRange(square, n, missing, outOfRange):
    ok, errors =  areAllNumbersInRangeDetail(square, n)
    assert not ok
    assert errors['missing'] == missing
    assert errors['out_of_range'] == outOfRange
