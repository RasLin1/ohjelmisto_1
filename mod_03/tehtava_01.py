kuha_koko = int(input("Kuinka suuri on kuhasi? "))
puutuva_pituus = 37 - kuha_koko

if kuha_koko < 37:
    print(f"Kuhasi on liian pieni, siitä  puuttuu {puutuva_pituus}cm. Heitä nyt se takasin sinne järveen!")

elif  kuha_koko >= 37:
    print("No nyt se on sopivan suuri!")