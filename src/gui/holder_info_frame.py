import tkinter as tk

class HolderInfoFrame(tk.LabelFrame):
    def __init__(self, parent, holder, account, padding=(10,10)):
        super().__init__()

        self.parent_window = parent
        self.holder = holder
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

        self.holder_name_label_text = "> Holder: "
        self.holder_name_data_label_text = f"{self.holder.first_name} {self.holder.last_name}"
        self.info_currency_label_text = "> Currency: "
        self.info_currency_data_label_text = self.account.currency
        self.info_interest_rate_label_text = "> Interest: "
        self.info_interest_rate_data_label_text = f"{self.account.interest_rate}%"


        # widgets
        self.holder_name_label = tk.Label(self, text=self.holder_name_label_text)
        self.holder_name_label.grid(row=0, column=0, pady=(10, 0), padx=(0, 20), sticky="w")
        self.holder_name_data_label = tk.Label(self, text=self.holder_name_data_label_text)
        self.holder_name_data_label.grid(row=0, column=1, pady=(10, 0), sticky="w")

        self.info_currency_label = tk.Label(self, text=self.info_currency_label_text)
        self.info_currency_label.grid(row=1, column=0, pady=(10, 10), padx=(0, 20), sticky="w")
        self.info_currency_data_label = tk.Label(self, text=self.info_currency_data_label_text)
        self.info_currency_data_label.grid(row=1, column=1, pady=(10, 10), sticky="w")

        self.info_interest_rate_label = tk.Label(self, text=self.info_interest_rate_label_text)
        self.info_interest_rate_label.grid(row=2, column=0, pady=(0, 10), padx=(0, 20), sticky="w")
        self.info_interest_rate_data_label = tk.Label(self, text=self.info_interest_rate_data_label_text)
        self.info_interest_rate_data_label.grid(row=2, column=1, pady=(0, 10), sticky="w")





