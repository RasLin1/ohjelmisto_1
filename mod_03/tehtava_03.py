sukupuoli = input("Oletko mies tai nainen? ")
hemoglobiiniarvo = int(input("Mikä  on hemoglobiiniarvosi? "))

if sukupuoli in ["m", "M", "mies", "Mies"]:
    if hemoglobiiniarvo <= 134:
        print("Sinun hemoglobiini on lian alhanen")
    elif hemoglobiiniarvo > 134 and hemoglobiiniarvo < 195:
        print("Sinun hemoglobiini on sopivalla tasolla")
    elif hemoglobiiniarvo >= 195:
        print("Sinun hemoglobiini on lian korkea")

elif sukupuoli in ["f", "F", "nainen", "Nainen"]:
    if hemoglobiiniarvo <= 117:
        print("Sinun hemoglobiini on lian alhanen")
    elif hemoglobiiniarvo > 117 and hemoglobiiniarvo < 175:
        print("Sinun hemoglobiini on sopivalla tasolla")
    elif hemoglobiiniarvo >= 175:
        print("Sinun hemoglobiini on lian korkea")