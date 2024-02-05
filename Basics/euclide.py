def gcd(a, b):
    """Compute greater common diviser of strictly positive numbers a and b

    Args:
        a: first number (>0)
        b: second number (>0)

    Returns:
        gcd of a and b
    """
    while a != b:
        if a > b:
            a= a - b
        else:
            b = b - a
    return a
