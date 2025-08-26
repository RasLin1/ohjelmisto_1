counter = 0
number_list = []
while counter < 1000:
    number_controller = counter/3
    if number_controller % 1 == 0:
        number_list.append(counter)
        counter += 1
    else:
        counter += 1
else:
    print()

print(f"Kolmella jaettavat numerot: {number_list}")
