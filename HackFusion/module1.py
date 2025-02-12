# Sulphitesimal
# Member: Aqiba Abdul Qadir

import time


user_dct = {}   # This is made global because there is no database


def login_options(user):
    while True:
        print("Home Page\n\n")
        opt2 = input("Press the digit accordingly:\n1. Modify fields\n2. Exit to Menu\n")

        if opt2 == '1':
            print('\nChoose an option!')
            opt3 = input('1. Modify username\n2. Modify Password\n3. Modify email\n4.Exit to Home Page\n')

            if opt3 == '1':
                while True:
                    new = input('Enter new username: ')
                    if new not in user_dct:
                        details = user_dct[user]
                        del user_dct[user]
                        user_dct[new] = details
                        print("Username successfully changed! Redirecting to Home page.\n")
                        time.sleep(2)
                        break
                    else:
                        print("Username already taken. Try a new username!")

            elif opt3 == '2':
                new = input('Enter new password: ')
                user_dct[user]['password'] = new
                print("Password successfully changed! Redirecting to Home page.\n")
                time.sleep(2)

            elif opt3 == '3':
                new = input('Enter new email: ')
                user_dct[user]['email'] = new
                print("Email successfully changed! Redirecting to Home page.\n")
                time.sleep(2)

        else:
            break
    print('\n\n\n')


def sign_up():
    user = ''
    while not user or user in user_dct:
        user = input("Enter username: ")
        if user in user_dct:
            print("Username already taken! Try a different username.\n")
        else:
            break
    print()
    pas = ''

    while not pas:
        pas = input("Enter password: ")
        if not pas:
            print("Field shouldn't be empty!")
        else:
            break

    print()
    email = ''
    while not email:
        email = input("Enter email: ")
        if not email:
            print("Field shouldn't be empty!")
        else:
            break

    user_dct[user] = {'password': pas, 'email': email}

    print("You have been signed up successfully! Please login to continue.\n")
    time.sleep(1)
    print('\n\n\n')


def log_in():
    user = ''
    while not user or user not in user_dct:
        user = input('Enter username: ')
        if user in user_dct:
            curr = user_dct[user]['password']
            pas = ''
            while pas != curr:
                pas = input("Enter password: ")
                if pas != curr:
                    print("Incorrect password! Try again.\n")
                else:
                    break
            print("Login Successful!\n")
            time.sleep(2)
            print('\n\n\n')
            login_options(user)
            break

        else:
            print('Incorrect username!\n')
    print('\n\n\n')


while True:
    print("Menu\n")
    opt = input("Press the digit accordingly:\n1. Sign up\n2. Log in\n")
    print()
    if opt == '1':
        sign_up()

    elif opt == '2':
        log_in()

