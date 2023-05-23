from bank import Bank
from holder import Holder
from account import Account
from currency import Currency
from api_fetcher import ApiFetcher
from gui.holder_registration import HolderRegistrationWindow
from gui.password_registration import PasswordRegistrationWindow
from gui.account_registration import AccountRegistrationWindow
from gui.main_window import MainWindow
from datetime import datetime
from decouple import config
import customtkinter as ctk

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

market_price_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=BAC&interval=5min&apikey="
market_company_info_url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol=BAC&apikey="
MARKET_KEY = config('MARKET_KEY')

exchange_url ="https://api.freecurrencyapi.com/v1/latest?apikey="
API_KEY = config('EXCHANGE_KEY')
base_currency = "USD"



def main() -> None:

    market_data = get_market_data(market_price_url, MARKET_KEY)
    company_info = get_market_data(market_company_info_url, MARKET_KEY)
    bank = Bank(market_data, company_info)

    # # Holder registration
    # name, surname, birth_date = holder_registration(bank)
    # new_holder = Holder(name, surname, birth_date)
    new_holder = Holder("Luca", "Vassos", datetime.strptime("19940514", "%Y%m%d").date())

    # # # Password registration
    # password = password_registration(bank)
    # new_holder.password = password

    # # # Account registration
    # balance, interest_rate, currency = account_registration(bank)
    # new_account = Account(new_holder.id, balance, interest_rate, currency)
    new_account = Account(99, 100, "1.8", "EUR")
    
    
    exchange_rates = get_exchange_rates(exchange_url, API_KEY, new_account.currency)
    currency_obj = Currency(exchange_rates)
    
    # Main window
    run_main_window(new_holder, new_account, bank, currency_obj)



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