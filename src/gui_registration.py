import customtkinter as ctk
import bcrypt

ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode("dark") # "system" (default), "dark", "light"


class RegistrationGui(ctk.CTk):
    """
    Main class where I run my application
    """

    holder_info: list[str] = []
    password: list[bytes] = []

    def __init__(self):
        super().__init__()

        self.title("Luca's bank")
        self.width = "500"
        self.height = "300"
        self.geometry(f"{self.width}x{self.height}")


        
class WelcomeWindow(RegistrationGui):
    """
    Class which contains my first welcome window
    """
    def __init__(self):
        super().__init__()

        self.grid_columnconfigure((0,1), weight=2)
        self.grid_rowconfigure((0,1), weight=1)

        # Title
        self.welcome_label = ctk.CTkLabel(self, text="Welcome to Luca's Bank", fg_color="transparent", text_color="white", font=("tahoma", 24))
        self.welcome_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")

        # Description
        self.textbox = ctk.CTkTextbox(master=self, width=200, padx=10, fg_color="transparent", corner_radius=0, text_color="white", font=("tahoma", 15))
        self.textbox.grid(row=1, column=0, sticky="nsew")
        self.textbox.insert("0.1", "> Open an account\n\n")
        self.textbox.insert("0.2", "> Add money\n\n")
        self.textbox.insert("0.3", "> Transfer between accounts\n\n")
        self.textbox.insert("0.4", "> Currency exchange\n\n")

        # Start button
        self.start_button = ctk.CTkButton(self, width=40, height=40, text="Start now", text_color="black", font=("tahoma", 16), command=self.button_callback)
        self.start_button.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

    def button_callback(self):
        holder_registration_window = HolderRegistrationWindow()
        self.destroy()
        holder_registration_window.mainloop()
        

        


class HolderRegistrationWindow(RegistrationGui):
    """
    Class which contains the window of holder registration
    """
    def __init__(self) -> None:
        super().__init__()

        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1,2,3,4,5), weight=1)


        # Title: Registration
        self.welcome_label = ctk.CTkLabel(self, text="Registration", fg_color="transparent", text_color="white", font=("tahoma", 24))
        self.welcome_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")

        # Registration entries

        self.first_name_entry = ctk.CTkEntry(self, width=300, height=20, text_color="white", font=("tahoma", 15), placeholder_text="Your name")
        self.first_name_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

        self.last_name_entry = ctk.CTkEntry(self, width=300, height=20, text_color="white", font=("tahoma", 15), placeholder_text="Your surname")
        self.last_name_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

        self.birth_date_entry = ctk.CTkEntry(self, width=300, height=20, text_color="white", font=("tahoma", 15), placeholder_text="Your date of birth")
        self.birth_date_entry.grid(row=3, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

        # Error log lable
        self.error_label = ctk.CTkLabel(self, text="", fg_color="transparent", text_color="red", font=("tahoma", 15))
        self.error_label.grid(row=4, column=0, padx=10, pady=(10,10), sticky="w")

        # Continue button

        self.start_button = ctk.CTkButton(self, width=40, height=40, text="Continue", text_color="black", font=("tahoma", 16), command=self.check_content)
        self.start_button.grid(row=5, column=1, padx=20, pady=20, sticky="ew")


    def check_content(self) -> None:
        
        first = self.first_name_entry.get()
        last = self.last_name_entry.get()
        birth_date = self.birth_date_entry.get()

        if not first or not last or not birth_date:
            self.error_label.configure(text="Some fields are empty!")
        else:
            RegistrationGui.holder_info = [el for el in [first, last, birth_date]]
            self.next_window()
        

    def next_window(self) -> None:

        password_registration_window = PasswordRegistrationWindow()
        self.destroy()
        password_registration_window.mainloop()   
        



class PasswordRegistrationWindow(RegistrationGui):
    """
    Class which contains the window of holder registration
    """
    def __init__(self):
        super().__init__()

        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1,2,3,4), weight=1)

        # Title: Registration
        self.welcome_label = ctk.CTkLabel(self, text="Registration", fg_color="transparent", text_color="white", font=("tahoma", 24))
        self.welcome_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")

        # Registration entries

        self.password_entry = ctk.CTkEntry(self, width=300, height=20, text_color="white", font=("tahoma", 15), placeholder_text="Enter your password")
        self.password_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

        self.repeated_password_entry = ctk.CTkEntry(self, width=300, height=20, text_color="white", font=("tahoma", 15), placeholder_text="Repeat your password")
        self.repeated_password_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

        # Label: Disclaimer
        self.welcome_label = ctk.CTkLabel(self, text="Attention: if you loose your password, you will not be able to access.", fg_color="transparent", text_color="white", font=("tahoma", 12))
        self.welcome_label.grid(row=3, column=0, columnspan=2, padx=10, pady=(10,10), sticky="w")

        # Continue button

        self.start_button = ctk.CTkButton(self, width=50, height=40, text="Confirm registration", text_color="black", font=("tahoma", 16), command=self.check_password)
        self.start_button.grid(row=4, column=1, padx=20, pady=20, sticky="ew")


    def hash_password(self, password: bytes) -> bytes:
        return bcrypt.hashpw(password, bcrypt.gensalt())

    def check_password(self) -> None:

        password = self.password_entry.get()
        repeated_password = self.repeated_password_entry.get()

        if not password or not repeated_password or password != repeated_password:
            self.welcome_label.configure(text="The two passwords don't match!", text_color="red")
        elif password == repeated_password:
            hashed = self.hash_password(bytes(password, 'utf-8'))
            RegistrationGui.password.append(hashed)
            self.button_callback()
        else:
            raise ValueError

    def button_callback(self):
        self.destroy()
        

