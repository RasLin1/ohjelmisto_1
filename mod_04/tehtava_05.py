username = "test"
password = "test"
login_tries = 0
login_success = False

while login_tries <= 4 and not login_success:
    input_username = input("Anna kayttäjätunnus: ")
    input_password = input("Anna salasana: ")
    if input_username == username and input_password == password:
        print("Tervetuloa")
        login_success = True
    else:
        print(f"Pääsy kieletty")
        login_tries = login_tries + 1

if login_tries == 4:
    print("Pääsy täysin kieletty")