from euclide import gcd

def main():
    a = 15
    b = 21
    g = gcd(a, b)
    print('Gcd of', a, 'and', b, 'is', g)
    # g = gcd('toto', 'titi')

if __name__ == '__main__':
    main()