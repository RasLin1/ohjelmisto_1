number_list = []
while True:
    temp_num = int(input("Anna numero: "))
    if temp_num > 0:
        number_list.append(temp_num)
    else:
        small_number = min(number_list)
        large_number = max(number_list)
        print(f"Pienin numero oli {small_number} ja suurin oli {large_number}")
        break