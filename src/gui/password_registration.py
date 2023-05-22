import tkinter as tk
from tkinter import messagebox
import bcrypt


class PasswordRegistrationWindow(tk.Tk):
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
        self.password_registration_label = tk.Label(self, text=self.password_registration_label_text)
        self.password_registration_label.grid(row=0, column=0)

        self.password_label = tk.Label(self, text=self.password_label_text)
        self.password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(self, width=30, borderwidth=5)
        self.password_entry.grid(row=1, column=1)


        self.repeat_password_label = tk.Label(self, text=self.repeat_password_label_text)
        self.repeat_password_label.grid(row=2, column=0)
        self.repeat_password_entry = tk.Entry(self, width=30, borderwidth=5)
        self.repeat_password_entry.grid(row=2, column=1)


        self.message_label = tk.Label(self, text="")
        self.message_label.grid(row=3, column=0)

        self.register_password_button = tk.Button(self, text=self.register_password_button_text, padx=self.btn_padx, pady=self.btn_pady, state="active", command=self.validate_password_registration).grid(row=4,column=2)


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


if __name__ == "__main__":
    app = PasswordRegistrationWindow()
    app.start()