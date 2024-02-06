from typing import List, Tuple

# type alias
Square = List[List[int]]

# function with types (hint or annotation type)
def magicSum(n: int) -> int:
    return n * (n**2 + 1) // 2

def isMagic(square: Square) -> bool:
    # TODO
    return False

def isMagicDetail(square: Square):
    # TODO
    return {
        'rows_ok': [False, False, False],
        'columns_ok': [False, False, False],
        'diagonals_ok': [False, False],
    }


def areMagicRows(square: Square, ms: int) -> bool:
    """check if all rows of a square are magic according to sum ms

    Args:
        square (_type_): square to check
        ms (_type_): magic sum expected

    Returns:
        bool: True if all rows are magic
    """
    # TODO
    return False

def areMagicRowsDetail(square: Square, ms: int) -> List[bool]:
    """check if all rows of a square are magic according to sum ms

    Args:
        square (_type_): square to check
        ms (_type_): magic sum expected

    Returns:
        ?: list of magicness for each row
    """
    # TODO
    return [ False, False, False ]


def areMagicColumns(square: Square, ms: int) -> bool:
    pass

def areMagicColumnsDetail(square: Square, ms: int) -> List[bool]:
    pass

def areMagicDiagonals(square: Square, ms: int) -> bool:
    pass

def areMagicDiagonalsDetail(square: Square, ms: int) -> Tuple[bool, bool]:
    pass
