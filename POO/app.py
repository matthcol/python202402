from city import City, CoastalCity

def main():
    city1 = City('Pau', 77_000, 64)
    city1copy = City('Pau', 77_000, 64)
    city2 = City('Toulouse', 470_000, 31)
    print(city1 == city2, city1 == city1)
    print(city1 != city2, city1 != city1)
    print(city1 == city1copy, city1 != city1copy)
    # print(city1 < city2, city1 <= city1, city1 > city1, city1 >= city1)
    for city in city1, city2:
        print("City:", city)
        print("\t-name:", city.name)
        print("\t-population:", city.population)
        print("\t-department:", city.department)
        print()
        city += 10
        city += -100
        city -= 20
    print(city1, city2)
    print("Difference of population:", city2.populationDifference(city1))
    coastalCity = CoastalCity("Bayonne", 49_000, 64, "Atlantic Ocean")
    coastalCity += 10
    print(coastalCity, type(coastalCity), coastalCity.populationDifference(city1))

if __name__ =="__main__":
    main()