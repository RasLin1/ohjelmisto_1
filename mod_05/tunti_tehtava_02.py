num_list = []

add_number = True

while add_number == True:
    temp_holder = int(input("Anna numero: "))
    if temp_holder > 0:
        num_list.append(temp_holder)
    elif temp_holder <= 0:
        even_num_list = []
        for x in num_list:
            if x % 2 == 0:
                even_num_list.append(x)
        for x in even_num_list:
            print(x)
