num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def number_separator(numbers, return_order):
    even_num_list = []
    odd_num_list = []
    for x in numbers:
        if x % 2 == 0:
            even_num_list.append(x)
        elif x % 2 == 1:
            odd_num_list.append(x)
    if return_order == 0:
        return even_num_list
    elif return_order == 1:
        return odd_num_list
    else:
        return "Return order not specified"

separator_return = int(input("0 = Parilliset | 1 = Parittomat | Mitkä haluat? "))
separated_numbers = number_separator(num_list, separator_return)
print(separated_numbers)