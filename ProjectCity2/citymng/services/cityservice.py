from citymng.data import City

def process(city: City) -> bool:
    return len(city.name) > 0 and 0 < city.department < 1000