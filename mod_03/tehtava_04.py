vuosi = int(input("Tarkista jos vuosi oli karkausvuosi: "))

if vuosi % 4 == 0 and vuosi %100 != 0 or vuosi % 400 == 0:
    print(f"Vuosi {vuosi} oli karkausvuosi")
else:
    print(f"Vuosi {vuosi} ei ollut karkausvuosi")