import customtkinter as ctk # type: ignore
import sys
sys.path.append("src")
from bank import Bank # type: ignore


class WelcomeWindow(ctk.CTk):
    def __init__(self, bank: Bank):
        """
        Represents a welcome window for the banking application.

        Args:
        bank: An instance of the Bank class representing the bank.
        """
        super().__init__()

        self.bank = bank

        # geometry & positioning
        self.width = 800
        self.height = 400
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")
        self.attributes("-topmost", True)

        # grid layout
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # holder information
        self.title(self.bank.name)
        self.choice: int

        # widgets variables
        self.welcome_label_text = f"Welcome to {self.bank.name}"
        self.open_account_label_text = "> Open an account"
        self.add_money_label_text = "> Add money"
        self.make_transfers_label_text = "> Make transfers"
        self.currency_exchange_label_text = "> Currency exchange"
        self.register_button_text = "Register"
        self.login_button_text = "Log in"

        # widgets
        # ============ Top frame with main label ============ #
        self.welcome_frame = ctk.CTkFrame(self, corner_radius=2)
        self.welcome_frame.grid(
            row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew"
        )
        self.welcome_frame.grid_rowconfigure(0, weight=1)
        self.welcome_label = ctk.CTkLabel(
            self.welcome_frame,
            text=self.welcome_label_text,
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.welcome_label.grid(row=0, column=0, padx=10, pady=(10, 10))

        # ============ Main frame with entries ============ #
        self.entries_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.entries_frame.grid(
            row=1, column=0, rowspan=2, padx=(10, 10), pady=(0, 10), sticky="nsew"
        )
        self.entries_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.entries_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.open_account_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.open_account_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.open_account_label.grid(
            row=0, column=1, padx=10, pady=(10, 10), sticky="w"
        )

        self.add_money_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.add_money_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.add_money_label.grid(row=1, column=1, padx=10, pady=(10, 10), sticky="w")

        self.make_transfers_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.make_transfers_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.make_transfers_label.grid(
            row=2, column=1, padx=10, pady=(10, 10), sticky="w"
        )

        self.currency_exchange_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.currency_exchange_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.currency_exchange_label.grid(
            row=3, column=1, padx=10, pady=(10, 10), sticky="w"
        )

        # ============ Right column with button ============ #
        self.register_button = ctk.CTkButton(
            self,
            text=self.register_button_text,
            state="active",
            width=100,
            height=40,
            text_color="black",
            font=("tahoma", 16),
            command=self.register,
        ).grid(row=1, column=1, padx=10, pady=(10, 10))
        self.login_button = ctk.CTkButton(
            self,
            text=self.login_button_text,
            state="active",
            width=100,
            height=40,
            text_color="black",
            font=("tahoma", 16),
            command=self.login,
        ).grid(row=2, column=1, padx=10, pady=(10, 10))

    def register(self) -> None:
        """
        Sets the choice attribute to 1 and closes the window.
        Choice 1 starts the registration process in main.py.
        """
        self.choice = 1
        self.close()

    def login(self) -> None:
        """
        Sets the choice attribute to 2 and closes the window.
        Choice 2 starts the login process in main.py.
        """
        self.choice = 2
        self.close()

    def start(self):
        """
        Starts the main event loop for the window.
        """
        self.mainloop()

    def close(self):
        """
        Closes the window.
        """
        self.destroy()
