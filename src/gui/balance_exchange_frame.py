import customtkinter as ctk # type: ignore
from gui.exchange_frame import ExchangeFrame  # type: ignore
import logging

# setting up logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler("./gui_logs/balance_exchange_frame.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class BalanceExchangeFrame(ctk.CTkFrame):
    """A custom Tkinter frame for displaying exchanged balance information.

    This frame is used to display the exchanged balance amount and currency label.

    Args:
        parent (tkinter.Widget): The parent widget to which this frame belongs.
        exchange_frame (tkinter.Widget): The exchange frame to which this balance frame belongs.
    """
    def __init__(self, parent, exchange_frame: ExchangeFrame):
        logger.info("Balance exchange frame object created.")
        """Initialize the current frame.

        Args:
            parent (tkinter.Widget): The parent widget to which this frame belongs.
            exchange_frame (tkinter.Widget): The exchange frame to which this balance frame belongs.

        """
        super().__init__(parent)

        self.parent_window = parent
        self.exchange_frame = exchange_frame
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.exchange_labance_label_text = "> Exchanged to"
        self.exchange_balance_amount_label_text = "          "
        self.exchange_currency_label_text = "   "

        # widgets
        self.exchange_labance_label = ctk.CTkLabel(
            self,
            text=self.exchange_labance_label_text,
            font=ctk.CTkFont("Tahoma", size=18, weight="normal"),
        )
        self.exchange_labance_label.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.exchange_balance_amount_label = ctk.CTkLabel(
            self,
            text=self.exchange_balance_amount_label_text,
            font=ctk.CTkFont("Tahoma", size=18, weight="normal"),
        )
        self.exchange_balance_amount_label.grid(row=0, column=2, sticky="ew")

        self.exchange_currency_label = ctk.CTkLabel(
            self,
            text=self.exchange_currency_label_text,
            font=ctk.CTkFont("Tahoma", size=18, weight="normal"),
        )
        self.exchange_currency_label.grid(row=0, column=3, sticky="ew")
