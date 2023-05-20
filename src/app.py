from bank import Bank
from holder import Holder
from account import Account
from gui_registration import RegistrationGui, WelcomeWindow
from gui_account import AccountInformation
from gui_main import MainWindow


def main():


    registration()

    holder_info = RegistrationGui.holder_info
    password_info = RegistrationGui.password
    new_holder = Holder(holder_info[0],holder_info[1],holder_info[2],password_info[0])

    account_setup()

    account_info = AccountInformation.account_info
    new_account = Account(new_holder.id, account_info[0], account_info[1], account_info[2])

    run_main_window(new_holder, new_account)

def run_main_window(holder: Holder, account: Account) -> None:
    app = MainWindow(holder, account)
    app.mainloop()

def registration():
    app = WelcomeWindow()
    app.mainloop()

def account_setup():
    app = AccountInformation()
    app.mainloop()


if __name__ == "__main__":
    main()