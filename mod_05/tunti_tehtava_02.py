num_list = []

valid_number = False

temp_holder = int(input("Anna positivinen kokonaisluku: "))
if temp_holder > 0:
    valid_number = True
    for x in range(temp_holder + 1):
        counter = 1
        if x % 2 == 0:
            num_list.append(x)
            counter = counter + 1
        else:
            counter = counter + 1

if valid_number:
    for x in num_list:
        print(x)
else:
    print("Huono numero!")
