import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime, date


class HolderRegistrationWindow(ctk.CTk):
    def __init__(self, bank):
        super().__init__()

        # geometry & positioning
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
        self.holder_name = ""
        self.holder_surname = ""
        self.holder_birth_date = ""

        # widgets variables
        self.holder_registration_label_text = "Holder registration"
        self.holder_name_label_text = "> Enter your name:"
        self.holder_surname_label_text = "> Enter your surname:"
        self.holder_birth_date_label_text = "> Enter your birth date (YYYY/MM/DD):"
        self.holder_birth_date_separator_label_text = " / "
        self.register_button_text = "Register holder"


        # widgets
        # ============ Top frame with main label ============ #
        self.holder_registration_frame = ctk.CTkFrame(self, corner_radius=0)
        self.holder_registration_frame.grid(row=0, column=0, columnspan=4, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.holder_registration_frame.grid_rowconfigure(0, weight=1)
        self.holder_registration_label = ctk.CTkLabel(self.holder_registration_frame, text=self.holder_registration_label_text, font=ctk.CTkFont(size=20, weight="normal"))
        self.holder_registration_label.grid(row=0, column=0, padx=10, pady=(10,10))

        # ============ Main frame with entries ============ #
        self.entries_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.entries_frame.grid(row=1, column=0, columnspan=4, padx=(10, 10), pady=(0, 10), sticky="nsew")
        self.entries_frame.grid_rowconfigure((0,1,2), weight=1)
        self.entries_frame.grid_columnconfigure((0,1,2,3,4,5), weight=1)


        self.holder_name_label = ctk.CTkLabel(self.entries_frame, text=self.holder_name_label_text, font=ctk.CTkFont(size=15, weight="normal"))
        self.holder_name_label.grid(row=0, column=0, padx=10, pady=(10,10), sticky="w")
        self.holder_name_entry = ctk.CTkEntry(self.entries_frame)
        self.holder_name_entry.grid(row=0, column=1, padx=10, pady=(10,10))

        self.holder_surname_label = ctk.CTkLabel(self.entries_frame, text=self.holder_surname_label_text, font=ctk.CTkFont(size=15, weight="normal"))
        self.holder_surname_label.grid(row=1, column=0, padx=10, pady=(10,10), sticky="w")
        self.holder_surname_entry = ctk.CTkEntry(self.entries_frame)
        self.holder_surname_entry.grid(row=1, column=1, padx=10, pady=(10,10))


        self.holder_birth_date_label = ctk.CTkLabel(self.entries_frame, text=self.holder_birth_date_label_text, font=ctk.CTkFont(size=15, weight="normal"))
        self.holder_birth_date_label.grid(row=2, column=0, padx=10, pady=(10,10), sticky="w")
        self.holder_birth_date_year_entry = ctk.CTkEntry(self.entries_frame)
        self.holder_birth_date_year_entry.grid(row=2, column=1, padx=10, pady=(10,10))
        self.holder_birth_date_separator_label = ctk.CTkLabel(self.entries_frame, text=self.holder_birth_date_separator_label_text, font=ctk.CTkFont(size=15, weight="normal"))
        self.holder_birth_date_separator_label.grid(row=2, column=2, padx=10, pady=(10,10))
        self.holder_birth_date_month_entry = ctk.CTkEntry(self.entries_frame)
        self.holder_birth_date_month_entry.grid(row=2, column=3, padx=10, pady=(10,10))
        self.holder_birth_date_separator_label = ctk.CTkLabel(self.entries_frame, text=self.holder_birth_date_separator_label_text, font=ctk.CTkFont(size=15, weight="normal"))
        self.holder_birth_date_separator_label.grid(row=2, column=4, padx=10, pady=(10,10))
        self.holder_birth_date_day_entry = ctk.CTkEntry(self.entries_frame)
        self.holder_birth_date_day_entry.grid(row=2, column=5, padx=10, pady=(10,10))

        # ============ Bottom row with button ============ #
        self.register_button = ctk.CTkButton(self, text=self.register_button_text, state="active", width=40, height=40, text_color="black", font=("tahoma", 16), command=self.validate_registration).grid(row=5, column=3, padx=10, pady=(10,10), sticky="ew")


    def validate_registration(self) -> None:
        name = self.holder_name_entry.get().strip()
        surname = self.holder_surname_entry.get().strip()
        birth_date_year = self.holder_birth_date_year_entry.get().strip()
        birth_date_month = self.holder_birth_date_month_entry.get().strip()
        birth_date_day = self.holder_birth_date_day_entry.get().strip()

        if not name or not surname:
            self.show_error()
        elif not birth_date_year or not birth_date_month or not birth_date_day:
            self.show_error()
        else:        
            if self.validate_birth_date(birth_date_year, birth_date_month, birth_date_day) is False:
                return
            else:
                full_birth_date = f"{birth_date_year}{birth_date_month}{birth_date_day}"
                formatted_birth_date = datetime.strptime(full_birth_date, "%Y%m%d").date()
                self.register_holder(name, surname, formatted_birth_date)
            
    
    def validate_birth_date(self, year: str, month: str, day: str) -> bool:
        if len(year) != 4:
            messagebox.showerror("Error", "Incorrect date format", parent=self)
            return False
        if len(month) < 1 or len(month) > 2 or len(day) < 1 or len(day) > 2:
            messagebox.showerror("Error", "Incorrect date format", parent=self)
            return False
        
        try:
            y = int(year)
            m = int(month)
            d = int(day)
        except (ValueError):
            messagebox.showerror("Error", "Input not correct (1)", parent=self)
            return False
        
        year_now = datetime.now().year
    
        if y > int(year_now):
            messagebox.showerror("Error", "Incorrect year format", parent=self)
            return False
        elif m < 0 or m > 12:
            messagebox.showerror("Error", "Incorrect month format", parent=self)
            return False
        elif d < 0 or d > 31:
            messagebox.showerror("Error", "Incorrect day format", parent=self)
            return False
        
        try:
            f_date = f"{year}-{month}-{day}"
            date.fromisoformat(f_date)
        except (ValueError):
            messagebox.showerror("Error", "Input not correct (2)", parent=self)
            return False
        
        return True
        
        
    def register_holder(self, name:str, surname:str, birth_date:date) -> None:
        self.holder_name = name.capitalize()
        self.holder_surname = surname.capitalize()
        self.holder_birth_date = birth_date

        self.close()
        
    def show_error(self) -> None:
        # parent=self keeps the popup window in front
        messagebox.showerror("Error", "Input not correct", parent=self)
        
    def start(self):
        self.mainloop()

    def close(self):
        self.destroy()