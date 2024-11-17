import random


class Room:
    def __init__(self, style, status, booking_price, is_smoking, room_key):
        self.__style = style
        self.__status = status
        self.__booking_price = booking_price
        self.__is_smoking = is_smoking
        self.room_key = room_key


    def get_style(self):
        return self.__style

    def set_style(self, style):
        self.__style = style

    def get_booking_price(self):
        return self.__booking_price

    def set_booking_price(self, booking_price):
        self.__booking_price = booking_price

    def get_is_smoking(self):
        return self.__is_smoking

    def set_is_smoking(self, is_smoking):
        self.__is_smoking = is_smoking

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

class RoomKey:
    def __init__(self, barcode, issued_at, is_active, is_master):
        self.key_id = random.randint(0,100)
        self.barcode = barcode
        self.issued_at = issued_at
        self.is_active = is_active
        self.is_master = is_master

    def __str__(self):
        return f"{self.key_id}, {self.barcode}"

class RoomBooking:
    def __init__(self, reservation_number, start_date, duration_in_days, status, check_in, check_out, room_id, invoice):
        self.reservation_number = reservation_number
        self.start_date = start_date
        self.duration_in_days = duration_in_days
        self.status = status
        self.check_in = check_in
        self.check_out = check_out
        self.room_id = room_id
        self.invoice = invoice

    def __str__(self):
        return f"{self.reservation_number}, {self.status}, room_id: {self.room_id}"

class Invoice:
    def __init__(self, amount, bill):
        self.amount = amount
        self.bill = bill

    def __str__(self):
        return f"Your pay amount: {self.amount}, bill: {self.bill}"

class Bill:
    def __init__(self, creation_date, status):
        self.creation_date = creation_date
        self.status = status

class CreditCardTransaction(Bill):
    def __init__(self, creation_date, status, name_on_card, zip_code):
        super().__init__(creation_date, status)
        self.name_on_card = name_on_card
        self.zip_code = zip_code

    def __str__(self):
        return f"{self.creation_date}, {self.status}, card name: {self.name_on_card}"

class CheckTransaction(Bill):
    def __init__(self, creation_date, status, bank_name, check_number):
        super().__init__(creation_date, status)
        self.bank_name = bank_name
        self.check_number = check_number

    def __str__(self):
        return f"{self.creation_date}, {self.status}, bank name: {self.bank_name}, check: {self.check_number}"

class CashTransaction(Bill):
    def __init__(self, creation_date, status, cash_tendered):
        super().__init__(creation_date, status)
        self.cash_tendered = cash_tendered

    def __str__(self):
        return f"{self.creation_date}, {self.status}, cash: {self.cash_tendered}"