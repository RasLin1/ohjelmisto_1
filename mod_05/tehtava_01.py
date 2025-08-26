import random

dice_amount = int(input("Kuinka monta arpakuutiota haluat heittää? "))
dice_numbers = []

for x in range(dice_amount):
    temp_num_holder = random.randint(1, 6)
    dice_numbers.append(temp_num_holder)

print(dice_numbers)