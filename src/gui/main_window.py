import tkinter as tk
import customtkinter as ctk
from .top_up_window import TopUpWindow
from .holder_info_frame import HolderInfoFrame
from .bank_info_frame import BankInfoFrame
from .balance_frame import BalanceFrame
from .exchange_frame import ExchangeFrame
from .balance_exchange_frame import BalanceExchangeFrame
from .transfer_window import TransferWindow

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class MainWindow(tk.Tk):
    def __init__(self, holder, account, bank, currency_obj):
        super().__init__()

        self.holder = holder
        self.account = account
        self.bank = bank
        self.currency_obj = currency_obj


        # geometry & positioning
        self.width = 1200
        self.height = 500
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")

        # grid layout
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        # variables
        self.title(bank.name)
        self.main_label_text = "Your account overview"
        self.top_up_button_text = "Top up"
        self.transfer_button_text = "Transfer"
        self.log_out_button_text = "Log out"


        # widget
        # ============ Sidebar ============ #
        self.sidebar_frame = ctk.CTkFrame(self, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=7, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)
        self.sidebar_frame.grid_columnconfigure((0,1,2), weight=1)


        self.main_label = ctk.CTkLabel(self.sidebar_frame, text=self.main_label_text, font=ctk.CTkFont("Tahoma", size=23, weight="bold"))
        self.main_label.grid(row=0, column=0, columnspan=3, padx=(5, 5), pady=(5, 5))
        self.top_up_button = ctk.CTkButton(self.sidebar_frame, text=self.top_up_button_text, state="active", command=self.open_top_up_window)
        self.top_up_button.grid(row=2, column=1, sticky="ew")
        self.transfer_button = ctk.CTkButton(self.sidebar_frame, text=self.transfer_button_text, state="active", command=self.open_transfer_window)
        self.transfer_button.grid(row=3, column=1, sticky="ew")
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:")
        self.appearance_mode_label.grid(row=5, column=1, sticky="ew")
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=1, sticky="ew", padx=(5, 5), pady=(5, 5))
    

        # ============ Right frames ============ #
        self.holder_info_frame = HolderInfoFrame(self, self.holder, self.account)
        self.holder_info_frame.grid(row=0, column=5, rowspan=2, padx=(5,5), pady=(5,5), sticky="nsew")

        self.exchange_frame = ExchangeFrame(self, self.account, self.currency_obj)
        self.exchange_frame.grid(row=2, column=5, rowspan=2, padx=(5,5), pady=(5,5), sticky="nsew")

        self.bank_info_frame = BankInfoFrame(self, self.bank)
        self.bank_info_frame.grid(row=4,column=5, rowspan=2, padx=(5,5), pady=(5,5), sticky="nsew")

        # ============ Center frames ============ #
        self.balance_frame = BalanceFrame(self, self.account)
        self.balance_frame.grid(row=0, column=1, columnspan=4, padx=(5,5), pady=(5,5), sticky="nsew")

        self.balance_exchange_frame = BalanceExchangeFrame(self, self.exchange_frame)
        self.balance_exchange_frame.grid(row=1, column=1, columnspan=4, padx=(5,5), pady=(5,5), sticky="nsew")


        # buttons
        self.log_out_button = ctk.CTkButton(self, text=self.log_out_button_text, state="active", command=self.log_out)
        self.log_out_button.grid(row=6,column=5, padx=(5,5), pady=(5,5))


    def change_appearance_mode_event(self, appearance_mode: str):
        ctk.set_appearance_mode(appearance_mode)

    
    def open_top_up_window(self):
        top_up_window = TopUpWindow(self)
        top_up_window.start()

    def open_transfer_window(self):
        transfer_window = TransferWindow(self, self.account)
        transfer_window.start()        
        
    def start(self):
        self.mainloop()

    def log_out(self):
        self.destroy()

