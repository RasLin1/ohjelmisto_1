def gallons_to_liters(gallons):
    liters = gallons*3.785
    return liters

gall_to_liter_allowed = True

while gall_to_liter_allowed == True:
    gallons_amount = float(input("Anna bensiini määrä nestegallonoina yhden decimaalin tarkudella: "))
    if gallons_amount > 0:
        liter_amount = gallons_to_liters(gallons_amount)
        print(f"{gallons_amount} gallonia on {liter_amount} litraa")
    else:
        print("Annoit negatiivisen numeron, lopetetaan!")
        gall_to_liter_allowed = False




