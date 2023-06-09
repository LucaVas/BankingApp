import customtkinter as ctk # type: ignore
from tkinter import messagebox
from datetime import datetime, date
import sys
sys.path.append("src")
from bank import Bank # type: ignore
import logging

# setting up logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler("./gui_logs/holder_registration.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class HolderRegistrationWindow(ctk.CTk):
    """A window for registering a new holder in the bank."""

    def __init__(self, bank: Bank):
        logger.info("New Holder Registration window created.")
        """
        Initialize the registration window for the new holder.

        Args:
            bank: The bank object which represents the bank.
        """
        super().__init__()

        # geometry & positioning
        self.width = 800
        self.height = 400
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")
        # self.attributes("-topmost", True)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # grid layout
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)

        # holder information
        self.title(bank.name)
        self.holder_name = ""
        self.holder_surname = ""
        self.holder_birth_date: date

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
        self.holder_registration_frame.grid(
            row=0, column=0, columnspan=4, padx=(10, 10), pady=(10, 0), sticky="nsew"
        )
        self.holder_registration_frame.grid_rowconfigure(0, weight=1)
        self.holder_registration_label = ctk.CTkLabel(
            self.holder_registration_frame,
            text=self.holder_registration_label_text,
            font=ctk.CTkFont(size=20, weight="normal"),
        )
        self.holder_registration_label.grid(row=0, column=0, padx=10, pady=(10, 10))

        # ============ Main frame with entries ============ #
        self.entries_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.entries_frame.grid(
            row=1, column=0, columnspan=4, padx=(10, 10), pady=(0, 10), sticky="nsew"
        )
        for i in range(6):
            self.entries_frame.grid_columnconfigure(i, weight=1)
            if i < 3:
                self.entries_frame.grid_rowconfigure(i, weight=1)

        self.holder_name_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.holder_name_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.holder_name_label.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="w")
        self.holder_name_entry = ctk.CTkEntry(self.entries_frame)
        self.holder_name_entry.grid(
            row=0, column=1, padx=10, columnspan=3, pady=(10, 10), sticky="ew"
        )

        self.holder_surname_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.holder_surname_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.holder_surname_label.grid(
            row=1, column=0, padx=10, pady=(10, 10), sticky="w"
        )
        self.holder_surname_entry = ctk.CTkEntry(self.entries_frame)
        self.holder_surname_entry.grid(
            row=1, column=1, padx=10, columnspan=3, pady=(10, 10), sticky="ew"
        )

        self.holder_birth_date_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.holder_birth_date_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.holder_birth_date_label.grid(
            row=2, column=0, padx=10, pady=(10, 10), sticky="w"
        )
        self.holder_birth_date_year_entry = ctk.CTkEntry(
            self.entries_frame, justify="center"
        )
        self.holder_birth_date_year_entry.grid(row=2, column=1, padx=10, pady=(10, 10))
        self.holder_birth_date_separator_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.holder_birth_date_separator_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.holder_birth_date_separator_label.grid(
            row=2, column=2, padx=10, pady=(10, 10)
        )
        self.holder_birth_date_month_entry = ctk.CTkEntry(
            self.entries_frame, justify="center"
        )
        self.holder_birth_date_month_entry.grid(row=2, column=3, padx=10, pady=(10, 10))
        self.holder_birth_date_separator_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.holder_birth_date_separator_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.holder_birth_date_separator_label.grid(
            row=2, column=4, padx=10, pady=(10, 10)
        )
        self.holder_birth_date_day_entry = ctk.CTkEntry(
            self.entries_frame, justify="center"
        )
        self.holder_birth_date_day_entry.grid(row=2, column=5, padx=10, pady=(10, 10))

        # ============ Bottom row with button ============ #
        self.register_button = ctk.CTkButton(
            self,
            text=self.register_button_text,
            state="active",
            width=40,
            height=40,
            text_color="black",
            font=("tahoma", 16),
            command=self.validate_registration,
        ).grid(row=5, column=3, padx=10, pady=(10, 10), sticky="ew")

    def validate_registration(self) -> None:
        """Validate the holder registration form and process the registration if valid."""
        name = self.holder_name_entry.get().strip()
        surname = self.holder_surname_entry.get().strip()
        birth_date_year = self.holder_birth_date_year_entry.get().strip()
        birth_date_month = self.holder_birth_date_month_entry.get().strip()
        birth_date_day = self.holder_birth_date_day_entry.get().strip()

        if not name or not surname:
            logger.error("Name or surname not entered.")
            self.show_error("Invalid input")
        elif not birth_date_year or not birth_date_month or not birth_date_day:
            logger.error("Day, month or year not entered.")
            self.show_error("Invalid input")
        else:
            if (
                self.validate_birth_date(
                    birth_date_year, birth_date_month, birth_date_day
                )
                is False
            ):
                return
            else:
                full_birth_date = f"{birth_date_year}{birth_date_month}{birth_date_day}"
                formatted_birth_date = datetime.strptime(
                    full_birth_date, "%Y%m%d"
                ).date()
                self.register_holder(name, surname, formatted_birth_date)

    def validate_birth_date(self, year: str, month: str, day: str) -> bool:
        """
        Validate the entered birth date.

        Args:
            year: The year of birth.
            month: The month of birth.
            day: The day of birth.

        Returns:
            A boolean indicating whether the birth date is valid or not.
        """
        if len(year) != 4:
            logger.error("Invalid year format")
            self.show_error("Incorrect date format")
            return False
        if len(month) < 1 or len(month) > 2 or len(day) < 1 or len(day) > 2:
            logger.error("Invalid month or day format.")
            self.show_error("Incorrect date format")
            return False

        try:
            y = int(year)
            m = int(month)
            d = int(day)
        except ValueError:
            logger.error("Day, month or year not valid integers.")
            self.show_error("Input not correct")
            return False

        year_now = datetime.now().year

        if y > int(year_now):
            logger.error("Future date entered")
            self.show_error("Incorrect year format")
            return False
        elif m < 0 or m > 12:
            logger.error("Invalid month.")
            self.show_error("Incorrect month format")
            return False
        elif d < 0 or d > 31:
            logger.error("Invalid day.")
            self.show_error("Incorrect day format")
            return False

        try:
            f_date = f"{year}-{month}-{day}"
            date.fromisoformat(f_date)
        except ValueError:
            logger.exception("ValueError")
            self.show_error("Input not correct")
            return False

        return True

    def register_holder(self, name: str, surname: str, birth_date: date) -> None:
        """
        Register the holder with the provided details by saving them in the current class.

        Args:
            name: The name of the holder.
            surname: The surname of the holder.
            birth_date: The birth date of the holder.
        """
        self.holder_name = name.capitalize()
        self.holder_surname = surname.capitalize()
        self.holder_birth_date = birth_date

        self.close()

    def show_error(self, error: str) -> None:
        """Display an error message for incorrect input.

        Args:
            error: The message error to be displayed.
        """
        # parent=self keeps the popup window in front
        messagebox.showerror("Error", error, parent=self)

    def start(self):
        """Start the main event loop of the window."""
        self.mainloop()

    def on_closing(self):
        """Handle the event when the window is closed by the user."""
        if messagebox.askokcancel(
            "Quit",
            "Do you want to quit?\nIf you quit now, the registration process will be stopped.",
            parent=self,
        ):
            self.destroy()
            sys.exit()

    def close(self):
        """Close the window and destroy it."""
        self.destroy()
