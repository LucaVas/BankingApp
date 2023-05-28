import customtkinter as ctk # type: ignore
from tkinter import messagebox
import bcrypt
from datetime import date, datetime
import sys
sys.path.append("src")
from bank import Bank # type: ignore


class LoginWindow(ctk.CTk):
    """Class representing the GUI for login window."""

    def __init__(self, bank: Bank, temp_db: dict) -> None:
        """
        Initialize the LoginWindow.

        Args:
            bank (Bank): An instance of the Bank class.
            temp_db (dict): The dictionary where the databse is loaded.

        Returns:
            None.
        """
        super().__init__()

        self.db = temp_db

        self.width = 800
        self.height = 400
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
        self.switch_var = ctk.StringVar(value="off")

        # widgets
        # ============ Top frame with main label ============ #
        self.login_frame = ctk.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(
            row=0, column=0, columnspan=3, padx=(10, 10), pady=(10, 0), sticky="nsew"
        )
        self.login_frame.grid_rowconfigure(0, weight=1)
        self.login_label = ctk.CTkLabel(
            self.login_frame,
            text=self.login_label_text,
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.login_label.grid(row=0, column=0, padx=10, pady=(10, 10))

        # ============ Main frame with entries ============ #
        self.entries_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.entries_frame.grid(
            row=1, column=0, columnspan=3, padx=(10, 10), pady=(0, 10), sticky="nsew"
        )
        self.entries_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.entries_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.name_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.name_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.name_label.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="w")
        self.name_entry = ctk.CTkEntry(self.entries_frame)
        self.name_entry.grid(row=0, column=1, padx=10, pady=(10, 10), sticky="ew")

        self.surname_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.surname_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.surname_label.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="w")
        self.surname_entry = ctk.CTkEntry(self.entries_frame)
        self.surname_entry.grid(row=1, column=1, padx=10, pady=(10, 10), sticky="ew")

        self.password_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.password_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.password_label.grid(row=2, column=0, padx=10, pady=(10, 10), sticky="w")
        self.password_entry = ctk.CTkEntry(self.entries_frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=(10, 10), sticky="ew")

        # ============ Bottom row with button ============ #
        self.password_switch = ctk.CTkSwitch(
            self,
            text="Show password",
            command=self.toggle_password,
            variable=self.switch_var,
            onvalue="on",
            offvalue="off",
        )
        self.password_switch.grid(row=2, column=1, padx=10, pady=(10, 10), sticky="ew")
        self.login_button = ctk.CTkButton(
            self,
            text=self.login_button_text,
            state="active",
            width=100,
            height=40,
            text_color="black",
            font=("tahoma", 16),
            command=self.validate_login_information,
        )
        self.login_button.grid(row=2, column=2, padx=10, pady=(10, 10), sticky="ew")

    def toggle_password(self) -> None:
        """
        Toggle the visibility of the password entry field.

        Returns:
            None.
        """
        if self.password_entry.cget("show") == "":
            self.password_entry.configure(show="*")
        else:
            self.password_entry.configure(show="")

    def validate_login_information(self) -> None:
        """
        Validate the provided login information.

        Returns:
            None.
        """
        self.first = self.name_entry.get()
        self.last = self.surname_entry.get()
        self.password = bytes(self.password_entry.get(), "utf-8")

        for holder in self.db["holders"]:
            hashed = bytes(holder["password"], "utf-8")
            if (
                self.first == holder["first"]
                and self.last == holder["last"]
                and bcrypt.checkpw(self.password, hashed)
            ):
                self.id = holder["id"]
                self.last_access = datetime.now()
                self.close()
                return
            else:
                continue

        self.show_error("User not found")

    def show_error(self, error: str) -> None:
        """
        Display a messagebox with an error message.

        Args:
            error (str): The error message to be displayed.

        Returns:
            None.
        """
        # parent=self keeps the popup window in front
        messagebox.showerror("Error", error, parent=self)

    def start(self):
        """
        Start the main loop of the GUI.

        Returns:
            None.
        """
        self.mainloop()

    def close(self):
        """
        Close the GUI window.

        Returns:
            None.
        """
        self.destroy()
