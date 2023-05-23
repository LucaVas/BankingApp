import tkinter as tk
import customtkinter as ctk

class BalanceFrame(ctk.CTkFrame):
    def __init__(self, parent, account):
        super().__init__(parent)

        self.parent_window = parent
        self.account = account

        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((0), weight=1)


        self.balance_label_text = "Your balance:"
        self.balance_amount_label_text = self.account.balance
        self.balance_currency_label_text = self.account.currency


        # widgets
        self.balance_label = ctk.CTkLabel(self, text=self.balance_label_text, font=ctk.CTkFont("Tahoma", size=20, weight="bold"))
        self.balance_label.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.balance_amount_label = ctk.CTkLabel(self, text=self.balance_amount_label_text, font=ctk.CTkFont("Tahoma", size=20, weight="bold"))
        self.balance_amount_label.grid(row=0, column=2, sticky="w")

        self.balance_currency_label = ctk.CTkLabel(self, text=self.balance_currency_label_text, font=ctk.CTkFont("Tahoma", size=20, weight="bold"))
        self.balance_currency_label.grid(row=0, column=3, sticky="ew")


