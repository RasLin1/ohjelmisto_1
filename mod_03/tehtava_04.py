vuosi = int(input("Tarkista jos vuosi oli karkausvuosi: "))

tarkistus_lasku = vuosi/4

if tarkistus_lasku % 1 == 0:
    print(f"Vuosi {vuosi} oli karkausvuosi")
else:
    print(f"Vuosi {vuosi} ei ollut karkausvuosi")