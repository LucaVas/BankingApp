import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import re


class AccountRegistrationWindow(ctk.CTk):
    def __init__(self, list_of_currencies: list[str], bank):
        super().__init__()

        self.currency_list = list_of_currencies

        # geometry & positioning
        self.width = 800
        self.height = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")
        self.attributes("-topmost", True)

        # grid layout
        self.grid_columnconfigure((0, 1, 3), weight=1)
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
        self.interest_rate_optionmenu_options = [
            "1.8",
            "2.0",
            "2.5"
        ]
        self.interest_rate_optionmenu_var = ctk.StringVar(value=self.interest_rate_optionmenu_options[0])
        self.currency_label_text = "> Select the account currency:"
        self.currency_optionmenu_options = self.currency_list
        self.currency_optionmenu_var = ctk.StringVar(value=self.currency_optionmenu_options[0])
        self.amount_label_text = "> Enter the initial balance amount:"
        self.connected_account_label_text = "> Enter the connected account:"
        self.register_account_button_text = "Save account"


        # ============ Top frame with main label ============ #
        self.account_registration_frame = ctk.CTkFrame(self, corner_radius=0)
        self.account_registration_frame.grid(row=0, column=0, columnspan=4, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.account_registration_frame.grid_rowconfigure(0, weight=1)
        self.password_registration_label = ctk.CTkLabel(self.account_registration_frame, text=self.account_registration_label_text, font=ctk.CTkFont(size=20, weight="normal"))
        self.password_registration_label.grid(row=0, column=0, padx=10, pady=(10,10))


        # ============ Main frame with entries ============ #
        self.entries_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.entries_frame.grid(row=1, column=0, columnspan=3, padx=(10, 10), pady=(0, 10), sticky="nsew")
        self.entries_frame.grid_rowconfigure((0,1,2,3), weight=1)
        self.entries_frame.grid_columnconfigure((0,1,2), weight=1)

        self.interest_rate_label = ctk.CTkLabel(self.entries_frame, text=self.interest_rate_label_text, font=ctk.CTkFont(size=15, weight="normal"))
        self.interest_rate_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")
        self.interest_rate_optionmenu = ctk.CTkOptionMenu(self.entries_frame, values=self.interest_rate_optionmenu_options, variable=self.interest_rate_optionmenu_var)
        self.interest_rate_optionmenu.grid(row=0, column=1, sticky="ew")

        self.currency_label = ctk.CTkLabel(self.entries_frame, text=self.currency_label_text, font=ctk.CTkFont(size=15, weight="normal"))
        self.currency_label.grid(row=1, column=0, padx=10, pady=(10,10), sticky="w")
        self.currency_optionmenu = ctk.CTkOptionMenu(self.entries_frame, values=self.currency_optionmenu_options, variable=self.currency_optionmenu_var)
        self.currency_optionmenu.grid(row=1, column=1, sticky="ew")

        self.amount_label = ctk.CTkLabel(self.entries_frame, text=self.amount_label_text, font=ctk.CTkFont(size=15, weight="normal"))
        self.amount_label.grid(row=2, column=0, padx=10, pady=(10,10), sticky="w")
        self.amount_entry = ctk.CTkEntry(self.entries_frame)
        self.amount_entry.grid(row=2, column=1, padx=10, columnspan=2, pady=(10,10), sticky="ew")

        self.connected_account_label = ctk.CTkLabel(self.entries_frame, text=self.connected_account_label_text, font=ctk.CTkFont(size=15, weight="normal"))
        self.connected_account_label.grid(row=3, column=0, padx=10, pady=(10,10), sticky="w")
        self.connected_account_entry = ctk.CTkEntry(self.entries_frame)
        self.connected_account_entry.grid(row=3, column=1, padx=10, columnspan=2, pady=(10,10), sticky="ew")


        self.message_label = ctk.CTkLabel(self, text="")
        self.message_label.grid(row=2, column=0)

        # ============ Bottom row with button ============ #
        self.register_account_button = ctk.CTkButton(self, text=self.register_account_button_text, state="active", width=40, height=40, text_color="black", font=("tahoma", 16), command=self.validate_input).grid(row=3, column=3, padx=10, pady=(10,10), sticky="ew")


    def validate_input(self) -> None:
        try:
            amount = float(self.amount_entry.get())
        except (ValueError):
            self.show_error("Invalid amount")
            return
        
        if amount < 0:
            self.show_error("Invalid amount")
            return
        
        pattern = r'^LT\d{18}$'
        connected_account = self.connected_account_entry.get().strip()
        if re.match(pattern, connected_account):
            self.register_account(amount, connected_account)
        else:
            self.show_error("Invalid account")
            return
    
    def register_account(self, amount: float, connected_account: str) -> None:
        self.interest_rate = self.interest_rate_optionmenu_var.get()
        self.currency = self.currency_optionmenu_var.get()
        self.balance = amount
        self.connected_account = connected_account

        self.close()


    def show_error(self, error: str) -> None:
        # parent=self keeps the popup window in front
        messagebox.showerror("Error", error, parent=self)
        
    def start(self):
        self.mainloop()

    def close(self):
        self.destroy()
