from person_app.enums import AccountType
from person_app.models import Person, Address

if __name__ == '__main__':
    p = Person("Tony",
               Address("Toshkent",
                       "Olmazor"),
               "user@gmail.com",
               "+998931234567",
               AccountType.MEMBER)

    print(p)