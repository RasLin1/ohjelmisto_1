number_list = []
largest_numbers = []
number_amount = 5
allow_loop = True

while allow_loop == True:
    temp_num = int(input("Anna numero: "))
    if temp_num > 0:
        number_list.append(temp_num)
    else:
        if len(number_list) < number_amount:
            for x in range(len(number_list)):
                temp_num_large = max(number_list)
                largest_numbers.append(temp_num_large)
                number_list.remove(temp_num_large)
                allow_loop = False
        else:
            for x in range(number_amount):
                temp_num_large = max(number_list)
                largest_numbers.append(temp_num_large)
                number_list.remove(temp_num_large)
                allow_loop = False
        print(largest_numbers)




