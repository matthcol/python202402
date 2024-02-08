from dataclasses import dataclass
from typing import Self
import math

# https://docs.python.org/3/library/dataclasses.html

@dataclass
class Point:
    name: str
    x: float = 0
    y: float = 0
    
    def distance(self, other: Self) -> float:
        return math.hypot(self.x - other.x, self.y - other.y)