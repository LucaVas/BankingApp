import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from .top_up_window import TopUpWindow
from .holder_info_frame import HolderInfoFrame
from .bank_info_frame import BankInfoFrame
from .balance_frame import BalanceFrame
from .exchange_frame import ExchangeFrame
from .balance_exchange_frame import BalanceExchangeFrame
from .transfer_window import TransferWindow
from .treeview_frame import TreeViewFrame
import sys

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class MainWindow(tk.Tk):
    """Main window of the application."""

    def __init__(self, holder, account, bank, currency_obj, temp_db, writer):
        """Initialize the main window.

        Args:
            holder: Holder object.
            account: Account object.
            bank: Bank object.
            currency_obj: Currency object.
            temp_db: Database where the json is loaded.
            writer: Writer object.
        """
        super().__init__()

        self.holder = holder
        self.account = account
        self.bank = bank
        self.currency_obj = currency_obj
        self.temp_db = temp_db
        self.writer = writer

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # geometry & positioning
        self.width = 1500
        self.height = 700
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")

        # grid layout
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        # variables
        self.title(bank.name)
        self.main_label_text = "Your account overview"
        self.top_up_button_text = "Top up"
        self.transfer_button_text = "Transfer"
        self.log_out_button_text = "Log out"

        # widget
        # ============ Sidebar ============ #
        self.sidebar_frame = ctk.CTkFrame(self, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=7, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.sidebar_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.main_label = ctk.CTkLabel(
            self.sidebar_frame,
            text=self.main_label_text,
            font=ctk.CTkFont("Tahoma", size=23, weight="bold"),
        )
        self.main_label.grid(row=0, column=0, columnspan=3, padx=(5, 5), pady=(5, 5))
        self.top_up_button = ctk.CTkButton(
            self.sidebar_frame,
            text=self.top_up_button_text,
            state="active",
            command=self.open_top_up_window,
        )
        self.top_up_button.grid(row=2, column=1, sticky="ew")
        self.transfer_button = ctk.CTkButton(
            self.sidebar_frame,
            text=self.transfer_button_text,
            state="active",
            command=self.open_transfer_window,
        )
        self.transfer_button.grid(row=3, column=1, sticky="ew")
        self.appearance_mode_label = ctk.CTkLabel(
            self.sidebar_frame, text="Appearance Mode:"
        )
        self.appearance_mode_label.grid(row=5, column=1, sticky="ew")
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(
            self.sidebar_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_optionemenu.grid(
            row=6, column=1, sticky="ew", padx=(5, 5), pady=(5, 5)
        )

        # ============ Right frames ============ #
        self.holder_info_frame = HolderInfoFrame(self, self.holder, self.account)
        self.holder_info_frame.grid(
            row=0, column=5, rowspan=2, padx=(5, 5), pady=(5, 5), sticky="nsew"
        )

        self.exchange_frame = ExchangeFrame(self, self.account, self.currency_obj)
        self.exchange_frame.grid(
            row=2, column=5, rowspan=2, padx=(5, 5), pady=(5, 5), sticky="nsew"
        )

        self.bank_info_frame = BankInfoFrame(self, self.bank)
        self.bank_info_frame.grid(
            row=4, column=5, rowspan=2, padx=(5, 5), pady=(5, 5), sticky="nsew"
        )

        # ============ Center frames ============ #
        self.balance_frame = BalanceFrame(self, self.account)
        self.balance_frame.grid(
            row=0, column=1, columnspan=4, padx=(5, 5), pady=(5, 5), sticky="nsew"
        )

        self.balance_exchange_frame = BalanceExchangeFrame(self, self.exchange_frame)
        self.balance_exchange_frame.grid(
            row=1, column=1, columnspan=4, padx=(5, 5), pady=(5, 5), sticky="nsew"
        )

        self.treeview_frame = TreeViewFrame(self, self.holder, self.temp_db)
        self.treeview_frame.grid(
            row=2,
            column=1,
            rowspan=5,
            columnspan=4,
            padx=(5, 5),
            pady=(5, 5),
            sticky="nsew",
        )

        # buttons
        self.log_out_button = ctk.CTkButton(
            self, text=self.log_out_button_text, state="active", command=self.log_out
        )
        self.log_out_button.grid(row=6, column=5, padx=(5, 5), pady=(5, 5))

        self.top_up_window = None
        self.transfer_window = None

    def change_appearance_mode_event(self, appearance_mode: str):
        """Change the appearance mode of the application.

        Args:
            appearance_mode: The selected appearance mode ("Light", "Dark", "System").
        """
        ctk.set_appearance_mode(appearance_mode)

    def open_top_up_window(self):
        """Open the top-up window."""
        if self.top_up_window is None or not self.top_up_window.winfo_exists():
            self.top_up_toplevel_window = TopUpWindow(
                self,
                self.temp_db,
                self.holder,
                self.writer,
                self.treeview_frame,
                self.account,
            )
        else:
            self.top_up_toplevel_window.focus()  # if window exists focus it

    def open_transfer_window(self):
        """Open the transfer window."""
        if self.transfer_window is None or not self.transfer_window.winfo_exists():
            self.transfer_toplevel_window = TransferWindow(
                self,
                self.account,
                self.temp_db,
                self.holder,
                self.writer,
                self.treeview_frame,
            )
        else:
            self.transfer_toplevel_window.focus()

    def start(self):
        """Start the main window."""
        self.mainloop()

    def on_closing(self):
        """Handle the closing event of the main window."""
        if messagebox.askokcancel(
            "Quit",
            "Do you want to quit? If so, the actions you took will not be saved.",
        ):
            self.destroy()
            sys.exit()

    def log_out(self):
        """Log out of the application."""
        self.destroy()
