import pytest

# functions to test
from magicsquare import Square, magicSum, \
    isMagic, isMagicDetail, \
    areMagicRows, areMagicRowsDetail, \
    areAllNumbersInRange, areAllNumbersInRangeDetail
    
# square examples (TODO: use fixtures instead)
from squares import *

# constants
MS_1 = 1
MS_3 = 15
MS_4 = 34
MS_5 = 65
MS_8 = 260
MS_12 = 870


@pytest.mark.parametrize(
    ["n", "ms"], 
    [
        (1, MS_1), 
        (3, MS_3), 
        (5, MS_5),
        (12, MS_12)
    ],
    ids={
        "size_1",
        "size_3",
        "size_5",
        "size_12",
    }
)
def test_magicSum(n: int, ms: int):
    assert magicSum(n) == ms
    
    
@pytest.mark.parametrize(
    ["square", "n", "ms"], 
    [
        (square_ok_3, 3, MS_3),
        (square_ko_3_col, 3, MS_3),
        (square_ko_3_diag, 3, MS_3),
        (square_ok_4_albrecht_durer, 4, MS_4),
        (square_ko_4_josep_maria_subirachs, 4, 33),
        (square_ok_5, 5, MS_5),
        (square_ok_5_semi_diabolik, 5, MS_5),
        (square_ok_8_benjamin_franklin, 8, MS_8),
        (square_ok_8_general_cazalas, 8, MS_8),
        (square_ok_8_willem_barink, 8, MS_8),
        (square_ok_12_willem_barink, 12, MS_12),
        
    ],
    ids=[
        "square_ok_3",
        "square_ko_3_col",
        "square_ko_3_diag",
        "square_ok_4_albrecht_durer",
        "square_ko_4_josep_maria_subirachs",
        "square_ok_5",
        "square_ok_5_semi_diabolik",
        "square_ok_8_benjamin_franklin",
        "square_ok_8_general_cazalas",
        "square_ok_8_willem_barink",
        "square_ok_12_willem_barink"
    ]
)
def test_areMagicRows_ok(square: Square, n: int, ms: int):
    assert  areMagicRows(square, n, ms)
    


    
        
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
