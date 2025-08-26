import random
number_found = False
dice_sides = int(input("Anna nopan maksimisilmäluku: "))
current_number = 0
desired_number = dice_sides


def dice(x):
    current_number = random.randint(1, x)
    return current_number

while number_found == False:
    if current_number != desired_number and not number_found:
        current_number = dice(dice_sides)
        print (current_number)
    else:
        number_found = True