import customtkinter as ctk

ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode("dark") # "system" (default), "dark", "light"

class AccountGui(ctk.CTk):
    """
    Main class where I run my account creation section
    """

    account_info: list[str] = []

    def __init__(self):
        super().__init__()

        self.title("Luca's bank")
        self.width = "500"
        self.height = "300"
        self.geometry(f"{self.width}x{self.height}")



class AccountInformation(AccountGui):
    """
    Class which contains the account creation window
    """
    def __init__(self):
        super().__init__()

        self.grid_columnconfigure((0,1), weight=2)
        self.grid_rowconfigure((0,1,2,3,4,5), weight=1)

        # Title
        self.title_label = ctk.CTkLabel(self, text="Account creation", fg_color="transparent", text_color="white", font=("tahoma", 24))
        self.title_label.grid(row=0, column=0, padx=10, columnspan=2, pady=(10,10), sticky="w")

        # Label for currency choice
        self.currency_label = ctk.CTkLabel(self, text="Choose the currency", fg_color="transparent", text_color="white", font=("tahoma", 15))
        self.currency_label.grid(row=1, column=0, padx=10, pady=(10,10), sticky="w")
        # Option for currency choice
        self.currency_option = ctk.CTkOptionMenu(self, values=["EUR", "USD"])
        self.currency_option.grid(row=1, column=1, padx=10, pady=(10,10), sticky="w")

        # Label for account balance entry
        self.balance_label = ctk.CTkLabel(self, text="Starting balance", fg_color="transparent", text_color="white", font=("tahoma", 15))
        self.balance_label.grid(row=2, column=0, padx=10, pady=(10,10), sticky="w")

        # Account balance entry
        self.balance_entry = ctk.CTkEntry(self, width=300, height=20, text_color="white", font=("tahoma", 15), placeholder_text="Your initial balance")
        self.balance_entry.grid(row=2, column=1, padx=10, pady=(10,10), sticky="ew")
    
        # Label for interest rate choice
        self.interest_rate_label = ctk.CTkLabel(self, text="Choose interest rate", fg_color="transparent", text_color="white", font=("tahoma", 15))
        self.interest_rate_label.grid(row=3, column=0, padx=10, pady=(10,10), sticky="w")
        # Option for interest rate choice
        self.interest_option = ctk.CTkOptionMenu(self, values=["1.8", "2.0"])
        self.interest_option.grid(row=3, column=1, padx=10, pady=(10,10), sticky="w")

        # Error log lable
        self.error_label = ctk.CTkLabel(self, text="", fg_color="transparent", text_color="red", font=("tahoma", 15))
        self.error_label.grid(row=4, column=0, columnspan=2, padx=10, pady=(10,10), sticky="w")

        # Create account button
        self.button = ctk.CTkButton(self, width=40, height=40, text="Create account", text_color="black", font=("tahoma", 16), command=self.check_content)
        self.button.grid(row=5, column=1, padx=20, pady=20, sticky="ew")


    def check_content(self):
        currency = self.currency_option.get()
        balance_amount = self.balance_entry.get()
        interest_rate = float(self.interest_option.get())
        
        try:
            float(balance_amount)
        except ValueError:
            self.error_label.configure(text="Balance amount must be a number")
            return
            
        if not balance_amount:
            self.error_label.configure(text="Missing balance amount!")
        else:
            AccountGui.account_info = [el for el in [balance_amount, interest_rate, currency]]  
            self.kill_window()

    def kill_window(self):
        self.destroy()
        