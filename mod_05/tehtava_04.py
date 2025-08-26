cities = []
city_amount = 0

while city_amount < 5:
    temp_name_holder = input("Anna kaupungin nimi: ")
    cities.append(temp_name_holder)
    city_amount = city_amount + 1

for x in cities:
    print(x)