from datetime import datetime
from tokenize import Double

from restaurant_app.enums import PaymentStatus
from restaurant_app.models import Invoice, CreditCardTransaction, CheckTransaction, CashTransaction


def create_invoice(room_price, days):
    print("""    1. Credit card
        2. Check
        3. Cash
            """)

    option = input("Enter payment method number: ")

    if option not in (1,4):
        print("Invalid method number")
        return False

    if option == 1:
        noc = input("Enter name on card: ")
        zip_code = input("Enter zip code: ")
        return Invoice(room_price * days, CreditCardTransaction(datetime.now(), PaymentStatus.PENDING, noc, zip_code))

    if option == 2:
        bank_name = input("Enter bank name: ")
        check_number = input("Enter check number: ")
        return Invoice(room_price * days, CheckTransaction(datetime.now(), PaymentStatus.PENDING, bank_name, check_number))

    if option == 3:
        cash_tendered = float(input("Enter cash tendered: "))
        return Invoice(room_price * days, CashTransaction(datetime.now(), PaymentStatus.PENDING, cash_tendered))

    return False