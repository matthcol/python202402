from squares import *
from magicsquare import isMagic, isMagicDetail

def main():
    for square in square_ok_3, square_ok_12_willem_barink, square_ko_3_row, square_ko_4_josep_maria_subirachs:
        ok = isMagic(square)
        detail = isMagicDetail(square)
        print("Square:")
        print(square)
        print("Magic:", ok)
        print("Magic (detail):", detail)
        print()
        
if __name__ == '__main__':
    main()