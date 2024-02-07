from typing import List, Tuple, Dict
from itertools import chain

# type alias
Square = List[List[int]]

# function with types (hint or annotation type)
def magicSum(n: int) -> int:
    return n * (n**2 + 1) // 2

def isMagic(square: Square) -> bool:
    n = len(square)
    ms = magicSum(n)
    return areMagicRows(square, n, ms) \
        and areMagicColumns(square, n, ms) \
        and areMagicDiagonals(square, n, ms) \
        and areAllNumbersInRange(square, n)

def isMagicDetail(square: Square) -> Dict[str, List[bool]]:
    n = len(square)
    square_n = n**2
    ms = magicSum(n)
    range_ok, range_ok_detail = areAllNumbersInRangeDetail(square, n)
    return {
        'rows_ok': areMagicRowsDetail(square, n, ms),
        'columns_ok': areMagicColumnsDetail(square, n, ms),
        'diagonals_ok': list(areMagicDiagonalsDetail(square, n, ms)),
        'range_ok': [
            range_ok,
            len(range_ok_detail['duplicate']) == 0,
            len(range_ok_detail['missing']) == 0,
            any(v <= 0 for v in range_ok_detail['out_of_range']),
            any(v > square_n for v in range_ok_detail['out_of_range']),
        ]
    }


def areMagicRows(square: Square, n: int, ms: int) -> bool:
    """check if all rows of a square are magic according to sum ms

    Args:
        square (Square): square to check
        ms (int): magic sum expected

    Returns:
        bool: True if all rows are magic
    """
    return all(sum(row) == ms for row in square)

def areMagicRowsDetail(square: Square, n: int, ms: int) -> List[bool]:
    """check if all rows of a square are magic according to sum ms

    Args:
        square (Square): square to check
        ms (int): magic sum expected

    Returns:
        List[bool]: list of magicness for each row
    """
    return [ sum(row) == ms for row in square ]


def areMagicColumns(square: Square, n: int, ms: int) -> bool:
    n = len(square)
    return all((sum(row[j] for row in square) == ms) for j in range(n))

def areMagicColumnsDetail(square: Square, n: int, ms: int) -> List[bool]:
    return [(sum(row[j] for row in square) == ms) for j in range(n)]

def areMagicDiagonals(square: Square, n: int, ms: int) -> bool:
    sum_diag1 = sum(square[i][i] for i in range(n))
    sum_diag2 = sum(square[i][-1-i] for i in range(n))
    return (sum_diag1==ms) and (sum_diag2==ms)

def areMagicDiagonalsDetail(square: Square, n: int, ms: int) -> Tuple[bool, bool]:
    sum_diag1 =  sum(square[i][i] for i in range(n))
    sum_diag2 =  sum(square[i][-1-i] for i in range(n))
    return (sum_diag1==ms, sum_diag2==ms)

def areAllNumbersInRange(square: Square, n: int) -> bool:
    # NB: not optimized algorithm
    square_n = n**2
    values_in_square = sorted(chain.from_iterable(square))
    expected_values = list(range(1, square_n+1)) 
    return (len(values_in_square) == square_n) \
        and values_in_square == expected_values

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
    
