from functools import total_ordering
from typing import Self  \
    , override # since python 3.12

@total_ordering
class City: # inherits class object
    """representation of a french city with its name, population and department
    """
    
    def __init__(self, name: str, population: int, department: int):
        self.name = name
        self.population = population
        self.department = department
        
    # used by both builtins str() and repr() if no __str__
    @override
    def __repr__(self) -> str:
        return f"City[{self.name}, pop={self.population}, dept={self.department}]"
    
    @override
    def __str__(self) -> str:
        return f"{self.name} (pop={self.population}, dept={self.department})"
    
    # defines both == and !=
    # rules of relation of equivalence: reflexive, commutative, transitive
    @override
    def __eq__(self, other: object) -> bool:
        # if type(other) is not City:
        if not isinstance(other, City): # accept sub-classes
            return NotImplemented
        return (self.name, self.population, self.department) == (other.name, other.population, other.department)
    
    
    # define both < and >: criteria order name, department, population 
    def __lt__(self, other: object) -> bool:
        # if type(other) is not City:
        if not isinstance(other, City):
            return NotImplemented
        return (self.name, self.department, self.population) < (other.name, other.department, other.population)
    
    #  += -=
    def __iadd__(self, value: int) -> Self:
        self.population += value
        return self
    
    def __isub__(self, value: int) -> Self:
        return self.__iadd__(-value)
    
    def populationDifference(self, other: Self) -> int:
        return self.population - other.population
    
    
class CoastalCity(City):
    
    def __init__(self, name, population, department, marine):
        super().__init__(name, population, department)
        self.marine = marine
        
    @override
    def __repr__(self) -> str:
        return f"CoastalCity[{self.name}, pop={self.population}, dept={self.department}, marine={self.marine}]"
    
    @override
    def __str__(self) -> str:
        return f"{self.name} (pop={self.population}, dept={self.department}) near {self.marine}"
        
    
    
    