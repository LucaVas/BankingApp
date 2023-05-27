import customtkinter as ctk
from tkinter import messagebox
import bcrypt
import sys


class PasswordRegistrationWindow(ctk.CTk):
    """
    A class representing a password registration window.

    Methods:
    - __init__(self, bank): Initialize the current window.
    - toggle_password(self): Toggle the visibility of password fields.
    - validate_password_registration(self): Validate the password registration.
    - hash_password(self, password: bytes) -> bytes: Hash the given password.
    - register_password(self, password: bytes): Register the password.
    - show_error(self, error: str): Show an error message.
    - start(self): Start the main loop of the window.
    - on_closing(self): Handle the closing event of the window.
    - close(self): Close the window.
    """

    def __init__(self, bank):
        super().__init__()

        self.width = 800
        self.height = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")
        # self.attributes("-topmost", True)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # grid layout
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # holder information
        self.title(bank.name)
        self.password: bytes

        # widgets variables
        self.password_registration_label_text = "Password registration"
        self.password_label_text = "> Enter your password:"
        self.repeat_password_label_text = "> Repeat your password:"
        self.register_password_button_text = "Save password"
        self.switch_var = ctk.StringVar(value="off")

        # widgets
        # ============ Top frame with main label ============ #
        self.password_registration_frame = ctk.CTkFrame(self, corner_radius=0)
        self.password_registration_frame.grid(
            row=0, column=0, columnspan=4, padx=(10, 10), pady=(10, 0), sticky="nsew"
        )
        self.password_registration_frame.grid_rowconfigure(0, weight=1)
        self.password_registration_label = ctk.CTkLabel(
            self.password_registration_frame,
            text=self.password_registration_label_text,
            font=ctk.CTkFont(size=20, weight="normal"),
        )
        self.password_registration_label.grid(row=0, column=0, padx=10, pady=(10, 10))

        # ============ Main frame with entries ============ #
        self.entries_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.entries_frame.grid(
            row=1, column=0, columnspan=3, padx=(10, 10), pady=(0, 10), sticky="nsew"
        )
        self.entries_frame.grid_rowconfigure((0, 1), weight=1)
        self.entries_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.password_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.password_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.password_label.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="w")
        self.password_entry = ctk.CTkEntry(self.entries_frame, show="*")
        self.password_entry.grid(row=0, column=1, padx=10, pady=(10, 10), sticky="ew")

        self.repeat_password_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.repeat_password_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.repeat_password_label.grid(
            row=1, column=0, padx=10, pady=(10, 10), sticky="w"
        )
        self.repeat_password_entry = ctk.CTkEntry(self.entries_frame, show="*")
        self.repeat_password_entry.grid(
            row=1, column=1, padx=10, pady=(10, 10), sticky="ew"
        )

        self.message_label = ctk.CTkLabel(self, text="")
        self.message_label.grid(row=2, column=0, columnspan=3)

        # ============ Bottom row with button and password toggler ============ #
        self.password_switch = ctk.CTkSwitch(
            self,
            text="Show password",
            command=self.toggle_password,
            variable=self.switch_var,
            onvalue="on",
            offvalue="off",
        )
        self.password_switch.grid(row=3, column=2, padx=10, pady=(10, 10), sticky="ew")

        self.register_password_button = ctk.CTkButton(
            self,
            text=self.register_password_button_text,
            state="active",
            width=40,
            height=40,
            text_color="black",
            font=("tahoma", 16),
            command=self.validate_password_registration,
        )
        self.register_password_button.grid(
            row=3, column=3, padx=10, pady=(10, 10), sticky="ew"
        )

    def toggle_password(self) -> None:
        """
        Toggle the visibility of password fields.

        Returns:
        None
        """
        if self.password_entry.cget("show") == "":
            self.password_entry.configure(show="*")
            self.repeat_password_entry.configure(show="*")

        else:
            self.password_entry.configure(show="")
            self.repeat_password_entry.configure(show="")

    def validate_password_registration(self) -> None:
        """
        Validate the password registration.

        Returns:
        None
        """
        password = self.password_entry.get()
        repeated_password = self.repeat_password_entry.get()

        if not password or not repeated_password:
            self.show_error("Invalid input")
        elif password != repeated_password:
            self.show_error("Invalid input")
        else:
            hashed = self.hash_password(bytes(password, "utf-8"))
            self.register_password(hashed)

    def hash_password(self, password: bytes) -> bytes:
        """
        Hash the given password.

        Parameters:
        - password (bytes): The password to hash.

        Returns:
        bytes: The hashed password.
        """
        return bcrypt.hashpw(password, bcrypt.gensalt())

    def register_password(self, password: bytes) -> None:
        """
        Register the password.

        Parameters:
        - password (bytes): The password to register.

        Returns:
        None
        """
        self.password = password
        self.close()

    def show_error(self, error: str) -> None:
        """
        Show an error message.

        Parameters:
        - error (str): The error message to display.

        Returns:
        None
        """
        # parent=self keeps the popup window in front
        messagebox.showerror("Error", error, parent=self)

    def start(self):
        """
        Start the main loop of the window.

        Returns:
        None
        """
        self.mainloop()

    def on_closing(self):
        """
        Handle the closing event of the window.

        Returns:
        None
        """
        if messagebox.askokcancel(
            "Quit",
            "Do you want to quit?\nIf you quit now, the registration process will be stopped.",
            parent=self,
        ):
            self.destroy()
            sys.exit()

    def close(self):
        """
        Close the window.

        Returns:
        None
        """
        self.destroy()
