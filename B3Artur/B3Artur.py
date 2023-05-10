def add_city_and_population(cities, populations):
    city = input("Sisestage linna nimi: ")
    population = int(input("Sisestage elanike arv: "))
    cities.append(city)
    populations.append(population)

def find_population_by_city(cities, populations):
    city = input("Sisestage linna nimi: ")
    if city in cities:
        index = cities.index(city)
        print("Linnas {} elab {} inimesed".format(city, populations[index]))
    else:
        print("Linn {} ei leidnud".format(city))

def display_sorted_cities_and_populations(cities, populations):
    for city, population in sorted(zip(cities, populations)):
        print(city, population)

def find_closest_city_by_population(cities, populations):
    target_population = int(input("Sisestage elanike arv: "))
    closest_city = None
    closest_distance = float("inf")
    for city, population in zip(cities, populations):
        distance = abs(population - target_population)
        if distance < closest_distance:
            closest_city = city
            closest_distance = distance
    print("Lähim linn {} elanikud: {}".format(target_population, closest_city))

def find_cities_with_fewer_population(cities, populations):
    n = int(input("Sisesta minimaalne elanike arv: "))
    cities_with_fewer = []
    for city, population in zip(cities, populations):
        if population < n:
            cities_with_fewer.append(city)
    print("Linnad, kus elab vähem inimesi {} inimesed:".format(n))
    print(cities_with_fewer)

def main():
    cities = []
    populations = []
    
    n = int(input("Sisestage täidetavate linnade arv (või 0, kui see pole piiratud): "))
    
    while n != 0 and len(cities) < n or n == 0:
        add_city_and_population(cities, populations)
    
    while True:
        print("Valige toiming:")
        print("1. Uurige, kui palju inimesi linnas on")
        print("2. Kuvage tähestikulises järjekorras linnade ja elanike loend")
        print("3. Leidke linn, kus elab lähim elanikkond")
        print("4. Leidke linnad, kus on vähem kui n elanikku")
        print("5. Sinu variant")
        print("0. Välju")
        
        choice = int(input("Sisestage toimingu number: "))
        if choice == 0:
            break
        elif choice == 1:
            find_population_by_city(cities, populations)
        elif choice == 2:
            display_sorted_cities_and_populations(cities, populations)
        elif choice == 3:
            find_closest_city_by_population(cities, populations)
        elif choice == 4:
            find_cities_with_fewer_population(cities, populations)
        elif choice == 5:
            pass
        else:
            print("Vale valik")

if __name__ == "__main__":
    main()
