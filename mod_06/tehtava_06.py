def pizza_value_calc(width, price):
    area = (3.14*((width/100)/2)**2)
    area_price = (price/area)
    area_price_rounded = "%.2f" % area_price
    return area_price_rounded

pizza_areas = []
counter = 0
while counter < 2:
    temp_list = []
    temp_width = float(input("Mikä on pizzan halkaisija? "))
    temp_price = float(input("Mikä on pizzan hinta? "))
    pizza_area = pizza_value_calc(temp_width, temp_price)
    print(f"{temp_width}, {temp_price}, {pizza_area}")
    temp_list.append(pizza_area)
    temp_list.append(counter + 1)
    pizza_areas.append(temp_list)
    counter = counter + 1

for x, y in pizza_areas:
    print(f"Pizza {y} oli {x}€/m^2")

# if pizza_areas[1] > pizza_areas[2]: