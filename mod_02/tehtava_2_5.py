import math

luoti = 13.3
naula = 32 * luoti
leiviska = 20 * naula

luoti_maara = int(input("Kuinka monta luotia? "))
naula_maara = int(input("Kuinka monta naulaa? "))
leiviska_maara = int(input("Kuinka monta leiviskää? "))

luoti_gramma = float(luoti_maara * luoti)
naula_gramma = float(naula_maara * naula)
leiviska_gramma = float(leiviska_maara * leiviska)
yhteensa = float(luoti_gramma + naula_gramma + leiviska_gramma)

print("Paino yhteenveto:")
print(f"Luoteja: {luoti_gramma}g")
print(f"Nauloja: {naula_gramma}g")
print(f"Leiviskoja: {leiviska_gramma}g")
print(f"Yhteensä: {yhteensa}")