def gcd(a: int, b: int) -> int:
    """Compute greater common diviser of strictly positive integers a and b

    Args:
        a (int): first integer (>0)
        b (int): second integer (>0)

    Raises:
        ValueError: if one arg is negative or zero
        
    Returns:
        int: gcd of a and b
    """
    # negative or null integers
    # sol1: assert => AssertionError
    # assert a > 0
    # assert b > 0
    
    # sol2: other exception
    if (a <= 0) or (b <= 0):
        raise ValueError("args a and b must be stritcly positive")
    
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
