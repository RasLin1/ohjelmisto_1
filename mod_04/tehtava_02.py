while True:
    inch = int(input("Anna tuuma määrä: "))
    if inch >= 1:
        inch_to_cm = inch*2.54
        print(f"{inch} tuumaa on {inch_to_cm}cm")
    else:
        print("Tuo on negatiivinen numero!")
        break