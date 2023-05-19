from bank import Bank
from holder import Holder
from account import Account
from gui_registration import Registration, WelcomeWindow


def main():


    registration()

    holder_info = Registration.holder_info
    password_info = Registration.password
    new_holder = Holder(holder_info[0],holder_info[1],holder_info[2],password_info[0])



def registration():
    app = WelcomeWindow()
    app.mainloop()


if __name__ == "__main__":
    main()