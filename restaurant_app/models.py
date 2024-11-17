
class Room:
    def __init__(self, style, status, booking_price, is_smoking):
        self.__style = style
        self.__status = status
        self.__booking_price = booking_price
        self.__is_smoking = is_smoking

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
