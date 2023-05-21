import customtkinter as ctk
from holder import Holder

ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode("dark") # "system" (default), "dark", "light"



class TopUpWndow(ctk.CTkFrame):
    """
    Class which contains the account creation window
    """
    def __init__(self, master, holder: Holder, parent, **kwargs):
        super().__init__(master, **kwargs)

        self.width = 600
        self.height = 300
     

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)


        self.window = ctk.CTkToplevel(parent)
        
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1,2,3,4,5), weight=1)

        self.parent = parent

        # Title
        self.title_label = ctk.CTkLabel(self, text="Top Up", fg_color="transparent", text_color="white", font=("tahoma", 24))
        self.title_label.grid(row=0, column=0, padx=10, columnspan=2, pady=(10,10), sticky="ew")

        # Label: "Account from"
        self.account_from_label = ctk.CTkLabel(self, text="> Account to withdraw from: ", fg_color="transparent", text_color="white", font=("tahoma", 15))
        self.account_from_label.grid(row=1, column=0, padx=10, pady=(10,10), sticky="ew")
        # Option for account from
        self.account_from_option = ctk.CTkOptionMenu(self, values=[account for account in holder.connected_accounts])
        self.account_from_option.grid(row=1, column=1, padx=10, pady=(10,10), sticky="ew")

        # Label: "Account to"
        self.account_to_label = ctk.CTkLabel(self, text="> Account to top up:", fg_color="transparent", text_color="white", font=("tahoma", 15))
        self.account_to_label.grid(row=2, column=0, padx=10, pady=(10,10), sticky="ew")
        # Option for account to
        self.account_to_option = ctk.CTkOptionMenu(self, values=[account for account in holder.accounts])
        self.account_to_option.grid(row=2, column=1, padx=10, pady=(10,10), sticky="ew")
    
        # Label: "Amount"
        self.interest_rate_label = ctk.CTkLabel(self, text="> Enter the amount: ", fg_color="transparent", text_color="white", font=("tahoma", 15))
        self.interest_rate_label.grid(row=3, column=0, padx=10, pady=(10,10), sticky="w")
        # Entry for amount
        self.amount_entry = ctk.CTkEntry(self, width=300, height=20, text_color="white", font=("tahoma", 15), placeholder_text="Amount to top up")
        self.amount_entry.grid(row=3, column=1, padx=10, pady=(10,10), sticky="ew")

        # Error log lable
        self.error_label = ctk.CTkLabel(self, text="", fg_color="transparent", text_color="red", font=("tahoma", 15))
        self.error_label.grid(row=4, column=0, columnspan=2, padx=10, pady=(10,10), sticky="w")

        # Create account button
        self.button = ctk.CTkButton(self, width=40, height=40, text="Top up", text_color="black", font=("tahoma", 16), command=self.check_content)
        self.button.grid(row=5, column=1, padx=20, pady=20, sticky="ew")


    def check_content(self) -> float | None:
        account_from = self.account_from_option.get()
        account_to = self.account_to_option.get()
        amount = self.amount_entry.get()
        
        try:
            float(amount)
        except (ValueError):
            self.error_label.configure(text="Amount amount must be a number")
            return None
            
        if not amount:
            self.error_label.configure(text="Missing amount!")
        else:
            self.parent.update_balance(amount)
            self.kill_window()
    
        return None


    def kill_window(self):
        self.destroy()
        