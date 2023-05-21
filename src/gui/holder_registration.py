import tkinter as tk
from tkinter import messagebox


class HolderRegistrationWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # geometry & positioning
        self.width = 1000
        self.height = 600
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")
        self.attributes("-topmost", True)


        # holder information
        self.title("Bank99")
        self.holder_name = ""
        self.holder_surname = ""
        self.holder_birth_date = ""

        # widgets variables
        self.holder_registration_label_text = "Holder registration"
        self.holder_name_label_text = "> Enter your name:"
        self.holder_surname_label_text = "> Enter your surname:"
        self.holder_birth_date_label_text = "> Enter your birth date:"
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
        self.holder_birth_date_entry = tk.Entry(self, width=30, borderwidth=5)
        self.holder_birth_date_entry.grid(row=3, column=1)

        self.register_button = tk.Button(self, text=self.register_button_text, padx=self.btn_padx, pady=self.btn_pady, state="active", command=self.validate_registration).grid(row=4,column=2)


    def validate_registration(self) -> None:
        name = self.holder_name_entry.get()
        surname = self.holder_surname_entry.get()
        birth_date = self.holder_birth_date_entry.get()

        if not name or not surname or not birth_date:
            self.show_error()
        else:        
            self.register(name, surname, birth_date)
    
    def register(self, name:str, surname:str, birth_date:str) -> None:
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


if __name__ == "__main__":
    app = HolderRegistrationWindow()
    app.start()