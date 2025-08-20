hyttiluokka  = input("Mikäon  hyttiluokkasi? ")

if hyttiluokka == "lux" or "Lux" or "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")

elif hyttiluokka == "a" or "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")

elif hyttiluokka == "b" or "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")

elif hyttiluokka == "c" or "C":
    print("C on ikkunaton hytti autokannen alapuolella.")

else:
    print("Virrheellinen hyttiluokka")