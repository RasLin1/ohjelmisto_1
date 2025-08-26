import random

game_number = random.randint(1, 10)
game_allowed = True

while game_allowed == True:
    guess = int(input("Arvaa numero 1-10 välillä: "))
    if guess == game_number:
        print(f"Oikein, numero oli {game_number}")
        game_allowed = False
    elif guess > game_number:
        print("Liian suuri arvaus")
    elif guess < game_number:
        print("Liian pieni arvaus")
