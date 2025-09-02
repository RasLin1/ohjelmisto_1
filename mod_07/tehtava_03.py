airports = {}

allow_airport = True

def insert_airport(icao, name):
    aiport_exists = False
    for x in airports:
        if x == icao:
            aiport_exists = True