import tkinter as tk
import customtkinter as ctk # type: ignore
import sys
sys.path.append("src")
from account import Account # type: ignore
from currency import Currency # type: ignore
import logging

# setting up logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler("./gui_logs/exchange_frame.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class ExchangeFrame(ctk.CTkFrame):
    """A custom Tkinter frame for currency exchange.

    This frame allows the user to perform currency exchange operations. It displays the exchange
    rate and the exchanged balance based on the selected currency.

    Args:
        parent (tkinter.Widget): The parent widget to which this frame belongs.
        account (Account): The account object associated with the exchange.
        currency_obj (Currency): The currency object containing currency-related information.
    """
    def __init__(self, parent, account: Account, currency_obj: Currency):
        logger.info("New exchange frame created succesfully.")
        """Initialize the current frame.

        Args:
            parent (tkinter.Widget): The parent widget to which this frame belongs.
            account (Account): The account object associated with the exchange.
            currency_obj (Currency): The currency object containing currency-related information.

        """
        super().__init__(parent)

        self.parent_window = parent
        self.account = account
        self.currency_obj = currency_obj

        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
            if i != 2:
                self.grid_rowconfigure(i, weight=1)

        self.exchange_label_text = "Currency exchange"
        self.currency_optionmenu_options = self.currency_obj.currencies
        self.currency_optionmenu_var = tk.StringVar(
            value=self.currency_optionmenu_options[0]
        )

        # widgets
        self.exchange_label = ctk.CTkLabel(self, text=self.exchange_label_text)
        self.exchange_label.grid(row=0, column=0, columnspan=2, sticky="ew")

        # Option: account from
        self.currency_optionmenu = ctk.CTkOptionMenu(
            self,
            values=self.currency_optionmenu_options,
            variable=self.currency_optionmenu_var,
            command=self.update_exchange,
            anchor="center"
        )
        # default option
        self.currency_optionmenu.grid(row=1, column=1)

    def update_exchange(self, option: str):
        """Update the exchange information based on the selected currency.

        This method is called when a new currency option is selected. It retrieves the exchange rate,
        calculates the exchanged balance, and updates the corresponding labels.

        Args:
            option (str): The selected currency option.

        """
        exchange_rate = self.get_exchange(option)
        current_balance = float(
            self.parent_window.balance_frame.balance_amount_label.cget("text")
        )
        exchanged_balance = current_balance * exchange_rate

        self.parent_window.balance_exchange_frame.exchange_balance_amount_label.configure(
            text=f"{exchanged_balance:.2f}"
        )
        self.parent_window.balance_exchange_frame.exchange_currency_label.configure(
            text=option
        )

        logger.info(f"EXchange balance lable updated with exchanged rate {exchange_rate}")

    def get_exchange(self, currency: str) -> float:
        """Get the exchange rate for the specified currency.

        This method retrieves the exchange rate from the currency object.

        Args:
            currency (str): The currency for which to retrieve the exchange rate.

        Returns:
            float: The exchange rate for the specified currency.

        """ 
        exchange = self.currency_obj.get_exchange(currency)
        logger.info(f"Exchange retrieved successfully {exchange}")
        return exchange
