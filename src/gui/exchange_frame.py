import tkinter as tk
import customtkinter as ctk

class ExchangeFrame(ctk.CTkFrame):
    def __init__(self, parent, account, currency_obj):
        super().__init__(parent)

        self.parent_window = parent
        self.account = account
        self.currency_obj = currency_obj

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.exchange_label_text = "Currency exchange"
        self.currency_optionmenu_options = self.currency_obj.currencies
        self.currency_optionmenu_var = tk.StringVar(value=self.currency_optionmenu_options[0])


        # widgets
        self.exchange_label = ctk.CTkLabel(self, text=self.exchange_label_text)
        self.exchange_label.grid(row=0, column=0, columnspan=3, sticky="ew")

        # Option: account from
        self.currency_optionmenu = ctk.CTkOptionMenu(self, values=self.currency_optionmenu_options, variable=self.currency_optionmenu_var, command=self.update_exchange)
        # default option
        self.currency_optionmenu.grid(row=1, column=1)

    def update_exchange(self, option):
        exchange_rate = self.get_exchange(option)
        current_balance = float(self.parent_window.balance_frame.balance_amount_label.cget("text"))
        exchanged_balance = current_balance * exchange_rate

        self.parent_window.balance_exchange_frame.exchange_balance_amount_label.configure(text=f"{exchanged_balance:.2f}")
        self.parent_window.balance_exchange_frame.exchange_currency_label.configure(text=option)

    def get_exchange(self, currency: str) -> float:
        return self.currency_obj.get_exchange(currency)


