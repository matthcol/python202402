from city import City

def main():
    city1 = City('Pau', 77_000, 64)
    city2 = City('Toulouse', 470_000, 31)
    print(city1 == city2, city1 == city1)
    print(city1 != city2, city1 != city1)
    for city in city1, city2:
        print("City:", city)
        print("\t-name:", city.name)
        print("\t-population:", city.population)
        print("\t-department:", city.department)

if __name__ =="__main__":
    main()