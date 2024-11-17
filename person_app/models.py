import random
from logging import fatal


class Person:
    def __init__(self, name, address, email, phone, account_type):
        self._id = random.randint(1, 100)
        self._name = name
        self._address = address
        self._email = email
        self._phone = phone
        self._account_type = account_type

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_address(self):
        return self._address
    def set_address(self, address):
        self._address = address

    def get_email(self):
        return self._email
    def set_email(self, email):
        self._email = email

    def get_phone(self):
        return self._name
    def set_phone(self, phone):
        self._phone = phone

    def get_account_type(self):
        return self._name
    def set_account_type(self, account_type):
        self._account_type = account_type

    def __str__(self):
        return f"{self._name}, {self._phone}, {self._account_type}"

class Account(Person):
    def __init__(self, name, address, email, phone, account_type, password, account_status):
        super().__init__(name, address, email, phone, account_type)
        self._id = random.randint(1, 100)
        self.__password = password
        self.__account_status = account_status

    def get_password(self):
        return self.__password


    def get_account_status(self):
        return self.__account_status
    def set_account_status(self, account_status):
        self.__account_status = account_status

    def reset_password(self, password):
        if isinstance(password, str):
            self.__account_status = password
            return True
        else:
            print("Entered password is not valid!")
            return False

class Receptionist():
    pass





class Address:
    def __init__(self, city_name, street_name):
        self.__city_name = city_name
        self.__street_name = street_name

    def get_city_name(self):
        return self.__city_name
    def set_city_name(self, city_name):
        self.__city_name = city_name

    def get_street_name(self):
        return self.__street_name
    def set_street_name(self, street_name):
        self.__street_name = street_name

    def __str__(self):
        return f"{self.__city_name}, {self.__street_name}"























