num_list = []

add_number = True

temp_holder = int(input("Anna numero: "))
if temp_holder > 0:
    for x in range(temp_holder + 1):
        counter = 1
        if x % 2 == 0:
            num_list.append(x)
            counter = counter + 1
        else:
            counter = counter + 1
for x in num_list:
    print(x)
