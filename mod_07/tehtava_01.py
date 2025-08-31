seasons = ('talvi', 'kevät', 'kesä', 'syksy')

def season_checker(season_number):
    current_season = ''
    if season_number in (1, 2, 12):
        return seasons[0]
    elif season_number in (3, 4, 5):
        return seasons[1]
    elif season_number in (6, 7, 8):
        return seasons[2]
    elif season_number in (9, 10, 11):
        return seasons[3]
    else:
        return 'ei ole'

month_num = int(input("Anna kuukauden numero: "))
corresponding_season = season_checker(month_num)
print(f"Antamasi kuukausi on {corresponding_season} kuukausi!")