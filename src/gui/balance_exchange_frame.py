import customtkinter as ctk


class BalanceExchangeFrame(ctk.CTkFrame):
    """A custom Tkinter frame for displaying exchanged balance information.

    This frame is used to display the exchanged balance amount and currency label.

    Args:
        parent (tkinter.Widget): The parent widget to which this frame belongs.
        exchange_frame (tkinter.Widget): The exchange frame to which this balance frame belongs.
    """
    def __init__(self, parent, exchange_frame):
        """Initialize the current frame.

        Args:
            parent (tkinter.Widget): The parent widget to which this frame belongs.
            exchange_frame (tkinter.Widget): The exchange frame to which this balance frame belongs.

        """
        super().__init__(parent)

        self.parent_window = parent
        self.exchange_frame = exchange_frame

        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((0), weight=1)

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
