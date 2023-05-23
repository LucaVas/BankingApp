import tkinter as tk
from tkinter import messagebox


class AccountRegistrationWindow(tk.Tk):
    def __init__(self, list_of_currencies: list[str], bank):
        super().__init__()

        self.currency_list = list_of_currencies

        # geometry & positioning
        # self.width = 1000
        # self.height = 600
        # self.screen_width = self.winfo_screenwidth()
        # self.screen_height = self.winfo_screenheight()
        # self.x = (self.screen_width / 2) - (self.width / 2)
        # self.y = (self.screen_height / 2) - (self.height / 2)
        # self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")
        self.attributes("-topmost", True)


        # holder information
        self.title(bank.name)
        self.balance = 0.0
        self.currency = ""
        self.interest_rate = ""

        # widgets variables
        self.account_registration_label_text = "Account registration"
        self.interest_rate_label_text = "> Select the interest rate:"
        self.interest_rate_optionmenu_options = [
            "1.8",
            "2.0",
            "2.5"
        ]
        self.interest_rate_optionmenu_var = tk.StringVar()
        self.currency_label_text = "> Select the account currency:"
        self.currency_optionmenu_options = self.currency_list
        self.currency_optionmenu_var = tk.StringVar()
        self.amount_label_text = "> Enter the initial balance amount:"
        self.register_account_button_text = "Save account"

        # style
        self.btn_padx = 10
        self.btn_pady = 5

        # widgets
        self.account_registration_label = tk.Label(self, text=self.account_registration_label_text)
        self.account_registration_label.grid(row=0, column=0)

        self.interest_rate_label = tk.Label(self, text=self.interest_rate_label_text)
        self.interest_rate_label.grid(row=1, column=0)
        self.interest_rate_optionmenu = tk.OptionMenu(self, self.interest_rate_optionmenu_var, *self.interest_rate_optionmenu_options)
        # default option
        self.interest_rate_optionmenu_var.set(self.interest_rate_optionmenu_options[0])
        self.interest_rate_optionmenu.grid(row=1, column=1)


        self.currency_label = tk.Label(self, text=self.currency_label_text)
        self.currency_label.grid(row=2, column=0)
        self.currency_optionmenu = tk.OptionMenu(self, self.currency_optionmenu_var, *self.currency_optionmenu_options)
        # default option
        self.currency_optionmenu_var.set(self.currency_optionmenu_options[0])
        self.currency_optionmenu.grid(row=2, column=1)


        self.amount_label = tk.Label(self, text=self.amount_label_text)
        self.amount_label.grid(row=3, column=0)
        self.amount_entry = tk.Entry(self, width=30, borderwidth=5)
        self.amount_entry.grid(row=3, column=1)


        self.message_label = tk.Label(self, text="")
        self.message_label.grid(row=4, column=0)

        self.register_account_button = tk.Button(self, text=self.register_account_button_text, padx=self.btn_padx, pady=self.btn_pady, state="active", command=self.validate_input).grid(row=5,column=2)


    def validate_input(self) -> None:
        try:
            amount = float(self.amount_entry.get())
        except (ValueError):
            self.show_error()
            return
        
        if amount < 0:
            self.show_error()
            return
        else:
            self.register_account(amount)
    
    def register_account(self, amount: float) -> None:
        self.interest_rate = self.interest_rate_optionmenu_var.get()
        self.currency = self.currency_optionmenu_var.get()
        self.balance = amount

        self.close()


    def show_error(self) -> None:
        # parent=self keeps the popup window in front
        messagebox.showerror("Error", "Balance input not correct", parent=self)
        
    def start(self):
        self.mainloop()

    def close(self):
        self.destroy()