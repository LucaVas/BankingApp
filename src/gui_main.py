import customtkinter as ctk
from bank import Bank
from holder import Holder
from account import Account
from currency import Currency

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
        self.width = 1200
        self.height = 700
     

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)


        self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")


class MainWindow(MainGui):
    """
    Class which contains the main window of my application
    """
    def __init__(self, holder: Holder, account: Account, bank: Bank) -> None:
        super().__init__()

        self.grid_columnconfigure((0,1,2,3), weight=1)
        self.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)


        """ Left side """
        # Label: "Your Account"
        self.title_label = ctk.CTkLabel(self, text="Your Account", fg_color="transparent", text_color="white", font=("tahoma", 24))
        self.title_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")

        # Button: "Top-Up"
        self.button_top_up = ctk.CTkButton(self, width=40, height=40, text="Top-Up", text_color="black", font=("tahoma", 16), command=self.top_up)
        self.button_top_up.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        # Button: "Transfer"
        self.button_transfer = ctk.CTkButton(self, width=40, height=40, text="Transfer", text_color="black", font=("tahoma", 16), command=self.transfer)
        self.button_transfer.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        # Label: "Appearance mode"
        self.appearence_label = ctk.CTkLabel(self, text="> Appearence mode", fg_color="transparent", text_color="white", font=("tahoma", 15))
        self.appearence_label.grid(row=5, column=0, padx=10, pady=(10,10), sticky="w")

        # Options: "Appearence Mode"
        self.appearance_option = ctk.CTkOptionMenu(self, values=["Light", "Dark"])
        self.appearance_option.grid(row=6, column=0, padx=10, pady=(10,10), sticky="w")


        """ Center """
        self.balance_frame = BalanceFrame(self, account.balance, account.currency)
        self.balance_frame.grid(row=0, column=1, columnspan=2, padx=20, pady=20, sticky="nsew")

        self.currency_frame = CurrencyFrame(self, account.currency)
        self.currency_frame.grid(row=1, column=2, padx=20, pady=20, sticky="nsew")

        self.transfers_list_frame = TransfersListFrame(master=self)
        self.transfers_list_frame.grid(row=2, column=1, columnspan=2, rowspan=4, padx=20, pady=20, sticky="nsew")

        # Messages log lable
        self.message_label = ctk.CTkLabel(self, text="Message", text_color="red", font=("tahoma", 15))
        self.message_label.grid(row=6, column=1, columnspan=2, padx=10, pady=(10,10), sticky="w") 


        """ Right side """
        self.account_info_frame = AccountInfoFrame(self, holder.first_name, account.currency, account.interest_rate)
        self.account_info_frame.grid(row=0, column=3, rowspan=2, padx=20, pady=20, sticky="nsew")
    
        self.exchange_frame = ExchangeFrame(self, self.currency_frame)
        self.exchange_frame.grid(row=2, column=3, rowspan=2, padx=20, pady=20, sticky="nsew")

        self.bank_info_frame = BankInfoFrame(self, bank)
        self.bank_info_frame.grid(row=4, column=3, rowspan=2, padx=20, pady=20, sticky="nsew")

        # Button: "Log-out"
        self.button_log_out = ctk.CTkButton(self, width=40, height=40, text="Log out", text_color="black", font=("tahoma", 18), command=self.log_out)
        self.button_log_out.grid(row=6, column=3, padx=20, pady=20, sticky="ew")


  




    def top_up(self):
        pass
        
    def transfer(self):
        pass

    def log_out(self):
        self.kill_window()

    def kill_window(self):
        self.destroy()



