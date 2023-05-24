import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import bcrypt



class PasswordRegistrationWindow(ctk.CTk):
    def __init__(self, bank):
        super().__init__()

        self.width = 800
        self.height = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")
        self.attributes("-topmost", True)

        # grid layout
        self.grid_columnconfigure((0, 1, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)


        # holder information
        self.title(bank.name)
        self.password = ""

        # widgets variables
        self.password_registration_label_text = "Password registration"
        self.password_label_text = "> Enter your password:"
        self.repeat_password_label_text = "> Repeat your password:"
        self.register_password_button_text = "Save password"

        # style
        self.btn_padx = 10
        self.btn_pady = 5

        # widgets
        # ============ Top frame with main label ============ #
        self.password_registration_frame = ctk.CTkFrame(self, corner_radius=0)
        self.password_registration_frame.grid(row=0, column=0, columnspan=4, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.password_registration_frame.grid_rowconfigure(0, weight=1)
        self.password_registration_label = ctk.CTkLabel(self.password_registration_frame, text=self.password_registration_label_text, font=ctk.CTkFont(size=20, weight="normal"))
        self.password_registration_label.grid(row=0, column=0, padx=10, pady=(10,10))

        # ============ Main frame with entries ============ #
        self.entries_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.entries_frame.grid(row=1, column=0, columnspan=3, padx=(10, 10), pady=(0, 10), sticky="nsew")
        self.entries_frame.grid_rowconfigure((0,1), weight=1)
        self.entries_frame.grid_columnconfigure((0,1,2), weight=1)

        self.password_label = ctk.CTkLabel(self.entries_frame, text=self.password_label_text, font=ctk.CTkFont(size=15, weight="normal"))
        self.password_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")
        self.password_entry = ctk.CTkEntry(self.entries_frame)
        self.password_entry.grid(row=0, column=1, padx=10, pady=(10,10))


        self.repeat_password_label = ctk.CTkLabel(self.entries_frame, text=self.repeat_password_label_text, font=ctk.CTkFont(size=15, weight="normal"))
        self.repeat_password_label.grid(row=1, column=0, padx=10, pady=(10,10), sticky="w")
        self.repeat_password_entry = ctk.CTkEntry(self.entries_frame)
        self.repeat_password_entry.grid(row=1, column=1, padx=10, pady=(10,10))


        self.message_label = ctk.CTkLabel(self, text="")
        self.message_label.grid(row=2, column=0, columnspan=3)

        # ============ Bottom row with button ============ #
        self.register_password_button = ctk.CTkButton(self, text=self.register_password_button_text, state="active", width=40, height=40, text_color="black", font=("tahoma", 16), command=self.validate_password_registration).grid(row=3, column=3, padx=10, pady=(10,10), sticky="ew")


    def validate_password_registration(self) -> None:
        password = self.password_entry.get()
        repeated_password = self.repeat_password_entry.get()

        if not password or not repeated_password:
            self.show_error()
        elif password != repeated_password:
            self.show_error()
        else:        
            hashed = self.hash_password(bytes(password, 'utf-8'))
            self.register_password(hashed)
    
    def hash_password(self, password: bytes) -> bytes:
        return bcrypt.hashpw(password, bcrypt.gensalt())
    
    def register_password(self, password: bytes) -> None:
        self.password = password

        self.close()
        
        
    def show_error(self) -> None:
        # parent=self keeps the popup window in front
        messagebox.showerror("Error", "Input not correct", parent=self)
        
    def start(self):
        self.mainloop()

    def close(self):
        self.destroy()
