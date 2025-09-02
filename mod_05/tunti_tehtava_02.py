num_list = []

add_number = True

while add_number == True:
    temp_holder = int(input("Anna numero: "))
    if temp_holder > 0:
        num_list.append(temp_holder)
    elif temp_holder <= 0:
        odd_num_list = []
        for x in num_list:
            if x % 2 == 1:
                odd_num_list.append(x)
        for x in odd_num_list:
            print(x)
