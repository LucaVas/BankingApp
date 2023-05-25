import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import bcrypt
from datetime import date, datetime



class LoginWindow(ctk.CTk):
    def __init__(self, bank, temp_db) -> None:
        super().__init__()

        self.db = temp_db

        self.width = 800
        self.height = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")
        self.attributes("-topmost", True)

        # grid layout
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)


        # holder information
        self.title(bank.name)
        self.first = ""
        self.last = ""
        self.id: int
        self.password: bytes
        self.last_access: date

        # widgets variables
        self.login_label_text = "Log-in"
        self.name_label_text = "> Enter your name:"
        self.surname_label_text = "> Enter your surname:"
        self.password_label_text = "> Enter your password:"
        self.login_button_text = "Log in"


        # widgets
        # ============ Top frame with main label ============ #
        self.login_frame = ctk.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, columnspan=3, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.login_frame.grid_rowconfigure(0, weight=1)
        self.login_label = ctk.CTkLabel(self.login_frame, text=self.login_label_text, font=ctk.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=10, pady=(10,10))

        # ============ Main frame with entries ============ #
        self.entries_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.entries_frame.grid(row=1, column=0, columnspan=3, padx=(10, 10), pady=(0, 10), sticky="nsew")
        self.entries_frame.grid_rowconfigure((0,1,2), weight=1)
        self.entries_frame.grid_columnconfigure((0,1,2), weight=1)

        self.name_label = ctk.CTkLabel(self.entries_frame, text=self.name_label_text, font=ctk.CTkFont(size=15, weight="normal"))
        self.name_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")
        self.name_entry = ctk.CTkEntry(self.entries_frame)
        self.name_entry.grid(row=0, column=1, padx=10, pady=(10,10), sticky="ew")

        self.surname_label = ctk.CTkLabel(self.entries_frame, text=self.surname_label_text, font=ctk.CTkFont(size=15, weight="normal"))
        self.surname_label.grid(row=1, column=0, padx=10, pady=(10,10), sticky="w")
        self.surname_entry = ctk.CTkEntry(self.entries_frame)
        self.surname_entry.grid(row=1, column=1, padx=10, pady=(10,10), sticky="ew")

        self.password_label = ctk.CTkLabel(self.entries_frame, text=self.password_label_text, font=ctk.CTkFont(size=15, weight="normal"))
        self.password_label.grid(row=2, column=0, padx=10, pady=(10,10), sticky="w")
        self.password_entry = ctk.CTkEntry(self.entries_frame)
        self.password_entry.grid(row=2, column=1, padx=10, pady=(10,10), sticky="ew")

        # ============ Bottom row with button ============ #
        self.login_button = ctk.CTkButton(self, text=self.login_button_text, state="active", width=100, height=40, text_color="black", font=("tahoma", 16), command=self.validate_login_information).grid(row=2, column=2, padx=10, pady=(10,10), sticky="ew")


    def validate_login_information(self) -> None:
        self.first = self.name_entry.get()
        self.last = self.surname_entry.get()
        self.password = bytes(self.password_entry.get(), 'utf-8')

        for holder in self.db['holders']:
            hashed = bytes(holder["password"], 'utf-8')
            if self.first == holder["first"] and self.last == holder["last"] and bcrypt.checkpw(self.password, hashed):
                self.id = holder["id"]
                self.last_access = datetime.now()
                self.close()
                return
            else:
                continue  

        self.show_error()
        
    def show_error(self) -> None:
        # parent=self keeps the popup window in front
        messagebox.showerror("Error", "User not found", parent=self)
        
    def start(self):
        self.mainloop()

    def close(self):
        self.destroy()
