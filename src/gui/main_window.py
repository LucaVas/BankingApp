import tkinter as tk
from tkinter import messagebox
from .top_up_window import TopUpWindow


class MainWindow(tk.Tk):
    def __init__(self, holder, account, bank):
        super().__init__()

        self.holder = holder
        self.account = account
        self.bank = bank

        # geometry & positioning
        self.width = 600
        self.height = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")


        # text content of widgets
        # self.iconbitmap("img/bank-50.png")
        self.title("Bank99")
        self.balance_label_text = "Your balance:"
        self.balance_amount_label_text = self.account.balance
        self.acc_text = ""
        self.top_up_button_text = "Top up"
        self.log_out_button_text = "Log out"

        # style
        self.btn_padx = 10
        self.btn_pady = 5

        # widgets
        self.balance_label = tk.Label(self, text=self.balance_label_text)
        self.balance_label.grid(row=0, column=0)

        self.balance_amount_label = tk.Label(self, text=self.balance_amount_label_text)
        self.balance_amount_label.grid(row=0, column=1)

        self.acc = tk.Label(self, text=self.acc_text)
        self.acc.grid(row=1, column=1)

        self.top_up_button = tk.Button(self, text=self.top_up_button_text, padx=self.btn_padx, pady=self.btn_pady, state="active", command=self.open_top_up_window).grid(row=2,column=2)

        self.log_out_button = tk.Button(self, text=self.log_out_button_text, padx=self.btn_padx, pady=self.btn_pady, state="active", command=self.log_out).grid(row=3,column=2)

    
    def open_top_up_window(self):
        top_up_window = TopUpWindow(self)
        top_up_window.start()
        
        
    def start(self):
        self.mainloop()

    def log_out(self):
        self.destroy()
