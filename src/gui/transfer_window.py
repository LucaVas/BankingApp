import tkinter as tk
from tkinter import messagebox
from typing import Optional


class TransferWindow(tk.Toplevel):
    def __init__(self, parent, account, padding=(20,20)) -> None:
        super().__init__()

        self.parent_window = parent
        self.account = account
        self.attributes("-topmost", True)

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

        self.title("Transfer")
        self.main_lable_text = "Transfer"
        self.amount_label_text = "> Insert the amount"
        self.recipient_account_label_text = "> Account to"
        self.reason_label_text = "> Enter the reason for transfer"
        self.confirm_button_text = "Confirm"

        # Main label: Top Up
        self.main_label = tk.Label(self, text=self.main_lable_text)
        self.main_label.grid(row=0, column=0, padx=20, pady=20)

        # Entry label: Amount
        self.amount_label = tk.Label(self, text=self.amount_label_text)
        self.amount_label.grid(row=1, column=0)

        # Entry: Amount
        self.amount_entry = tk.Entry(self, width=30, borderwidth=5)
        self.amount_entry.grid(row=1, column=1)

        # Option Label: Account to
        self.recipient_account_label = tk.Label(self, text=self.recipient_account_label_text)
        self.recipient_account_label.grid(row=2, column=0)

        # Option: account to
        self.recipient_account_entry = tk.Entry(self, width=30, borderwidth=5)
        self.recipient_account_entry.grid(row=2, column=1)


        self.reason_label = tk.Label(self, text=self.reason_label_text)
        self.reason_label.grid(row=3, column=0)

        self.reason_entry = tk.Entry(self, width=30, borderwidth=5)
        self.reason_entry.grid(row=3, column=1)


        self.confirm_button = tk.Button(self, text=self.confirm_button_text, command=lambda: self.validate_transfer())
        self.confirm_button.grid(row=4, column=1)


    def validate_transfer(self) -> None:
        
        amount, current_amount = self.validate_amount()
        recipient_account = self.validate_recipient()
        reason = self.validate_reason()
        
        self.transfer(amount, current_amount, recipient_account, reason)


    def validate_recipient(self) -> str:
        recipient_account = self.recipient_account_entry.get()
        if len(recipient_account) != 20:
            self.show_error("Invalid recipient")
            raise Exception()
        else:
            return recipient_account

    def validate_reason(self) -> str:
        reason = self.reason_entry.get()
        if not reason:
            self.show_error("Invalid reason")
            raise Exception
        else:
            return reason            

    def validate_amount(self) -> tuple[float, float]:
        try:
            amount = float(self.amount_entry.get())
        except (ValueError):
            self.show_error("Invalid amount")
            raise Exception

        current_amount = float(self.parent_window.balance_frame.balance_amount_label.cget("text"))
            
        if amount < 0 or not amount:
            self.show_error("Invalid amount")
            raise Exception
        elif current_amount < amount:
            self.show_error("Invalid amount")
            raise Exception
        else:
            return amount, current_amount

    def transfer(self, amount: float, current_amount: float, recipient_account: str, reason: str) -> None:

        self.parent_window.balance_frame.balance_amount_label.configure(text=current_amount - amount)

        self.close()

    def show_error(self, text:str) -> None:
        # parent=self keeps the popup window in front
        messagebox.showerror("Error", text, parent=self)

    def start(self) -> None:
        self.mainloop()

    def close(self) -> None:
        self.destroy()





