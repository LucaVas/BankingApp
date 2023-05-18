import customtkinter as ctk

ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode("dark") # "system" (default), "dark", "light"


# Presentation window
        
class WelcomeWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Luca's bank")
        self.width = "500"
        self.height = "400"

        self.geometry(f"{self.width}x{self.height}")
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
        self.start_button.grid(row=1, column=1, padx=20, pady=20, sticky="ew", columnspan=2)

    def button_callback(self):
        print("button clicked")

        


    
        
    
        
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Luca's bank")
        self.width = "400"
        self.height = "500"


        self.geometry(f"{self.width}x{self.height}")
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((3), weight=1)


        # self.button = ctk.CTkButton(self, text="my button", command=self.button_callback)
        # self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        # self.checkbox_frame = CheckboxFrame(self)
        # self.checkbox_frame.grid(row=1, column=0, padx=10, pady=(10,10), sticky="nsw")

        # self.entry_frame = HolderInformationFrame(self)
        # self.entry_frame.grid(row=2, column=0, padx=10, pady=(10,10))



class HolderInformationFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.entry = ctk.CTkEntry(self, width=300, height=10, text_color="white", font=("tahoma", 20), placeholder_text="Name")
        self.entry.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")
        
        self.entry = ctk.CTkEntry(self, width=300, height=10, text_color="white", font=("tahoma", 20), placeholder_text="Surname")
        self.entry.grid(row=1, column=0, padx=10, pady=(10,10), sticky="w")

        self.entry = ctk.CTkEntry(self, width=300, height=10, text_color="white", font=("tahoma", 20), placeholder_text="Date of birth")
        self.entry.grid(row=2, column=0, padx=10, pady=(10,10), sticky="w")
        




class CheckboxFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.checkbox_1 = ctk.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = ctk.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_3 = ctk.CTkCheckBox(self, text="checkbox 3")
        self.checkbox_3.grid(row=2, column=0, padx=10, pady=(10,0), sticky="w")