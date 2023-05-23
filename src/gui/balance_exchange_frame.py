import tkinter as tk

class BalanceExchangeFrame(tk.LabelFrame):
    def __init__(self, parent, exchange_frame, padding=(20,20)):
        super().__init__()

        self.parent_window = parent
        self.exchange_frame = exchange_frame

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

        self.exchange_labance_label_text = "> Exchanged to"
        self.exchange_balance_amount_label_text = " "
        self.exchange_currency_label_text = " "


        # widgets
        self.exchange_balance_amount_label = tk.Label(self, text=self.exchange_labance_label_text, font=("Tahoma", 15))
        self.exchange_balance_amount_label.grid(row=0, column=0, pady=(10, 10), sticky="w")
        
        self.exchange_balance_amount_label = tk.Label(self, text=self.exchange_balance_amount_label_text, font=("Tahoma", 15))
        self.exchange_balance_amount_label.grid(row=0, column=1, pady=(10, 0), sticky="w")

        self.exchange_currency_label = tk.Label(self, text=self.exchange_currency_label_text, font=("Tahoma", 15))
        self.exchange_currency_label.grid(row=0, column=2, pady=(10, 0), sticky="w")


