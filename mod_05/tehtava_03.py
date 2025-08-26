import math

number = int(input("Anna numero: "))
is_prime = True

for i in range(2, int(math.sqrt(number)) + 1):
    if number % i == 0:
        is_prime = False
        break
if is_prime == True:
    print(f"{number} on alkuluku!")

elif is_prime == False:
    print(f"{number} ei ole alkuluku!")
    