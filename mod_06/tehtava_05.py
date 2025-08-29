num_list = [1, 2, 3, 4, 5, 6]


def odd_even_separator(num_list, desired_return):
    odd_num_list = []
    even_num_list = []
    for x in num_list:
        if x % 2 == 1:
            odd_num_list.append(x)
        elif x % 2 == 0:
            even_num_list.append(x)
    if desired_return == 0:
        return odd_num_list
    elif desired_return == 1:
        return even_num_list
    else:
        return "Error: desired return is invalid"

seperator_return = odd_even_separator(num_list, 1)
print(seperator_return)