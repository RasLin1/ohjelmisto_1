allow_inch_to_cm = True

while allow_inch_to_cm == True:
    inch = float(input("Anna tuuma määrä: "))
    if inch >= 0.01:
        inch_to_cm = inch*2.54
        print(f"{inch} tuumaa on {inch_to_cm}cm")
    else:
        print("Tuo on negatiivinen numero!")
        allow_inch_to_cm = False