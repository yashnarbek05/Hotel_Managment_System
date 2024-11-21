from person_app.services import login, register, book_room

if __name__ == '__main__':
    user = ''
    while True:
        print("""    1. Login
                2. Register
                3. Exit
                    """)

        option = int(input("Enter option: "))

        if option == 1:
            user = login()
            if not user:
                print("Login is errored")
                continue

            print("""    1. book room
                      2. log out
                          """)
            option = input("Enter option: ")
            if option == 1:
                book_room(user)

        elif option == 2:
            user = register()
            if not user:
                print("Register is errored")
                continue

            print("""    1. book room
                   2. log out
                       """)

            option = input("Enter option: ")

            if option == 1:
                book_room(user)

        elif option == 3:
            break
        else:
            print("Invalid option!!!")
