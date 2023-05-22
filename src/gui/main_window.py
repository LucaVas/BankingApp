import tkinter as tk
from .top_up_window import TopUpWindow
from .holder_info_frame import HolderInfoFrame
from .bank_info_frame import BankInfoFrame
from .balance_frame import BalanceFrame
from .exchange_frame import ExchangeFrame
from .balance_exchange_frame import BalanceExchangeFrame



class MainWindow(tk.Tk):
    def __init__(self, holder, account, bank, padding=(20, 20)):
        super().__init__()

        self.holder = holder
        self.account = account
        self.bank = bank


        # geometry & positioning
        # self.width = 1000
        # self.height = 500
        # self.screen_width = self.winfo_screenwidth()
        # self.screen_height = self.winfo_screenheight()
        # self.x = (self.screen_width / 2) - (self.width / 2)
        # self.y = (self.screen_height / 2) - (self.height / 2)
        # self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")


        # text content of widgets
        self.padding = padding
        self.configure(
            {   
                "highlightthickness" : 0,
                # border thickness
                "bd" : 0,
                "padx" : self.padding[0],
                "pady" : self.padding[1]
            }
        )
        self.title("Bank99")
        self.main_label_text = "Your account overview"
        self.top_up_button_text = "Top up"
        self.transfer_button_text = "Transfer"
        self.log_out_button_text = "Log out"

        # style
        self.btn_padx = 15
        self.btn_pady = 5

        # widget
        self.main_label = tk.Label(self, text=self.main_label_text, font=("Tahoma", 20))
        self.main_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
    

        # frames
        self.balance_frame = BalanceFrame(self, self.account, padding=(20, 20))
        self.balance_frame.grid(row=1, column=2, padx=20, pady=20, columnspan=2)

        self.exchange_frame = ExchangeFrame(self, self.account, padding=(20, 20))
        self.exchange_frame.grid(row=3, column=4, padx=20, pady=20, rowspan=2)

        self.balance_exchange_frame = BalanceExchangeFrame(self, self.exchange_frame, padding=(20, 20))
        self.balance_exchange_frame.grid(row=2, column=3)

        self.holder_info_frame = HolderInfoFrame(self, self.holder, self.account, padding=(20,20))
        self.holder_info_frame.grid(row=1, column=4, padx=20, pady=20, rowspan=2)

        self.bank_info_frame = BankInfoFrame(self, self.bank, padding=(20,20))
        self.bank_info_frame.grid(row=5,column=4, padx=20, pady=20, rowspan=2)


        # buttons
        self.top_up_button = tk.Button(self, text=self.top_up_button_text, font=("Tahoma, 12"), padx=self.btn_padx, pady=self.btn_pady, state="active", command=self.open_top_up_window).grid(row=1,column=0)

        self.transfer_button = tk.Button(self, text=self.transfer_button_text, font=("Tahoma, 12"), padx=self.btn_padx, pady=self.btn_pady, state="active", command=self.open_transfer_window).grid(row=2,column=0)
        
        self.log_out_button = tk.Button(self, text=self.log_out_button_text, font=("Tahoma, 12"), padx=self.btn_padx, pady=self.btn_pady, state="active", command=self.log_out).grid(row=6,column=3)

    
    def open_top_up_window(self):
        top_up_window = TopUpWindow(self)
        top_up_window.start()

    def open_transfer_window(self):
        pass        
        
    def start(self):
        self.mainloop()

    def log_out(self):
        self.destroy()

