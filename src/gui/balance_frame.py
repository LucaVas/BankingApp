import tkinter as tk

class BalanceFrame(tk.LabelFrame):
    def __init__(self, parent, account, padding=(20,20)):
        super().__init__()

        self.parent_window = parent
        self.account = account

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

        self.balance_label_text = "Your balance:"
        self.balance_amount_label_text = self.account.balance
        self.balance_currency_label_text = self.account.currency


        # widgets
        self.balance_label = tk.Label(self, text=self.balance_label_text, font=("Tahoma", 15))
        self.balance_label.grid(row=0, column=0, pady=(10, 0), padx=(0, 20), sticky="w")

        self.balance_amount_label = tk.Label(self, text=self.balance_amount_label_text, font=("Tahoma", 15))
        self.balance_amount_label.grid(row=0, column=1, pady=(10, 0), sticky="w")

        self.balance_currency_label = tk.Label(self, text=self.balance_currency_label_text, font=("Tahoma", 15))
        self.balance_currency_label.grid(row=0, column=2, pady=(10, 0), sticky="w")


