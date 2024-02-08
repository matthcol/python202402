from point import Point

p1 = Point("O")
p2 = Point("A", 3.5, 4.5)
p3 = Point("B", 7.5, 1.5)
print(p1, p2, p3) 
print(p2.distance(p2))