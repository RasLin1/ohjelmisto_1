import random
number_found = False
current_number = 0
desired_number = 6

def dice():
    current_number = random.randint(1, 6)
    return current_number

while number_found == False:
    if current_number != desired_number and not number_found:
        current_number = dice()
        print (current_number)
    else:
        number_found = True
        