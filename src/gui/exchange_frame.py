import tkinter as tk

class ExchangeFrame(tk.LabelFrame):
    def __init__(self, parent, account, currency_obj, padding=(20,20)):
        super().__init__()

        self.parent_window = parent
        self.account = account
        self.currency_obj = currency_obj

        # format
        self.padding = padding
        self.configure(
            {   
                "highlightthickness" : 0,
                # border thickness
                "bd" : 1,
                "padx" : self.padding[0],
                "pady" : self.padding[1]
            }
        )

        self.exchange_label_text = "Currency exchange"
        self.currency_optionmenu_options = self.currency_obj.currencies
        self.currency_optionmenu_var = tk.StringVar()


        # widgets
        self.exchange_label = tk.Label(self, text=self.exchange_label_text, font=("Tahoma", 10))
        self.exchange_label.grid(row=0, column=0, pady=(10, 0), padx=(0, 20), sticky="ew")

        # Option: account from
        self.currency_optionmenu = tk.OptionMenu(self, self.currency_optionmenu_var, *self.currency_optionmenu_options, command=self.update_exchange)
        # default option
        self.currency_optionmenu_var.set(self.currency_optionmenu_options[0])
        self.currency_optionmenu.grid(row=1, column=0, padx=(10,10), pady=(10, 10), columnspan=2)

    def update_exchange(self, option):
        exchange_rate = self.get_exchange(option)
        current_balance = float(self.parent_window.balance_frame.balance_amount_label.cget("text"))
        exchanged_balance = current_balance * exchange_rate

        self.parent_window.balance_exchange_frame.exchange_balance_amount_label.configure(text=f"{exchanged_balance:.2f}")
        self.parent_window.balance_exchange_frame.exchange_currency_label.configure(text=option)

    def get_exchange(self, currency: str) -> float:
        return self.currency_obj.get_exchange(currency)


