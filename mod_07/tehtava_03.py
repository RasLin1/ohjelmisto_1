airports = {}

allow_airport_program = True

def insert_airport(icao, name):
    icao_normalised = icao.upper()
    if icao_normalised in airports:
        return False
    airports[icao_normalised] = name
    return True
    
def search_airport(icao):
    icao_normalised = icao.upper()
    return airports.get(icao_normalised)

while allow_airport_program:
    program_determiner = int(input("Lisää lentokenttä(1), Hae lentokenttä(2), Lopeta(3) "))
    if program_determiner == 1:
        icao = input("Anna ICAO koodi: ")
        name = input("Anna lentokentän nimi: ")
        insert = insert_airport(icao, name)
        if insert:
            print("Lentokenttä lisätty")
            program_determiner = 0
    elif program_determiner == 2:
        icao = input("Anna lentokentän ICAO koodi: ")
        search = search_airport(icao)
        if search:
            print(f"Lentokenttä {icao.upper()} löytyi: {search}")
            program_determiner = 0
        else:
            print("Lentokenttää ei löytynyt")
    elif program_determiner == 3:
        allow_airport_program = False
        print("Ohjelma lopetettu")
    else:
        print("Anna numero 1-3 välillä!")
        
