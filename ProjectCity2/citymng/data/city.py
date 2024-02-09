# file city.py = module data.city
from dataclasses import dataclass

@dataclass
class City:
    name: str
    department: int