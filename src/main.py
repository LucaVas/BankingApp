from bank import Bank
from holder import Holder
from account import Account
from currency import Currency
from api_fetcher import ApiFetcher
from gui.welcome_window import WelcomeWindow
from gui.holder_registration import HolderRegistrationWindow
from gui.password_registration import PasswordRegistrationWindow
from gui.account_registration import AccountRegistrationWindow
from gui.main_window import MainWindow
from datetime import datetime
from decouple import config
import customtkinter as ctk
from reader import Reader
from writer import Writer
from config import db_name, market_price_url, market_company_info_url, exchange_url, base_currency

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

MARKET_KEY = config('MARKET_KEY')
API_KEY = config('EXCHANGE_KEY')



def main() -> None:
    
    market_data = get_market_data(market_price_url, MARKET_KEY)
    company_info = get_market_data(market_company_info_url, MARKET_KEY)
    bank = Bank(market_data, company_info)

    # load the database
    temp_db = load_database(db_name)

    # instantiate the writer
    writer = Writer(db_name)

    # === Welcome user === #
    welcome_window = WelcomeWindow(bank)
    welcome_window.start()


    if welcome_window.choice == 1:
        holder, account = start_registration_process(bank, writer, temp_db)
    elif welcome_window.choice == 2:
        start_login_process(bank)
    else:
        raise Exception("Process not found")

        
    # Get exchange rates
    exchange_rates = get_exchange_rates(exchange_url, API_KEY, account.currency)
    currency_obj = Currency(exchange_rates)
    
    # # Main window
    run_main_window(holder, account, bank, currency_obj)


    # writer.write_to_file(temp_db)


def start_registration_process(bank, writer, temp_db):
    # === Holder registration === #
    # new_holder = Holder("Paolo", "Marconi", datetime.strptime("19900511", "%Y%m%d").date())
    name, surname, birth_date = holder_registration(bank)
    new_holder = Holder(name, surname, birth_date)

    # === Password registration === #
    password = password_registration(bank)
    new_holder.password = password

    # # === Account registration === #
    # new_account = Account(99, 100, "1.8", "EUR")
    balance, interest_rate, currency = account_registration(bank)
    new_account = Account(new_holder.id, balance, interest_rate, currency)

    # === Store new user to temporary database dict === #
    writer.temp_write(new_holder, new_account, temp_db)

    return new_holder, new_account


def start_login_process(bank):
    print("login")

def load_database(db_name):
    reader = Reader(db_name)
    return reader.read_file()

def holder_registration(bank: Bank):
    registration = HolderRegistrationWindow(bank)
    registration.start()
    return registration.holder_name, registration.holder_surname, registration.holder_birth_date

def password_registration(bank: Bank):
    pass_registration = PasswordRegistrationWindow(bank)
    pass_registration.start()
    return pass_registration.password

def account_registration(bank: Bank) -> tuple[float, str, str]:
    acc_registration = AccountRegistrationWindow(Currency.list_of_currencies, bank)
    acc_registration.start()
    return acc_registration.balance, acc_registration.interest_rate, acc_registration.currency

def run_main_window(holder: Holder, account: Account, bank: Bank, currency_obj: Currency) -> None:
    app = MainWindow(holder, account, bank, currency_obj)
    app.mainloop()

def get_exchange_rates(url: str, key: str, base_currency: str) -> dict:
    data = fetch_api(url, key, base_currency)
    return data["data"]

def get_market_data(url: str, key: str) -> dict:
    data = fetch_api(url, key)
    return data

def fetch_api(url: str, key: str, base_currency: str = ""):
    api_fetcher = ApiFetcher(url, key, base_currency)
    return api_fetcher.fetch()



    

if __name__ == "__main__":
    main()