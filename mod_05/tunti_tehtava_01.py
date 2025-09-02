numbers = []

allow_number_list = True

while allow_number_list == True:
    if len(numbers) < 10:
        input_number = int(input("Anna numero:"))
        if input_number > -1:
            numbers.append(input_number)
        elif input_number <= -1:
            print("Älä anna negatiivista numeroa!")
    elif len(numbers) >= 10:
        allow_number_list = False
        numbers.sort()
        for x in numbers:
            print(x)
            
