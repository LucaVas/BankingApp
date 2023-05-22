import tkinter as tk

class BankInfoFrame(tk.LabelFrame):
    def __init__(self, parent, bank, padding=(10,10)):
        super().__init__()

        self.parent_window = parent
        self.bank = bank

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

        self.shares_amount_label_text = "> Shares: "
        self.shares_amount_data_label_text = self.bank.shares_amount
        self.shares_price_label_text = "> PPS: "
        self.shares_price_data_label_text = self.bank.share_price
        self.shares_delta_label_text = "> Shares price delta: "
        self.shares_delta_data_label_text = f"{self.bank.shares_delta}%"


        # widgets
        self.shares_amount_label = tk.Label(self, text=self.shares_amount_label_text)
        self.shares_amount_label.grid(row=0, column=0)
        self.shares_amount_data_label = tk.Label(self, text=self.shares_amount_data_label_text)
        self.shares_amount_data_label.grid(row=0, column=1)

        self.shares_price_label = tk.Label(self, text=self.shares_price_label_text)
        self.shares_price_label.grid(row=1, column=0)
        self.shares_price_data_label = tk.Label(self, text=self.shares_price_data_label_text)
        self.shares_price_data_label.grid(row=1, column=1)

        self.shares_delta_label = tk.Label(self, text=self.shares_delta_label_text)
        self.shares_delta_label.grid(row=2, column=0)
        self.shares_delta_data_label = tk.Label(self, text=self.shares_delta_data_label_text)
        self.shares_delta_data_label.grid(row=2, column=1)





