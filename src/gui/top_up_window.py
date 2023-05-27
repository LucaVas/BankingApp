import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from datetime import datetime
import logging


class TopUpWindow(ctk.CTkToplevel):
    def __init__(self, parent, temp_db, holder, writer, treeview_frame, account) -> None:
        super().__init__()

        self.parent_window = parent
        self.temp_db = temp_db
        self.holder = holder
        self.writer = writer
        self.treeview_frame = treeview_frame
        self.account = account

        # geometry & positioning
        self.width = 500
        self.height = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")
        self.attributes("-topmost", True)

        # grid layout
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.title("Top Up")
        self.main_label_text = "Top Up"
        self.amount_label_text = "> Insert the amount"
        self.account_from_label_text = "> Account from"
        self.account_from_optionmenu_options = self.parent_window.holder.connected_accounts
        self.account_from_optionmenu_var = tk.StringVar(value=self.account_from_optionmenu_options[0])
        self.top_up_button_text = "Top up"

        # ============ Top frame with main label ============ #
        self.main_label_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_label_frame.grid(row=0, column=0, columnspan=3, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.main_label_frame.grid_rowconfigure(0, weight=1)
        self.main_label = ctk.CTkLabel(self.main_label_frame, text=self.main_label_text, font=ctk.CTkFont(size=20, weight="normal"))
        self.main_label.grid(row=0, column=0, padx=(10,10), pady=(10,10))

        # ============ Main frame with entries ============ #
        self.entries_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.entries_frame.grid(row=1, column=0, columnspan=3, padx=(10, 10), pady=(0, 10), sticky="nsew")
        self.entries_frame.grid_rowconfigure((0,1, 2), weight=1)
        self.entries_frame.grid_columnconfigure((0,1,2), weight=1)

        # Entry label: Amount
        self.amount_label = ctk.CTkLabel(self.entries_frame, text=self.amount_label_text, font=ctk.CTkFont(size=15, weight="normal"))
        self.amount_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")
        self.amount_entry = ctk.CTkEntry(self.entries_frame)
        self.amount_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=(10,10), sticky="ew")


        # Option Label: Account from
        self.account_from_label = ctk.CTkLabel(self.entries_frame, text=self.account_from_label_text, font=ctk.CTkFont(size=15, weight="normal"))
        self.account_from_label.grid(row=1, column=0, padx=10, pady=(10,10), sticky="w")
        self.account_from_optionmenu = ctk.CTkOptionMenu(self.entries_frame, values=self.account_from_optionmenu_options, variable=self.account_from_optionmenu_var)
        self.account_from_optionmenu.grid(row=1, column=1, columnspan=2, padx=10, pady=(10,10), sticky="ew")
        # Option: account from

        self.message_label = ctk.CTkLabel(self, text="")
        self.message_label.grid(row=2, column=0, columnspan=3)


        # ============ Bottom row with button ============ #
        self.top_up_button = ctk.CTkButton(self, text=self.top_up_button_text, state="active", text_color="black", font=("tahoma", 16), command=self.validate_top_up)
        self.top_up_button.grid(row=3, column=2, padx=10, pady=(10,10), sticky="ew")


    def validate_top_up(self) -> None:
        
        try:
            amount = float(self.amount_entry.get())
        except (ValueError):
            self.show_error()
            return

        if amount < 0 or not amount:
            self.show_error()
        else:
            self.top_up(amount)


    def top_up(self, amount: float) -> None:
        action = "top-up"
        recipient_account = self.account.account_number 
        datestamp = datetime.now()  
        reason = "Top up to self"      
        
        current_amount = self.parent_window.balance_frame.balance_amount_label.cget("text")
        self.parent_window.balance_frame.balance_amount_label.configure(text=current_amount + amount)
        
        self.parent_window.account.balance = current_amount + amount

        self.add_action_to_treeview(amount, action, recipient_account, datestamp)
        self.add_action_to_db(amount, action, recipient_account, datestamp, reason)

        self.clear_exchanged_balance()

        self.close()

    def clear_exchanged_balance(self) -> None:
        self.parent_window.balance_exchange_frame.exchange_balance_amount_label.configure(text="") 
        self.parent_window.balance_exchange_frame.exchange_currency_label.configure(text="") 

    def add_action_to_treeview(self, amount: float, action: str, recipient_account: str, datestamp: datetime) -> None:
        self.treeview_frame.add_record(action, amount, recipient_account, str(datestamp))

    def add_action_to_db(self, amount: float, action: str, recipient_account: str, datestamp: datetime, reason) -> None:
        self.writer.temp_write_history(self.holder, action, amount, recipient_account, datestamp, reason, self.temp_db)

    def show_error(self) -> None:
        # parent=self keeps the popup window in front
        messagebox.showerror("Error", "Incorrect amount", parent=self)

    def close(self) -> None:
        self.destroy()





