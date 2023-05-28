import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Set the working directory to the parent directory of 'src'

from bank import Bank # type: ignore
from holder import Holder # type: ignore
from account import Account # type: ignore
from currency import Currency # type: ignore
from api_fetcher import ApiFetcher # type: ignore
from gui.welcome_window import WelcomeWindow # type: ignore
from gui.login_window import LoginWindow # type: ignore
from gui.holder_registration import HolderRegistrationWindow # type: ignore
from gui.password_registration import PasswordRegistrationWindow # type: ignore
from gui.account_registration import AccountRegistrationWindow # type: ignore
from gui.main_window import MainWindow # type: ignore
from decouple import config # type: ignore
import customtkinter as ctk # type: ignore
from reader import Reader # type: ignore
from writer import Writer # type: ignore
from config import db_name, market_price_url, market_company_info_url, exchange_url # type: ignore

import logging

# setting level of logging
log_file = "unified.log"
logging.basicConfig(level=logging.DEBUG, filename=log_file, filemode="w",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# setting up logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler("./main_logs/main.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

MARKET_KEY = config("MARKET_KEY")
API_KEY = config("EXCHANGE_KEY")


def main() -> None:
    """Main function to start the banking application."""

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
        holder, account = start_login_process(bank, writer, temp_db)
    else:
        raise Exception("Process not found")

    # Get exchange rates
    exchange_rates = get_exchange_rates(exchange_url, API_KEY, account.currency)
    currency_obj = Currency(exchange_rates)

    # # Main window
    run_main_window(holder, account, bank, currency_obj, temp_db, writer)

    writer.write_to_file(temp_db)





def start_registration_process(bank: Bank, writer: Writer, temp_db: dict) -> tuple[Holder, Account]:
    """Starts the registration process for a new holder and account.

    Args:
        bank: The Bank instance.
        writer: The Writer instance for writing to the database.
        temp_db: The temporary database.

    Returns:
        A tuple containing the new Holder and Account instances.
    """
    # === Holder registration === #
    # new_holder = Holder("Paolo", "Marconi", datetime.strptime("19900511", "%Y%m%d").date())
    name, surname, birth_date = holder_registration(bank)
    new_holder = Holder(name, surname, birth_date)

    # === Password registration === #
    password = password_registration(bank)
    new_holder.password = password

    # # === Account registration === #
    # new_account = Account(99, 100, "1.8", "EUR")
    balance, interest_rate, currency, connected_account = account_registration(bank)
    new_account = Account(new_holder.id, balance, interest_rate, currency)
    new_holder.connected_accounts.append(connected_account)

    # === Store new user to temporary database dict === #
    writer.temp_write(new_holder, new_account, temp_db)

    return new_holder, new_account


def start_login_process(bank: Bank, writer: Writer, temp_db: dict) -> tuple[Holder, Account]:
    """Starts the login process for an existing holder.

    Args:
        bank: The Bank instance.
        writer: The Writer instance for writing to the database.
        temp_db: The temporary database.

    Returns:
        A tuple containing the existing Holder and Account instances.
    """
    login_window = LoginWindow(bank, temp_db)
    login_window.start()

    holder = Holder.load(login_window, temp_db)
    account = Account.load(holder.id, temp_db)

    # === Store new user to temporary database dict === #
    writer.temp_write(holder, account, temp_db)

    return holder, account


def load_database(db_name: str) -> dict:
    """Loads the database from the json file.

    Args:
        db_name: The name of the database file.

    Returns:
        The database dictionary.
    """
    reader = Reader(db_name)
    return reader.read_file()


def holder_registration(bank: Bank) -> tuple[str, str, str]:
    """Performs the holder registration process.

    Args:
        bank: The Bank instance.

    Returns:
        A tuple containing the name, surname, and birth date of the holder.
    """
    registration = HolderRegistrationWindow(bank)
    registration.start()
    return (
        registration.holder_name,
        registration.holder_surname,
        registration.holder_birth_date,
    )


def password_registration(bank: Bank) -> bytes:
    """Performs the password registration process.

    Args:
        bank: The Bank instance.

    Returns:
        The password as bytes.
    """
    pass_registration = PasswordRegistrationWindow(bank)
    pass_registration.start()
    return pass_registration.password


def account_registration(bank: Bank) -> tuple[float, str, str, str]:
    """Performs the account registration process.

    Args:
        bank: The Bank instance.

    Returns:
        A tuple containing the balance, interest rate, currency, and connected account of the new account.
    """
    acc_registration = AccountRegistrationWindow(Currency.list_of_currencies, bank)
    acc_registration.start()
    return (
        acc_registration.balance,
        acc_registration.interest_rate,
        acc_registration.currency,
        acc_registration.connected_account,
    )


def run_main_window(
    holder: Holder,
    account: Account,
    bank: Bank,
    currency_obj: Currency,
    temp_db: dict,
    writer: Writer,
) -> None:
    """Runs the main window of the banking application.

    Args:
        holder: The Holder instance.
        account: The Account instance.
        bank: The Bank instance.
        currency_obj: The Currency instance.
        temp_db: The temporary database.
        writer: The Writer instance for writing to the database.
    """
    app = MainWindow(holder, account, bank, currency_obj, temp_db, writer)
    app.mainloop()

    # === Store new user to temporary database dict === #
    writer.temp_write(holder, account, temp_db)


def get_exchange_rates(url: str, key: str, base_currency: str) -> dict:
    """Fetches the exchange rates from an API.

    Args:
        url: The URL of the API.
        key: The API key.
        base_currency: The base currency.

    Returns:
        A dictionary containing the exchange rates.
    """
    data = fetch_api(url, key, base_currency)

    logger.info("Exchange data fetched from API succesfully.")
    return data["data"]


def get_market_data(url: str, key: str) -> dict:
    """Fetches market data from an API.

    Args:
        url: The URL of the API.
        key: The API key.

    Returns:
        A dictionary containing the market data.
    """
    data = fetch_api(url, key)
    logger.info("Market data fetched from API succesfully.")
    return data


def fetch_api(url: str, key: str, base_currency: str = "") -> dict:
    """Fetches data from an API.

    Args:
        url: The URL of the API.
        key: The API key.
        base_currency: The base currency.

    Returns:
        The fetched data.
    """
    api_fetcher = ApiFetcher(url, key, base_currency)
    return api_fetcher.fetch()


if __name__ == "__main__":
    main()