class BalanceFrame(ctk.CTkFrame):
    def __init__(self, master, balance: float, currency: str, **kwargs):
        super().__init__(master, **kwargs)

        # Label: "Balance"
        self.balance_label = ctk.CTkLabel(self, text="> Balance", fg_color="transparent", text_color="white", font=("tahoma", 24))
        self.balance_label.grid(row=0, column=0, padx=(10, 40), pady=(10,10), sticky="w")

        # Label: Amount
        self.amount_label = ctk.CTkLabel(self, text=str(balance), fg_color="transparent", text_color="white", font=("tahoma", 27))
        self.amount_label.grid(row=0, column=3, padx=(50,10), pady=(10,10), sticky="w")

        # Label: Currency

        self.currency_label = ctk.CTkLabel(self, text=currency, fg_color="transparent", text_color="white", font=("tahoma", 27))
        self.currency_label.grid(row=0, column=4, padx=10, pady=(10,10), sticky="w")


class CurrencyFrame(ctk.CTkFrame):
    def __init__(self, master, currency: str, **kwargs):
        super().__init__(master, **kwargs)

        # Label: Amount
        self.amount_label = ctk.CTkLabel(self, text="1940", fg_color="transparent", text_color="white", font=("tahoma", 27))
        self.amount_label.grid(row=0, column=1, padx=10, pady=(10,10), sticky="w")

        # Label: Currency
        self.currency_label = ctk.CTkLabel(self, text=currency, fg_color="transparent", text_color="white", font=("tahoma", 27))
        self.currency_label.grid(row=0, column=2, padx=10, pady=(10,10), sticky="w")

    def set_currency_label(self, value: str) -> None:
        self.currency_label.configure(text=value)


class TransfersListFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        self.grid_rowconfigure((0), weight=1)

        self.header = TransfersListRowFrame(self, "Action", "Amount", "From", "To", "Currency", "Date")
        self.header.grid(row=0, column=0, columnspan=6, padx=(0,10), pady=20, sticky="ew")

        self.row = TransfersListRowFrame(self, "Transfer", "100", "Luca", "Max", "EUR", "20/05/2023")
        self.row.grid(row=TransfersListRowFrame.rows, column=0, columnspan=6, padx=0, pady=20, sticky="ew")

        self.row = TransfersListRowFrame(self, "Top-Up", "20", "Luca", "Luca", "EUR", "04/05/2023")
        self.row.grid(row=TransfersListRowFrame.rows, column=0, columnspan=6, padx=0, pady=20, sticky="ew")

        self.row = TransfersListRowFrame(self, "Top-Up", "34", "Luca", "Luca", "EUR", "03/05/2023")
        self.row.grid(row=TransfersListRowFrame.rows, column=0, columnspan=6, padx=0, pady=20, sticky="ew")

        self.row = TransfersListRowFrame(self, "Transfer", "732", "Judita", "Luca", "EUR", "17/04/2023")
        self.row.grid(row=TransfersListRowFrame.rows, column=0, columnspan=6, padx=0, pady=20, sticky="ew")


