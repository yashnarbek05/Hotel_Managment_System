from datetime import datetime

from database.db import USERS, ROOM_WITH_BOOKS
from person_app.enums import AccountType, AccountStatus
from person_app.models import Account, Address
from restaurant_app.enums import BookingStatus
from restaurant_app.models import RoomBooking
from restaurant_app.services import create_invoice


def login():
    phone = input("Enter your phone number: ")
    password = input("Enter your password: ")

    for user in USERS:
        if user.get_phone() == phone and user.get_password() == password:
            return user

    return False

def register():
    name = input("Enter your name: ")

    address = input("Enter your address like (city_name,street_name) form: ")

    email = input("Enter your email: ")

    phone = input("Enter your phone number: ")

    password = input("Enter your password: ")

    password2 = input("Enter your password again: ")


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
    return account

def book_room(account):
    if account.get_account_type() != AccountType.GUEST or account.get_account_type != AccountType.RECEPTIONIST:
        return False

    reservation_number = input("Enter reservation number: ")
    start_date = datetime.strptime(input("Enter time when you visit(DD.MM.YYYY): "), "%d.%m.%Y")
    duration = input("Enter how many days you stay: ")

    print("Available rooms:", end='\n')
    for room in ROOM_WITH_BOOKS.keys():
        print(room, end="\n")
    room_id = input("Enter room id: ")

    print("You should create invoise")

    invoice = create_invoice(room_id, duration)

    if invoice:
        room_book = RoomBooking(reservation_number,
                    start_date,
                    duration,
                    BookingStatus.REQUESTED,
                    datetime.now(),
                    datetime.now(),
                    room_id,
                    invoice
                    )
        enter_room_book_to_db(room_id, room_book)
        return True

    print("Invalid invoise!!!")
    return False

def enter_room_book_to_db(room_id, room_book):
    room = ''
    for roomm in ROOM_WITH_BOOKS:
        if roomm.room_id == room_id:
            room = roomm
            ROOM_WITH_BOOKS.get(room).append(room_book)
            return True
    return False