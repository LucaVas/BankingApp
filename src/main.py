from bank import Bank
from holder import Holder
from account import Account
from currency import Currency
from gui.holder_registration import HolderRegistrationWindow
from gui.password_registration import PasswordRegistrationWindow
from gui.account_registration import AccountRegistrationWindow
from gui.main_window import MainWindow
from datetime import datetime
from api_fetcher import ApiFetcher


def main() -> None:

    bank = Bank()

    # # Holder registration
    # name, surname, birth_date = holder_registration()
    # new_holder = Holder(name, surname, birth_date)

    # # Password registration
    # password = password_registration()
    # new_holder.password = password

    # # Account registration
    # balance, interest_rate, currency = account_registration()
    # new_account = Account(new_holder.id, balance, interest_rate, currency)

    # Main window
    test_holder = Holder("Luca", "Vassos", datetime.strptime("19940514", "%Y%m%d").date())
    test_account = Account(99, 150, 1.8, "EUR")
    run_main_window(test_holder, test_account, bank)

    # run_main_window(new_holder, new_account, bank)




def holder_registration():
    registration = HolderRegistrationWindow()
    registration.start()
    return registration.holder_name, registration.holder_surname, registration.holder_birth_date

def password_registration():
    pass_registration = PasswordRegistrationWindow()
    pass_registration.start()
    return pass_registration.password

def account_registration():
    acc_registration = AccountRegistrationWindow()
    acc_registration.start()
    return acc_registration.balance, acc_registration.interest_rate, acc_registration.currency

def run_main_window(holder: Holder, account: Account, bank: Bank) -> None:
    app = MainWindow(holder, account, bank)
    app.mainloop()


    

if __name__ == "__main__":
    main()