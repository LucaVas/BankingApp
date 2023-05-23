import tkinter as tk
import customtkinter as ctk

class HolderInfoFrame(ctk.CTkFrame):
    def __init__(self, parent, holder, account):
        super().__init__(parent)

        self.parent_window = parent
        self.holder = holder
        self.account = account

        self.grid_columnconfigure((1, 2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.holder_name_label_text = "> Holder: "
        self.holder_name_data_label_text = f"{self.holder.first_name} {self.holder.last_name}"
        self.info_currency_label_text = "> Currency: "
        self.info_currency_data_label_text = self.account.currency
        self.info_interest_rate_label_text = "> Interest: "
        self.info_interest_rate_data_label_text = f"{self.account.interest_rate}%"


        # widgets
        self.holder_name_label = ctk.CTkLabel(self, text=self.holder_name_label_text, font=ctk.CTkFont("Tahoma", size=15, weight="bold"))
        self.holder_name_label.grid(row=0, column=0, padx=(15,0), sticky="w")
        self.holder_name_data_label = ctk.CTkLabel(self, text=self.holder_name_data_label_text, font=ctk.CTkFont("Tahoma", size=15, weight="normal"))
        self.holder_name_data_label.grid(row=0, column=1, columnspan=2, sticky="ew")

        self.info_currency_label = ctk.CTkLabel(self, text=self.info_currency_label_text, font=ctk.CTkFont("Tahoma", size=15, weight="bold"))
        self.info_currency_label.grid(row=1, column=0, padx=(15,0), sticky="w")
        self.info_currency_data_label = ctk.CTkLabel(self, text=self.info_currency_data_label_text, font=ctk.CTkFont("Tahoma", size=15, weight="normal"))
        self.info_currency_data_label.grid(row=1, column=1, columnspan=2, sticky="ew")

        self.info_interest_rate_label = ctk.CTkLabel(self, text=self.info_interest_rate_label_text, font=ctk.CTkFont("Tahoma", size=15, weight="bold"))
        self.info_interest_rate_label.grid(row=2, column=0, padx=(15,0), sticky="w")
        self.info_interest_rate_data_label = ctk.CTkLabel(self, text=self.info_interest_rate_data_label_text, font=ctk.CTkFont("Tahoma", size=15, weight="normal"))
        self.info_interest_rate_data_label.grid(row=2, column=1, columnspan=2, sticky="ew")





