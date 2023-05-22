import tkinter as tk

class MainContainer(tk.Frame):
    def __init__(self, parent, holder, account, bank):
        super().__init__(self)
        self.parent = parent


        self.title("Bank99")
        self.main_label_text = "Your account overview"
        self.balance_label_text = "Your balance:"
        self.balance_amount_label_text = self.account.balance
        self.acc_text = ""
        self.top_up_button_text = "Top up"
        self.transfer_button_text = "Transfer"
        self.log_out_button_text = "Log out"

        # style
        self.btn_padx = 15
        self.btn_pady = 5

        # widgets
        self.main_label = tk.Label(self, text=self.main_label_text)
        self.main_label.grid(row=0, column=0, columnspan=2, font=("Tahoma, 25"), padx=20, pady=20)


        self.balance_label = tk.Label(self, text=self.balance_label_text)
        self.balance_label.grid(row=1, column=1)

        self.balance_amount_label = tk.Label(self, text=self.balance_amount_label_text)
        self.balance_amount_label.grid(row=1, column=2)

        self.acc = tk.Label(self, text=self.acc_text)
        self.acc.grid(row=2, column=1)


        # frames
        self.holder_info_frame = HolderInfoFrame(self, self.holder, self.account, padding=(20,20))
        self.holder_info_frame.grid(row=1, column=3, padx=20, pady=20)

        self.bank_info_frame = BankInfoFrame(self, self.bank, padding=(20,20))
        self.bank_info_frame.grid(row=3,column=3, padx=20, pady=20)


        # buttons
        self.top_up_button = tk.Button(self, text=self.top_up_button_text, font=("Tahoma, 12"), padx=self.btn_padx, pady=self.btn_pady, state="active", command=self.open_top_up_window).grid(row=2,column=0)

        self.transfer_button = tk.Button(self, text=self.transfer_button_text, font=("Tahoma, 12"), padx=self.btn_padx, pady=self.btn_pady, state="active", command=self.open_transfer_window).grid(row=3,column=0)
        
        self.log_out_button = tk.Button(self, text=self.log_out_button_text, font=("Tahoma, 12"), padx=self.btn_padx, pady=self.btn_pady, state="active", command=self.log_out).grid(row=4,column=3)

    
    def open_top_up_window(self):
        top_up_window = TopUpWindow(self)
        top_up_window.start()

    def open_transfer_window(self):
        pass        
        
    def start(self):
        self.mainloop()

    def log_out(self):
        self.destroy()


        