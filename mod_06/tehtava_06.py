import math

def pizza_value_calc(width, price):
    area = (3.14*((width/100)/2)**2)
    area_price = (price/area)
    return area_price

def decimal_rounder(number):
    number_rounded = "%.2f" % number
    return number_rounded

pizza_areas = []
counter = 0
while counter < 2:
    temp_list = []
    temp_width = float(input("Mikä on pizzan halkaisija? "))
    temp_price = float(input("Mikä on pizzan hinta? "))
    pizza_area = pizza_value_calc(temp_width, temp_price)
    temp_list.append(pizza_area)
    temp_list.append(counter + 1)
    pizza_areas.append(temp_list)
    counter = counter + 1

cheaper_pizza = math.inf
cheap_pizza_number = 0

for x, y in pizza_areas:
    if cheaper_pizza > x:
        cheaper_pizza = x
        cheap_pizza_number = y
    else:
        cheaper_pizza = cheaper_pizza
        cheap_pizza_number = cheap_pizza_number
    
cheaper_pizza_rounded = decimal_rounder(cheaper_pizza)
print(f"Pizza {cheap_pizza_number} oli {cheaper_pizza_rounded}€/m^2")

