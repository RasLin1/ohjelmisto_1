import random

game_number = random.randint(1, 10)

while True:
    guess = int(input("Arvaa numero 1-10 välillä: "))
    if guess == game_number:
        print(f"Oikein, numero oli {game_number}")
        break
    elif guess > game_number:
        print("Liian suuri arvaus")
    elif guess < game_number:
        print("Liian pieni arvaus")
