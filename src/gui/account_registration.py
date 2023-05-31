from tkinter import messagebox
import customtkinter as ctk # type: ignore
import re
import sys
sys.path.append("src")
from bank import Bank # type: ignore
import logging

# setting up logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler("./gui_logs/account_registration.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class AccountRegistrationWindow(ctk.CTk):
    """
    A class representing the window for registering a new account in the bank.

    Methods:
    - __init__(self, list_of_currencies: list[str], bank): Initialize the current window.
    - validate_input(self): Validate the user input.
    - register_account(self, amount: float, connected_account: str): Register the account.
    - show_error(self, error: str): Show an error message.
    - start(self): Start the main loop of the window.
    - on_closing(self): Handle the closing event of the window.
    - close(self): Close the window.
    """

    def __init__(self, list_of_currencies: list[str], bank: Bank):
        super().__init__()

        logger.info("New Account registration window object created")

        self.currency_list = list_of_currencies

        # geometry & positioning
        self.width = 800
        self.height = 400
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")
        # self.attributes("-topmost", True)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # grid layout
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # holder information
        self.title(bank.name)
        self.balance = 0.0
        self.currency = ""
        self.interest_rate = ""
        self.connected_account = ""

        # widgets variables
        self.account_registration_label_text = "Account registration"
        self.interest_rate_label_text = "> Select the interest rate:"
        self.interest_rate_optionmenu_options = ["1.8", "2.0", "2.5"]
        self.interest_rate_optionmenu_var = ctk.StringVar(
            value=self.interest_rate_optionmenu_options[0]
        )
        self.currency_label_text = "> Select the account currency:"
        self.currency_optionmenu_options = self.currency_list
        self.currency_optionmenu_var = ctk.StringVar(
            value=self.currency_optionmenu_options[0]
        )
        self.amount_label_text = "> Enter the initial balance amount:"
        self.connected_account_label_text = "> Enter the connected account:"
        self.register_account_button_text = "Save account"

        # ============ Top frame with main label ============ #
        self.account_registration_frame = ctk.CTkFrame(self, corner_radius=0)
        self.account_registration_frame.grid(
            row=0, column=0, columnspan=4, padx=(10, 10), pady=(10, 10), sticky="nsew"
        )
        self.account_registration_frame.grid_rowconfigure(0, weight=1)
        self.password_registration_label = ctk.CTkLabel(
            self.account_registration_frame,
            text=self.account_registration_label_text,
            font=ctk.CTkFont(size=20, weight="normal"),
        )
        self.password_registration_label.grid(row=0, column=0, padx=10, pady=(10, 10))

        # ============ Main frame with entries ============ #
        self.entries_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.entries_frame.grid(
            row=1, column=0, columnspan=3, padx=(10, 10), pady=(0, 10), sticky="nsew"
        )
        self.entries_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.entries_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.interest_rate_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.interest_rate_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.interest_rate_label.grid(
            row=0, column=0, padx=10, pady=(10, 10), sticky="w"
        )
        self.interest_rate_optionmenu = ctk.CTkOptionMenu(
            self.entries_frame,
            values=self.interest_rate_optionmenu_options,
            variable=self.interest_rate_optionmenu_var,
            anchor="center"
        )
        self.interest_rate_optionmenu.grid(row=0, column=1, sticky="ew")

        self.currency_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.currency_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.currency_label.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="w")
        self.currency_optionmenu = ctk.CTkOptionMenu(
            self.entries_frame,
            values=self.currency_optionmenu_options,
            variable=self.currency_optionmenu_var,
            anchor="center"
        )
        self.currency_optionmenu.grid(row=1, column=1, sticky="ew")

        self.amount_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.amount_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.amount_label.grid(row=2, column=0, padx=10, pady=(10, 10), sticky="w")
        self.amount_entry = ctk.CTkEntry(self.entries_frame)
        self.amount_entry.grid(
            row=2, column=1, columnspan=2, sticky="ew"
        )

        self.connected_account_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.connected_account_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.connected_account_label.grid(
            row=3, column=0, padx=10, pady=(10, 10), sticky="w"
        )
        self.connected_account_entry = ctk.CTkEntry(self.entries_frame)
        self.connected_account_entry.grid(
            row=3, column=1, columnspan=2, sticky="ew"
        )

        self.message_label = ctk.CTkLabel(self, text="")
        self.message_label.grid(row=2, column=0)

        # ============ Bottom row with button ============ #
        self.register_account_button = ctk.CTkButton(
            self,
            text=self.register_account_button_text,
            state="active",
            width=40,
            height=40,
            text_color="black",
            font=("tahoma", 16),
            command=self.validate_input,
        ).grid(row=3, column=3, padx=10, pady=(10, 10), sticky="ew")

    def validate_input(self) -> None:
        """
        Validate the user input.

        Returns:
        None
        """
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            logger.exception("ValueError")
            self.show_error("Invalid amount")
            return

        if amount < 0:
            logger.error("Negative amount entered.")
            self.show_error("Invalid amount")
            return

        pattern = r"^LT\d{18}$"
        connected_account = self.connected_account_entry.get().strip()
        if re.match(pattern, connected_account):
            self.register_account(amount, connected_account)
            logger.info(f"Account number created: {connected_account}")
        else:
            logger.error(f"Invalid account number: {connected_account}")
            self.show_error("Invalid account. The account must begin with 'LT' followed by 18 digits.")
            return

    def register_account(self, amount: float, connected_account: str) -> None:
        """
        Register the account.

        Parameters:
        - amount (float): The initial balance amount.
        - connected_account (str): The connected account.

        Returns:
        None
        """
        self.interest_rate = self.interest_rate_optionmenu_var.get()
        self.currency = self.currency_optionmenu_var.get()
        self.balance = amount
        self.connected_account = connected_account

        self.close()

    def show_error(self, error: str) -> None:
        """
        Show an error message.

        Parameters:
        - error (str): The error message to display.

        Returns:
        None
        """
        # parent=self keeps the popup window in front
        messagebox.showerror("Error", error, parent=self)

    def start(self):
        """
        Start the main loop of the window.

        Returns:
        None
        """
        self.mainloop()

    def on_closing(self):
        """
        Handle the closing event of the window.

        Returns:
        None
        """
        if messagebox.askokcancel(
            "Quit",
            "Do you want to quit?\nIf you quit now, the registration process will be stopped.",
            parent=self,
        ):
            logger.warning("User closed the window unexpectedly.")
            self.destroy()
            sys.exit()

    def close(self):
        """
        Close the window.

        Returns:
        None
        """
        logger.info("Account registration window closed.")
        self.destroy()
