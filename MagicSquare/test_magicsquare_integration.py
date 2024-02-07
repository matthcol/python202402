"""
integration tests for all steps in magicness verification
functions: isMAgic, isMagicDetail
"""

import pytest

# functions to test
from magicsquare import isMagic, isMagicDetail
    
# square examples (TODO: use fixtures instead)
from squares import *

@pytest.mark.parametrize(
    ["square"],
    [
        (square_ok_3,),
        (square_ok_4_albrecht_durer,),
        (square_ok_5,),
        (square_ok_5_semi_diabolik,),
     #   (square_ok_8_benjamin_franklin,),
        (square_ok_8_general_cazalas,),
        (square_ok_8_willem_barink,),
        (square_ok_12_willem_barink,),
    ],
    ids=[
        "square_ok_3",
        "square_ok_4_albrecht_durer",
        "square_ok_5",
        "square_ok_5_semi_diabolik",
      #  "square_ok_8_benjamin_franklin",
        "square_ok_8_general_cazalas",
        "square_ok_8_willem_barink",
        "square_ok_12_willem_barink"
    ]
)
def test_isMagic_ok(square):
    assert isMagic(square)

@pytest.mark.parametrize(
    ["square"],
    [
        (square_ko_3_row,),
        (square_ko_3_col,),
        (square_ko_3_diag,),
        (square_ko_3_diag_one,),
        (square_ko_3_diag_two,),
        (square_ko_4_josep_maria_subirachs,),
        (square_ko_outOfRangeAbove,),
        (square_ko_outOfRangeUnder,),
    ],
    ids=[
        "square_ok_3",
        "square_ok_4_albrecht_durer",
        "square_ok_5",
        "square_ok_5_semi_diabolik",
        "square_ok_8_benjamin_franklin",
        "square_ok_8_general_cazalas",
        "square_ok_8_willem_barink",
        "square_ok_12_willem_barink"
    ]
)
def test_isMagic_ko(square):
    assert not isMagic(square)

@pytest.mark.parametrize(
    ["square", "n"],
    [
        (square_ok_3, 3),
        (square_ok_4_albrecht_durer, 3),
        (square_ok_5, 5),
        (square_ok_5_semi_diabolik, 5),
        # (square_ok_8_benjamin_franklin, 8),
        (square_ok_8_general_cazalas, 8),
        (square_ok_8_willem_barink, 8),
        (square_ok_12_willem_barink, 12),
    ],
    ids=[
        "square_ok_3",
        "square_ok_4_albrecht_durer",
        "square_ok_5",
        "square_ok_5_semi_diabolik",
       # "square_ok_8_benjamin_franklin",
        "square_ok_8_general_cazalas",
        "square_ok_8_willem_barink",
        "square_ok_12_willem_barink"
    ]
)
def test_isMagicDetail_ok(square, n):
    details = isMagicDetail(square)
    assert details['rows_ok'] == [ True for _ in range(n)]
    assert details['columns_ok'] == [ True for _ in range(n)]
    assert details['columns_ok'] == [ True, True ]
    assert details['range_ok'] == [ True, True, True, True, True ]

@pytest.mark.parametrize(
    [
        "square", 
        "expected_row_magicness", 
        "expected_column_magicness", 
        "expected_diagonal_magicness",
        "expected_range_flags",
    ],
    [
        (square_ko_3_row, [False, True, False], [True, True, True], [True, True], [True, True, True, True, True]),
        (square_ko_3_col, [True, True, True], [False, True, False], [True, True], [True, True, True, True, True]),
        (square_ko_3_diag, [True, True, True], [True, True, True], [False, False], [True, True, True, True, True]),
        (square_ko_3_diag_one, [True, True, False], [True, True, False], [False, True], [True, True, True, True, True]),
        (square_ko_3_diag_two, [False, True, True], [True, True, False], [True, False], [True, True, True, True, True]),
        (square_ko_4_josep_maria_subirachs, [False, False, False], [False, False, False], [False, False], [False, False, False, True, True]),
        (square_ko_outOfRangeAbove, [True, False, True], [False, True, False], [True, True], [False, True, False, True, False]),
        (square_ko_outOfRangeUnder, [True, True, True], [True, True, True], [True, True], [False, True, False, False, True]),
    ],
    ids=[
        "square_ok_3",
        "square_ok_4_albrecht_durer",
        "square_ok_5",
        "square_ok_5_semi_diabolik",
        "square_ok_8_benjamin_franklin",
        "square_ok_8_general_cazalas",
        "square_ok_8_willem_barink",
        "square_ok_12_willem_barink"
    ]
)
def test_isMagicDetail_ko(
    square, 
    expected_row_magicness, expected_column_magicness, 
    expected_diagonal_magicness,
    expected_range_flags
):
    details = isMagicDetail(square)
    assert details['rows_ok'] == expected_row_magicness
    assert details['columns_ok'] == expected_column_magicness
    assert details['columns_ok'] == expected_diagonal_magicness
    assert details['range_ok'] == expected_range_flags
