number_list = []
largest_numbers = []
number_amount = 5

while True:
    temp_num = int(input("Anna numero: "))
    if temp_num > 0:
        number_list.append(temp_num)
    else:
        for x in range(number_amount):
            temp_num_large = max(number_list)
            largest_numbers.append(temp_num_large)
            number_list.remove(temp_num_large)
        print(largest_numbers)
        break




