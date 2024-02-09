
import sys

#from data.city import City

# import package data => execute __init__.py
# import data
import data as d
from services.cityservice import process

# import module city inside package data
# import data.city

# c = data.city.City('Pau', 64)
# c = data.City('Pau', 64)
c = d.City('Pau', 64)
print(c)

# ok = process("Pau") # error type (MyPy)
ok = process(c)

# args CLI: sys.argv
# see also: https://docs.python.org/3/library/argparse.html
print("Args of this program:", sys.argv)