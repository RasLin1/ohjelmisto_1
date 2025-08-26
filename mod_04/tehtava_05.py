username = "test"
password = "test"
login_tries = 0

while login_tries <= 4:
    input_username = input("Anna kayttäjätunnus: ")
    input_password = input("Anna salasana: ")
    if input_username == username and input_password == password:
        print("Tervetuloa")
        break
    else:
        print("Pääsy kieletty")
        login_tries = login_tries + 1