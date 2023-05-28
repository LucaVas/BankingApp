import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk # type: ignore
from datetime import datetime
from gui.treeview_frame import TreeViewFrame # type: ignore
import sys
sys.path.append("src")
from holder import Holder # type: ignore
from writer import Writer # type: ignore
from account import Account # type: ignore



class TopUpWindow(ctk.CTkToplevel):
    """A custom top-level window for performing a top-up operation."""

    def __init__(
        self, parent, temp_db: dict, holder: Holder, writer: Writer, treeview_frame: TreeViewFrame, account: Account
    ) -> None:
        """Initialize the current window.

        Args:
            parent: The parent window.
            temp_db: The temporary database object.
            holder: The account holder object.
            writer: The writer object for managing database operations.
            treeview_frame: The frame containing the treeview widget.
            account: The account object for the top-up operation.
        """
        super().__init__()

        self.parent_window = parent
        self.temp_db = temp_db
        self.holder = holder
        self.writer = writer
        self.treeview_frame = treeview_frame
        self.account = account

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # geometry & positioning
        self.width = 500
        self.height = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")
        # self.attributes("-topmost", True)

        # grid layout
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.title("Top Up")
        self.main_label_text = "Top Up"
        self.amount_label_text = "> Insert the amount"
        self.account_from_label_text = "> Account from"
        self.account_from_optionmenu_options = (
            self.parent_window.holder.connected_accounts
        )
        self.account_from_optionmenu_var = tk.StringVar(
            value=self.account_from_optionmenu_options[0]
        )
        self.top_up_button_text = "Top up"

        # ============ Top frame with main label ============ #
        self.main_label_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_label_frame.grid(
            row=0, column=0, columnspan=3, padx=(10, 10), pady=(10, 0), sticky="nsew"
        )
        self.main_label_frame.grid_rowconfigure(0, weight=1)
        self.main_label = ctk.CTkLabel(
            self.main_label_frame,
            text=self.main_label_text,
            font=ctk.CTkFont(size=20, weight="normal"),
        )
        self.main_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

        # ============ Main frame with entries ============ #
        self.entries_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.entries_frame.grid(
            row=1, column=0, columnspan=3, padx=(10, 10), pady=(0, 10), sticky="nsew"
        )
        self.entries_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.entries_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Entry label: Amount
        self.amount_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.amount_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.amount_label.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="w")
        self.amount_entry = ctk.CTkEntry(self.entries_frame)
        self.amount_entry.grid(
            row=0, column=1, columnspan=2, padx=10, pady=(10, 10), sticky="ew"
        )

        # Option Label: Account from
        self.account_from_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.account_from_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.account_from_label.grid(
            row=1, column=0, padx=10, pady=(10, 10), sticky="w"
        )
        self.account_from_optionmenu = ctk.CTkOptionMenu(
            self.entries_frame,
            values=self.account_from_optionmenu_options,
            variable=self.account_from_optionmenu_var,
        )
        self.account_from_optionmenu.grid(
            row=1, column=1, columnspan=2, padx=10, pady=(10, 10), sticky="ew"
        )
        # Option: account from

        self.message_label = ctk.CTkLabel(self, text="")
        self.message_label.grid(row=2, column=0, columnspan=3)

        # ============ Bottom row with button ============ #
        self.top_up_button = ctk.CTkButton(
            self,
            text=self.top_up_button_text,
            state="active",
            text_color="black",
            font=("tahoma", 16),
            command=self.validate_top_up,
        )
        self.top_up_button.grid(row=3, column=2, padx=10, pady=(10, 10), sticky="ew")

    def validate_top_up(self) -> None:
        """Validate the top-up amount entered by the user."""
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            self.show_error("Invalid amount")
            return

        if amount < 0 or not amount:
            self.show_error("Invalid amount")
        else:
            self.top_up(amount)

    def top_up(self, amount: float) -> None:
        """Perform the top-up operation.

        Args:
            amount: The top-up amount.

        Raises:
            ValueError: If the amount is negative or zero.

        Note:
            The top-up operation updates the balance and adds the action to the treeview and database.
        """
        action = "top-up"
        recipient_account = self.account.account_number
        datestamp = datetime.now()
        reason = "Top up to self"

        current_amount = self.parent_window.balance_frame.balance_amount_label.cget(
            "text"
        )
        self.parent_window.balance_frame.balance_amount_label.configure(
            text=current_amount + amount
        )

        self.parent_window.account.balance = current_amount + amount

        self.add_action_to_treeview(amount, action, recipient_account, datestamp)
        self.add_action_to_db(amount, action, recipient_account, datestamp, reason)

        self.clear_exchanged_balance()

        self.close()

    def clear_exchanged_balance(self) -> None:
        """Clear the exchanged balance in the parent window."""
        self.parent_window.balance_exchange_frame.exchange_balance_amount_label.configure(
            text=""
        )
        self.parent_window.balance_exchange_frame.exchange_currency_label.configure(
            text=""
        )

    def add_action_to_treeview(
        self, amount: float, action: str, recipient_account: str, datestamp: datetime
    ) -> None:
        """Add the top-up action to the treeview.

        Args:
            amount: The top-up amount.
            action: The action type.
            recipient_account: The recipient account number.
            datestamp: The date and time of the top-up.
        """
        self.treeview_frame.add_record(
            action, amount, recipient_account, str(datestamp)
        )

    def add_action_to_db(
        self,
        amount: float,
        action: str,
        recipient_account: str,
        datestamp: datetime,
        reason: str,
    ) -> None:
        """Add the top-up action to the temporary database.

        Args:
            amount: The top-up amount.
            action: The action type.
            recipient_account: The recipient account number.
            datestamp: The date and time of the top-up.
            reason: The reason for the top-up.
        """
        self.writer.temp_write_history(
            self.holder,
            action,
            amount,
            recipient_account,
            datestamp,
            reason,
            self.temp_db,
        )

    def show_error(self, error: str) -> None:
        """Show an error message box.

        Args:
            text (str): The error message text.
        """
        # parent=self keeps the popup window in front
        messagebox.showerror("Error", error, parent=self)

    def on_closing(self):
        """Handle the window closing event."""
        if messagebox.askokcancel("Quit", "Do you want to quit?", parent=self):
            self.destroy()

    def close(self) -> None:
        """Close the top-up window."""
        self.destroy()
