from bank import Bank
from holder import Holder
from account import Account
from currency import Currency
from gui.holder_registration import HolderRegistrationWindow
from gui.password_registration import PasswordRegistrationWindow


def main() -> None:

    # Holder registration
    name, surname, birth_date = holder_registration()
    new_holder = Holder(name, surname, birth_date)

    # Password registration
    password = password_registration()
    new_holder.password = password

    # TODO: MainWindow

    print(repr(new_holder))


def holder_registration():
    registration = HolderRegistrationWindow()
    registration.start()
    return registration.holder_name, registration.holder_surname, registration.holder_birth_date

def password_registration():
    pass_registration = PasswordRegistrationWindow()
    pass_registration.start()
    return pass_registration.password
    

if __name__ == "__main__":
    main()