from datetime import datetime

from database.db import ROOM_WITH_BOOKS
from restaurant_app.enums import PaymentStatus
from restaurant_app.models import Invoice, CreditCardTransaction, CheckTransaction, CashTransaction


def create_invoice(room_id, days):
    room_price = 0
    for room in ROOM_WITH_BOOKS:
        if room.room_id == room_id:
            room_price = room.get_booking_price()

    if room_price == 0:
        print("Room id not available!")
        return False

    print("""    1. Credit card
        2. Check
        3. Cash
            """)

    option = input("Enter payment method number: ")

    if option not in (1, 4):
        print("Invalid method number")
        return False

    if option == 1:
        noc = input("Enter name on card: ")
        zip_code = input("Enter zip code: ")
        return Invoice(room_price * days, CreditCardTransaction(datetime.now(), PaymentStatus.PENDING, noc, zip_code))

    if option == 2:
        bank_name = input("Enter bank name: ")
        check_number = input("Enter check number: ")
        return Invoice(room_price * days,
                       CheckTransaction(datetime.now(), PaymentStatus.PENDING, bank_name, check_number))

    if option == 3:
        cash_tendered = float(input("Enter cash tendered: "))
        return Invoice(room_price * days, CashTransaction(datetime.now(), PaymentStatus.PENDING, cash_tendered))

    return False
