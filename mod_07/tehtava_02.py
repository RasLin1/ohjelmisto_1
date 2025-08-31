names = set()
allow_name_asker = True

def name_checker(name):
    for x in names:
        if x == name:
            return True
    return False


while allow_name_asker == True:
    temp_name_holder = input("Anna nimi: ")
    name_exists = name_checker(temp_name_holder)
    if temp_name_holder == "":
        for x in names:
            print(x)
        allow_name_asker = False
    elif name_exists == False:
        print("Uusi nimi")
        names.add(temp_name_holder)
    elif name_exists == True:
        print("Aiemmin syötetty nimi")
        names.add(temp_name_holder)
