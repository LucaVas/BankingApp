import customtkinter as ctk

ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode("dark") # "system" (default), "dark", "light"

class MainGui(ctk.CTk):
    """
    Main class where I run my main window section
    """

    account_info: list[str] = []

    def __init__(self):
        super().__init__()

        self.title("Luca's bank")
        self.width = "1000"
        self.height = "500"
        self.geometry(f"{self.width}x{self.height}")



class MainWindow(MainGui):
    """
    Class which contains the main window of my application
    """
    def __init__(self):
        super().__init__()

        self.grid_columnconfigure((0,1,2,3), weight=2)
        self.grid_rowconfigure((0,1,2,3,4), weight=1)


        """ First column """
        # Label: "Your Account"
        self.title_label = ctk.CTkLabel(self, text="Your Account", fg_color="transparent", text_color="white", font=("tahoma", 24))
        self.title_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")

        # Button: "Top-Up"
        self.button_top_up = ctk.CTkButton(self, width=40, height=40, text="Top-Up", text_color="black", font=("tahoma", 16), command=self.top_up)
        self.button_top_up.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        # Button: "Transfer"
        self.button_transfer = ctk.CTkButton(self, width=40, height=40, text="Transfer", text_color="black", font=("tahoma", 16), command=self.transfer)
        self.button_transfer.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        # Label: "Appearance mode"
        self.appearence_label = ctk.CTkLabel(self, text="> Appearence mode", fg_color="transparent", text_color="white", font=("tahoma", 15))
        self.appearence_label.grid(row=3, column=0, padx=10, pady=(10,10), sticky="w")

        # Options: "Appearence Mode"
        self.appearance_option = ctk.CTkOptionMenu(self, values=["Light", "Dark"])
        self.appearance_option.grid(row=4, column=0, padx=10, pady=(10,10), sticky="w")


        """ Second column """
        self.balance_frame = BalanceFrame(master=self)
        self.balance_frame.grid(row=0, column=1, columnspan=2, padx=20, pady=20, sticky="nsew")

        self.currency_frame = CurrencyFrame(master=self)
        self.currency_frame.grid(row=1, column=2, padx=20, pady=20, sticky="nsew")

        self.transfers_list_frame = TransfersListFrame(master=self)
        self.transfers_list_frame.grid(row=2, column=1, columnspan=2, rowspan=2, padx=20, pady=20, sticky="nsew")

        # Messages log lable
        self.message_label = ctk.CTkLabel(self, text="Message", text_color="red", font=("tahoma", 15))
        self.message_label.grid(row=4, column=1, columnspan=2, padx=10, pady=(10,10), sticky="w")   


        """ Fourth column """
        self.account_info_frame = AccountInfoFrame(master=self)
        self.account_info_frame.grid(row=0, column=3, rowspan=2, padx=20, pady=20, sticky="nsew")
    
        self.exchange_frame = ExchangeFrame(master=self)
        self.exchange_frame.grid(row=2, column=3, padx=20, pady=20, sticky="nsew")

    def top_up(self):
        pass
        
    def transfer(self):
        pass

    def kill_window(self):
        self.destroy()
        

class BalanceFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Label: "Balance"
        self.balance_label = ctk.CTkLabel(self, text="> Balance", fg_color="transparent", text_color="white", font=("tahoma", 24))
        self.balance_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")

        # Label: Amount
        self.amount_label = ctk.CTkLabel(self, text="1850", fg_color="transparent", text_color="white", font=("tahoma", 27))
        self.amount_label.grid(row=0, column=1, padx=10, pady=(10,10), sticky="w")

        # Label: Currency

        self.currency_label = ctk.CTkLabel(self, text="EUR", fg_color="transparent", text_color="white", font=("tahoma", 27))
        self.currency_label.grid(row=0, column=2, padx=10, pady=(10,10), sticky="w")


class CurrencyFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Label: Amount
        self.amount_label = ctk.CTkLabel(self, text="1940", fg_color="transparent", text_color="white", font=("tahoma", 27))
        self.amount_label.grid(row=0, column=1, padx=10, pady=(10,10), sticky="w")

        # Label: Currency
        self.currency_label = ctk.CTkLabel(self, text="USD", fg_color="transparent", text_color="white", font=("tahoma", 27))
        self.currency_label.grid(row=0, column=2, padx=10, pady=(10,10), sticky="w")


class TransfersListFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Label: Action
        self.action_label = ctk.CTkLabel(self, text="Action", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.action_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")

        # Label: Amount
        self.amount_label = ctk.CTkLabel(self, text="Amount", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.amount_label.grid(row=0, column=1, padx=10, pady=(10,10), sticky="w")

        # Label: From
        self.from_label = ctk.CTkLabel(self, text="From", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.from_label.grid(row=0, column=2, padx=10, pady=(10,10), sticky="w")

        # Label: To
        self.to_label = ctk.CTkLabel(self, text="To", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.to_label.grid(row=0, column=3, padx=10, pady=(10,10), sticky="w")

        # Label: Currency
        self.currency_label = ctk.CTkLabel(self, text="USD", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.currency_label.grid(row=0, column=4, padx=10, pady=(10,10), sticky="w")

        # Label: Date
        self.date_label = ctk.CTkLabel(self, text="19/05/2023", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.date_label.grid(row=0, column=5, padx=10, pady=(10,10), sticky="w")


class AccountInfoFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Label: "Holder"
        self.holder_label = ctk.CTkLabel(self, text="> Holder:", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.holder_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")

        # Label: Holder name
        self.holder_name_label = ctk.CTkLabel(self, text="Luca", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.holder_name_label.grid(row=0, column=1, padx=10, pady=(10,10), sticky="w")

        # Label: "Currency"
        self.currency_label = ctk.CTkLabel(self, text="> Currency: ", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.currency_label.grid(row=1, column=0, padx=10, pady=(10,10), sticky="w")

        # Label: Currency
        self.currency_tag_label = ctk.CTkLabel(self, text="EUR", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.currency_tag_label.grid(row=1, column=1, padx=10, pady=(10,10), sticky="w")

        # Label: "Rate"
        self.rate_label = ctk.CTkLabel(self, text="> Rate:", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.rate_label.grid(row=2, column=0, padx=10, pady=(10,10), sticky="w")

        # Label: Interest rate
        self.interest_rate_label = ctk.CTkLabel(self, text="2.0%", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.interest_rate_label.grid(row=2, column=1, padx=10, pady=(10,10), sticky="w")


class ExchangeFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Label: "Exchange"
        self.exchange_label = ctk.CTkLabel(self, text="Exchange:", fg_color="transparent", text_color="white", font=("tahoma", 22))
        self.exchange_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")

        # Options: "Exchange"
        self.exchange_option = ctk.CTkOptionMenu(self, values=["USD", "GBP"])
        self.exchange_option.grid(row=1, column=0, padx=10, pady=(10,10), sticky="w")