
import sys


import citymng.data as d
from .services.cityservice import process


c = d.City('Pau', 64)
print(c)

# ok = process("Pau") # error type (MyPy)
ok = process(c)

# args CLI: sys.argv
# see also: https://docs.python.org/3/library/argparse.html
print("Args of this program:", sys.argv)