num_list = [1, 2, 3, 4, 5]

def num_list_total_values(num_list):
    result = 0
    for x in num_list:
        result = result + x
    return result

total_value = num_list_total_values(num_list)
print(total_value)