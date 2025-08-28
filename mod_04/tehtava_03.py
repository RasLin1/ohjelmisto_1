number_list = []
allow_list_checker = True
while allow_list_checker == True:
    try:
        temp_num = input("Anna numero: ")
    except:
        print("Anna numero!")
    else:
        if temp_num > 0:
            number_list.append(temp_num)
        elif temp_num == 0 and number_list == []:
            print("Älä anna ensin 0!")
        else:
            small_number = min(number_list)
            large_number = max(number_list)
            print(f"Pienin numero oli {small_number} ja suurin oli {large_number}")
            allow_list_checker = False