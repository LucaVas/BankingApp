import tkinter as tk
from tkinter import messagebox


class TopUpWindow(tk.Toplevel):
    def __init__(self, parent) -> None:
        super().__init__()

        self.parent_window = parent
        self.width = 400
        self.height = 300
        self.geometry(f"{self.width}x{self.height}+{int(self.parent_window.x)}+{int(self.parent_window.y)}")
        # prevent window to get hidden when pop up appears
        self.attributes("-topmost", True)

        self.title("Top Up")
        self.main_lable_text = "Top Up"
        self.amount_label_text = "> Insert the amount"
        self.account_from_label_text = "> Account from"
        self.account_from_optionmenu_options = [
            "LT1",
            "LT2",
            "LT3"
        ]
        self.account_from_optionmenu_var = tk.StringVar()
        self.top_up_button_text = "Confirm"

        # Main label: Top Up
        self.main_label = tk.Label(self, text=self.main_lable_text)
        self.main_label.grid(row=0, column=0, padx=20, pady=20)

        # Entry label: Amount
        self.amount_label = tk.Label(self, text=self.amount_label_text)
        self.amount_label.grid(row=1, column=0)

        # Entry: Amount
        self.amount_entry = tk.Entry(self, width=30, borderwidth=5)
        self.amount_entry.grid(row=1, column=1)

        # Option Label: Account from
        self.account_from_label = tk.Label(self, text=self.account_from_label_text)
        self.account_from_label.grid(row=2, column=0)

        # Option: account from
        self.account_from_optionmenu = tk.OptionMenu(self, self.account_from_optionmenu_var, *self.account_from_optionmenu_options)
        # default option
        self.account_from_optionmenu_var.set(self.account_from_optionmenu_options[0])
        self.account_from_optionmenu.grid(row=2, column=1)

        self.button = tk.Button(self, text=self.top_up_button_text, command=lambda: self.validate_top_up())
        self.button.grid(row=3, column=1)


    def validate_top_up(self) -> None:
        
        try:
            amount = float(self.amount_entry.get())
        except (ValueError):
            self.show_error()
            return

        if amount < 0 or not amount:
            self.show_error()
        else:
            self.top_up(float(amount))


    def top_up(self, amount: float) -> None:
        current_amount = self.parent_window.balance_amount_label.cget("text")
        account_from = self.account_from_optionmenu_var.get()

        self.parent_window.balance_amount_label.configure(text=current_amount + amount)
        self.parent_window.acc.configure(text=account_from)

        self.close()

    def show_error(self) -> None:
        # parent=self keeps the popup window in front
        messagebox.showerror("Error", "Incorrect amount", parent=self)

    def start(self) -> None:
        self.mainloop()

    def close(self) -> None:
        self.destroy()