class TransfersListRowFrame(ctk.CTkFrame):

    rows=-1

    def __init__(self, master, action: str, amount: str, acc_from: str, acc_to: str, currency: str, date: str, **kwargs):
        super().__init__(master, **kwargs)

        TransfersListRowFrame.rows += 1

        self.action = action 
        self.amount = amount
        self.acc_from = acc_from
        self.acc_to = acc_to
        self.currency = currency
        self.date = date

        self.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        self.grid_rowconfigure((0), weight=0)

        # Label: Action
        self.action_label = ctk.CTkLabel(self, text=action, fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.action_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="ew")

        # Label: Amount
        self.amount_label = ctk.CTkLabel(self, text=amount, fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.amount_label.grid(row=0, column=1, padx=10, pady=(10,10), sticky="ew")

        # Label: From
        self.from_label = ctk.CTkLabel(self, text=acc_from, fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.from_label.grid(row=0, column=2, padx=10, pady=(10,10), sticky="ew")

        # Label: To
        self.to_label = ctk.CTkLabel(self, text=acc_to, fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.to_label.grid(row=0, column=3, padx=10, pady=(10,10), sticky="ew")

        # Label: Currency
        self.currency_label = ctk.CTkLabel(self, text=currency, fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.currency_label.grid(row=0, column=4, padx=10, pady=(10,10), sticky="ew")

        # Label: Date
        self.date_label = ctk.CTkLabel(self, text=date, fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.date_label.grid(row=0, column=5, padx=10, pady=(10,10), sticky="ew")


 
class AccountInfoFrame(ctk.CTkFrame):
    def __init__(self, master, holder_name: str, account_currency: str, account_rate: float, **kwargs):
        super().__init__(master, **kwargs)

        # Label: "Holder"
        self.holder_label = ctk.CTkLabel(self, text="> Holder:", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.holder_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")

        # Label: Holder name
        self.holder_name_label = ctk.CTkLabel(self, text=holder_name, fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.holder_name_label.grid(row=0, column=1, padx=10, pady=(10,10), sticky="w")

        # Label: "Currency"
        self.currency_label = ctk.CTkLabel(self, text="> Currency: ", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.currency_label.grid(row=1, column=0, padx=10, pady=(10,10), sticky="w")

        # Label: Currency
        self.currency_tag_label = ctk.CTkLabel(self, text=account_currency, fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.currency_tag_label.grid(row=1, column=1, padx=10, pady=(10,10), sticky="w")

        # Label: "Rate"
        self.rate_label = ctk.CTkLabel(self, text="> Rate:", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.rate_label.grid(row=2, column=0, padx=10, pady=(10,10), sticky="w")

        # Label: Interest rate
        self.interest_rate_label = ctk.CTkLabel(self, text=f"{account_rate:.2f}%", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.interest_rate_label.grid(row=2, column=1, padx=10, pady=(10,10), sticky="w")


class ExchangeFrame(ctk.CTkFrame):
    def __init__(self, master, currency_frame: CurrencyFrame, **kwargs):
        super().__init__(master, **kwargs)

        self.currency_frame = currency_frame

        # Label: "Exchange"
        self.exchange_label = ctk.CTkLabel(self, text="Exchange:", fg_color="transparent", text_color="white", font=("tahoma", 22))
        self.exchange_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")

        # Options: "Exchange"
        self.exchange_option = ctk.CTkOptionMenu(self, values=[cur for cur in list(Currency().__dict__.keys())], command=self.get_choice)
        self.exchange_option.grid(row=1, column=0, padx=10, pady=(10,10), sticky="w")

    def get_choice(self, choice) -> None:
        self.currency_frame.set_currency_label(choice)
        return None



class BankInfoFrame(ctk.CTkFrame):
    def __init__(self, master, bank: Bank, **kwargs) -> None:
        super().__init__(master, **kwargs)

        # Label: "Bank shares"
        self.bank_shares_label = ctk.CTkLabel(self, text="> Bank shares:", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.bank_shares_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")

        # Label: Bank shares amount
        self.shares_amount_label = ctk.CTkLabel(self, text=f"{bank.shares_amount}", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.shares_amount_label.grid(row=0, column=1, padx=10, pady=(10,10), sticky="w")

        # Label: Price per share
        self.price_per_share_label = ctk.CTkLabel(self, text="> PPS:", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.price_per_share_label.grid(row=1, column=0, padx=10, pady=(10,10), sticky="w")

        # Label: Price
        self.share_price_label = ctk.CTkLabel(self, text=f"{bank.share_price}", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.share_price_label.grid(row=1, column=1, padx=10, pady=(10,10), sticky="w")

        # Label: "Shares increase"
        self.shares_increase_label = ctk.CTkLabel(self, text="> Shares increase: ", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.shares_increase_label.grid(row=2, column=0, padx=10, pady=(10,10), sticky="w")

        # Label: Shares delta
        self.shares_delta_label = ctk.CTkLabel(self, text=f"{bank.shares_delta}", fg_color="transparent", text_color="white", font=("tahoma", 18))
        self.shares_delta_label.grid(row=2, column=1, padx=10, pady=(10,10), sticky="w")
