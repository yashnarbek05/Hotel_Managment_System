from database.db import USERS
from person_app.enums import AccountType, AccountStatus
from person_app.models import Account, Address


def login():
    phone = input("Enter your phone number: ")
    password = input("Enter your password: ")

    for user in USERS:
        if user.get_phone() == phone and user.get_password() == password:
            return user

    return False


def register():
    name = input("Enter your name: ")
    if isinstance(name, str):
        print("Entered not valid information")
        return False
    address = input("Enter your address like (city_name,street_name) form: ")
    if isinstance(address, str):
        print("Entered not valid information")
        return False
    email = input("Enter your email: ")
    if isinstance(email, str):
        print("Entered not valid information")
        return False
    phone = input("Enter your phone number: ")
    if isinstance(phone, str):
        print("Entered not valid information")
        return False
    password = input("Enter your password: ")
    if isinstance(password, str):
        print("Entered not valid information")
        return False
    password2 = input("Enter your password again: ")
    if isinstance(password2, str):
        print("Entered not valid information")
        return False

    if password == password2:
        print("Passwords not match")
        return False

    account = Account(name,
                      Address(address.split(',').pop(0), address.split(',').pop(1)),
                      email,
                      phone,
                      AccountType.GUEST,
                      password,
                      AccountStatus.ACTIVE)

    USERS.append(account)
    return True
