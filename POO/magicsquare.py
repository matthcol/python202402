from typing import List, Tuple, Dict

# type alias
Square = List[List[int]]

# function with types (hint or annotation type)
def magicSum(n: int) -> int:
    return n * (n**2 + 1) // 2

def isMagic(square: Square) -> bool:
    # TODO
    return False

def isMagicDetail(square: Square) -> Dict[str, List[bool]]:
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
    # TODO
    return False

def areMagicColumnsDetail(square: Square, ms: int) -> List[bool]:
    # TODO
    return [False, False, False]

def areMagicDiagonals(square: Square, ms: int) -> bool:
    # TODO
    return False

def areMagicDiagonalsDetail(square: Square, ms: int) -> Tuple[bool, bool]:
    # TODO
    return (False, False)

def areAllNumbersInRange(square: Square, n: int) -> bool:
    # TODO
    return False

def areAllNumbersInRangeDetail(square: Square, n: int) -> Tuple[bool, Dict[str, List[int]]]:
    """check if allnumbers in square are only used once and all from range[1..n²]

    Args:
        square (Square): square to check
        n (int): size of square

    Returns:
        Tuple[bool, Dict[str, List[int]]]: a pair with a boolean status if everything is good
        and a dictionnary of errors (possible keys are: missing, duplicate, out_of_range)
        
        Exemple of return value:
        - when all is ok
        (True, {})
        - when numbers are wrongly picked
        (False, {
            'duplicate': [3, 4],
            'missing': [1, 5, 6, 7, 9],
            'out_of_range': [-1, 0, 10] 
        })
    """
    # TODO
    return (False, {})
    
