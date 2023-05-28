import customtkinter as ctk # type: ignore
import sys
sys.path.append("src")
from holder import Holder # type: ignore
from account import Account # type: ignore
import logging

# setting up logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler("./gui_logs/holder_info_frame.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class HolderInfoFrame(ctk.CTkFrame):
    """A custom Tkinter frame for displaying holder information.

    This frame is used to display various information about the account holder, such as their name,
    the currency associated with the account, and the interest rate.

    Args:
        parent (tkinter.Widget): The parent widget to which this frame belongs.
        holder (Holder): The holder object containing the holder information.
        account (Account): The account object associated with the holder.
    """
    def __init__(self, parent, holder: Holder, account: Account):
        logger.info("New holder info frame created.")
        """Initialize the current frame.

        Args:
            parent (tkinter.Widget): The parent widget to which this frame belongs.
            holder (Holder): The holder object containing the holder information.
            account (Account): The account object associated with the holder.

        """
        super().__init__(parent)

        self.parent_window = parent
        self.holder = holder
        self.account = account

        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)

        self.holder_name_label_text = "> Holder: "
        self.holder_name_data_label_text = (
            f"{self.holder.first_name} {self.holder.last_name}"
        )
        self.info_currency_label_text = "> Currency: "
        self.info_currency_data_label_text = self.account.currency
        self.info_interest_rate_label_text = "> Interest: "
        self.info_interest_rate_data_label_text = f"{self.account.interest_rate}%"

        # widgets
        self.holder_name_label = ctk.CTkLabel(
            self,
            text=self.holder_name_label_text,
            font=ctk.CTkFont("Tahoma", size=15, weight="bold"),
        )
        self.holder_name_label.grid(row=0, column=0, padx=(15, 0), sticky="w")
        self.holder_name_data_label = ctk.CTkLabel(
            self,
            text=self.holder_name_data_label_text,
            font=ctk.CTkFont("Tahoma", size=15, weight="normal"),
        )
        self.holder_name_data_label.grid(row=0, column=1, columnspan=2, sticky="ew")

        self.info_currency_label = ctk.CTkLabel(
            self,
            text=self.info_currency_label_text,
            font=ctk.CTkFont("Tahoma", size=15, weight="bold"),
        )
        self.info_currency_label.grid(row=1, column=0, padx=(15, 0), sticky="w")
        self.info_currency_data_label = ctk.CTkLabel(
            self,
            text=self.info_currency_data_label_text,
            font=ctk.CTkFont("Tahoma", size=15, weight="normal"),
        )
        self.info_currency_data_label.grid(row=1, column=1, columnspan=2, sticky="ew")

        self.info_interest_rate_label = ctk.CTkLabel(
            self,
            text=self.info_interest_rate_label_text,
            font=ctk.CTkFont("Tahoma", size=15, weight="bold"),
        )
        self.info_interest_rate_label.grid(row=2, column=0, padx=(15, 0), sticky="w")
        self.info_interest_rate_data_label = ctk.CTkLabel(
            self,
            text=self.info_interest_rate_data_label_text,
            font=ctk.CTkFont("Tahoma", size=15, weight="normal"),
        )
        self.info_interest_rate_data_label.grid(
            row=2, column=1, columnspan=2, sticky="ew"
        )
