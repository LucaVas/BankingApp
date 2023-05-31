import customtkinter as ctk # type: ignore
import sys
sys.path.append("src")
from bank import Bank # type: ignore
import logging

# setting up logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler("./gui_logs/bank_info_frame.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class BankInfoFrame(ctk.CTkFrame):
    """A custom Tkinter frame for displaying bank information.

    This frame is used to display various information about the bank, such as shares amount,
    share price, and shares price delta.

    Args:
        parent (tkinter.Widget): The parent widget to which this frame belongs.
        bank (Bank): The bank object containing the bank information.
    """
    def __init__(self, parent, bank: Bank):
        logger.info("Bank info frame created successfully.")
        """Initialize the current frame.

        Args:
            parent (tkinter.Widget): The parent widget to which this frame belongs.
            bank (Bank): The bank object containing the bank information.

        """
        super().__init__(parent)

        self.parent_window = parent
        self.bank = bank

        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)

        self.shares_amount_label_text = "> Bank shares: "
        self.shares_amount_data_label_text = self.bank.shares_amount
        self.shares_price_label_text = "> Price per Share: "
        self.shares_price_data_label_text = self.bank.share_price
        self.shares_delta_label_text = "> Shares price delta: "
        self.shares_delta_data_label_text = f"{self.bank.shares_delta:.2f}%"

        # widgets
        self.shares_amount_label = ctk.CTkLabel(
            self,
            text=self.shares_amount_label_text,
            font=ctk.CTkFont("Tahoma", size=15, weight="bold"),
        )
        self.shares_amount_label.grid(row=0, column=0, padx=(15, 0), sticky="w")
        self.shares_amount_data_label = ctk.CTkLabel(
            self,
            text=self.shares_amount_data_label_text,
            font=ctk.CTkFont("Tahoma", size=15, weight="normal"),
        )
        self.shares_amount_data_label.grid(row=0, column=1, columnspan=2, sticky="nsew")

        self.shares_price_label = ctk.CTkLabel(
            self,
            text=self.shares_price_label_text,
            font=ctk.CTkFont("Tahoma", size=15, weight="bold"),
        )
        self.shares_price_label.grid(row=1, column=0, padx=(15, 0), sticky="w")
        self.shares_price_data_label = ctk.CTkLabel(
            self,
            text=self.shares_price_data_label_text,
            font=ctk.CTkFont("Tahoma", size=15, weight="normal"),
        )
        self.shares_price_data_label.grid(row=1, column=1, columnspan=2, sticky="nsew")

        self.shares_delta_label = ctk.CTkLabel(
            self,
            text=self.shares_delta_label_text,
            font=ctk.CTkFont("Tahoma", size=15, weight="bold"),
        )
        self.shares_delta_label.grid(row=2, column=0, padx=(15, 0), sticky="w")
        self.shares_delta_data_label = ctk.CTkLabel(
            self,
            text=self.shares_delta_data_label_text,
            font=ctk.CTkFont("Tahoma", size=15, weight="normal"),
        )
        self.shares_delta_data_label.grid(row=2, column=1, columnspan=2, sticky="nsew")
