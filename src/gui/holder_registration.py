import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date


class HolderRegistrationWindow(tk.Tk):
    def __init__(self, bank):
        super().__init__()

        # geometry & positioning
        # self.width = 1000
        # self.height = 600
        # self.screen_width = self.winfo_screenwidth()
        # self.screen_height = self.winfo_screenheight()
        # self.x = (self.screen_width / 2) - (self.width / 2)
        # self.y = (self.screen_height / 2) - (self.height / 2)
        # self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")
        self.attributes("-topmost", True)


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

        # style
        self.btn_padx = 10
        self.btn_pady = 5

        # widgets
        self.holder_registration_label = tk.Label(self, text=self.holder_registration_label_text)
        self.holder_registration_label.grid(row=0, column=0)

        self.holder_name_label = tk.Label(self, text=self.holder_name_label_text)
        self.holder_name_label.grid(row=1, column=0)
        self.holder_name_entry = tk.Entry(self, width=30, borderwidth=5)
        self.holder_name_entry.grid(row=1, column=1)


        self.holder_surname_label = tk.Label(self, text=self.holder_surname_label_text)
        self.holder_surname_label.grid(row=2, column=0)
        self.holder_surname_entry = tk.Entry(self, width=30, borderwidth=5)
        self.holder_surname_entry.grid(row=2, column=1)


        self.holder_birth_date_label = tk.Label(self, text=self.holder_birth_date_label_text)
        self.holder_birth_date_label.grid(row=3, column=0)
        self.holder_birth_date_year_entry = tk.Entry(self, width=10, borderwidth=5)
        self.holder_birth_date_year_entry.grid(row=3, column=1)
        self.holder_birth_date_separator_label = tk.Label(self, text=self.holder_birth_date_separator_label_text)
        self.holder_birth_date_separator_label.grid(row=3, column=2)
        self.holder_birth_date_month_entry = tk.Entry(self, width=10, borderwidth=5)
        self.holder_birth_date_month_entry.grid(row=3, column=3)
        self.holder_birth_date_separator_label = tk.Label(self, text=self.holder_birth_date_separator_label_text)
        self.holder_birth_date_separator_label.grid(row=3, column=4)
        self.holder_birth_date_day_entry = tk.Entry(self, width=10, borderwidth=5)
        self.holder_birth_date_day_entry.grid(row=3, column=5)

        self.register_button = tk.Button(self, text=self.register_button_text, padx=self.btn_padx, pady=self.btn_pady, state="active", command=self.validate_registration).grid(row=4,column=6)


    def validate_registration(self) -> None:
        name = self.holder_name_entry.get()
        surname = self.holder_surname_entry.get()
        birth_date_year = self.holder_birth_date_year_entry.get()
        birth_date_month = self.holder_birth_date_month_entry.get()
        birth_date_day = self.holder_birth_date_day_entry.get()

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
        self.holder_name = name
        self.holder_surname = surname
        self.holder_birth_date = birth_date

        self.close()
        
    def show_error(self) -> None:
        # parent=self keeps the popup window in front
        messagebox.showerror("Error", "Input not correct", parent=self)
        
    def start(self):
        self.mainloop()

    def close(self):
        self.destroy()