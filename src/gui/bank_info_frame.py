import tkinter as tk
import customtkinter as ctk

class BankInfoFrame(ctk.CTkFrame):
    def __init__(self, parent, bank):
        super().__init__(parent)

        self.parent_window = parent
        self.bank = bank

        self.grid_columnconfigure((1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.shares_amount_label_text = "> Shares: "
        self.shares_amount_data_label_text = self.bank.shares_amount
        self.shares_price_label_text = "> PPS: "
        self.shares_price_data_label_text = self.bank.share_price
        self.shares_delta_label_text = "> Shares price delta: "
        self.shares_delta_data_label_text = f"{self.bank.shares_delta:.2f}%"


        # widgets
        self.shares_amount_label = ctk.CTkLabel(self, text=self.shares_amount_label_text, font=ctk.CTkFont("Tahoma", size=15, weight="bold"))
        self.shares_amount_label.grid(row=0, column=0, padx=(15,0), sticky="w")
        self.shares_amount_data_label = ctk.CTkLabel(self, text=self.shares_amount_data_label_text, font=ctk.CTkFont("Tahoma", size=15, weight="normal"))
        self.shares_amount_data_label.grid(row=0, column=1, sticky="nsew")

        self.shares_price_label = ctk.CTkLabel(self, text=self.shares_price_label_text, font=ctk.CTkFont("Tahoma", size=15, weight="bold"))
        self.shares_price_label.grid(row=1, column=0, padx=(15,0), sticky="w")
        self.shares_price_data_label = ctk.CTkLabel(self, text=self.shares_price_data_label_text, font=ctk.CTkFont("Tahoma", size=15, weight="normal"))
        self.shares_price_data_label.grid(row=1, column=1, sticky="nsew")

        self.shares_delta_label = ctk.CTkLabel(self, text=self.shares_delta_label_text, font=ctk.CTkFont("Tahoma", size=15, weight="bold"))
        self.shares_delta_label.grid(row=2, column=0, padx=(15,0), sticky="w")
        self.shares_delta_data_label = ctk.CTkLabel(self, text=self.shares_delta_data_label_text, font=ctk.CTkFont("Tahoma", size=15, weight="normal"))
        self.shares_delta_data_label.grid(row=2, column=1, sticky="nsew")





