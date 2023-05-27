import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import re
from datetime import datetime
import sys
sys.path.append("src")
from account import Account
from holder import Holder
from writer import Writer
from gui.treeview_frame import TreeViewFrame


class TransferWindow(ctk.CTkToplevel):
    """A custom tkinter top-level window for transferring funds."""

    def __init__(
        self, parent, account: Account, temp_db: dict, holder: Holder, writer: Writer, treeview_frame: TreeViewFrame
    ) -> None:
        """Initialize the current window.

        Args:
            parent: The parent window, MainWindow.
            account: The account object.
            temp_db: The temporary database object.
            holder: The holder object.
            writer: The writer object.
            treeview_frame: The treeview frame object.
        """
        super().__init__()

        self.parent_window = parent
        self.account = account
        self.temp_db = temp_db
        self.holder = holder
        self.writer = writer
        self.treeview_frame = treeview_frame

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

        self.title("Transfer")
        self.main_label_text = "Transfer"
        self.amount_label_text = "> Insert the amount"
        self.recipient_account_label_text = "> Account to"
        self.reason_label_text = "> Enter the reason for transfer"
        self.confirm_button_text = "Confirm"

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

        self.recipient_account_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.recipient_account_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.recipient_account_label.grid(
            row=1, column=0, padx=10, pady=(10, 10), sticky="w"
        )
        self.recipient_account_entry = ctk.CTkEntry(self.entries_frame)
        self.recipient_account_entry.grid(
            row=1, column=1, columnspan=2, padx=10, pady=(10, 10), sticky="ew"
        )

        self.reason_label = ctk.CTkLabel(
            self.entries_frame,
            text=self.reason_label_text,
            font=ctk.CTkFont(size=15, weight="normal"),
        )
        self.reason_label.grid(row=2, column=0, padx=10, pady=(10, 10), sticky="w")
        self.reason_entry = ctk.CTkEntry(self.entries_frame)
        self.reason_entry.grid(
            row=2, column=1, columnspan=2, padx=10, pady=(10, 10), sticky="ew"
        )

        self.message_label = ctk.CTkLabel(self, text="")
        self.message_label.grid(
            row=3, column=0, columnspan=3, padx=10, pady=(10, 10), sticky="ew"
        )

        # ============ Bottom row with button ============ #
        self.confirm_button = ctk.CTkButton(
            self,
            text=self.confirm_button_text,
            state="active",
            text_color="black",
            font=("tahoma", 16),
            command=self.validate_transfer,
        )
        self.confirm_button.grid(row=3, column=2, padx=10, pady=(10, 10), sticky="ew")

    def validate_transfer(self) -> None:
        """Validate the transfer by checking the amount, recipient, and reason."""

        amount, current_amount = self.validate_amount()
        recipient_account = self.validate_recipient()
        reason = self.validate_reason()

        self.transfer(amount, current_amount, recipient_account, reason)

    def validate_recipient(self) -> str:
        """Validate the recipient account number.

        Returns:
            str: The validated recipient account number.

        Raises:
            Exception: If the recipient account number is invalid.
        """
        recipient_account = self.recipient_account_entry.get().strip()
        pattern = r"^LT\d{18}$"

        if re.match(pattern, recipient_account):
            return recipient_account
        else:
            self.show_error("Invalid recipient")
            raise Exception()

    def validate_reason(self) -> str:
        """Validate the reason for transfer.

        Returns:
            str: The validated reason.

        Raises:
            Exception: If the reason is invalid.
        """
        reason = self.reason_entry.get()
        if not reason:
            self.show_error("Invalid reason")
            raise Exception
        else:
            return reason

    def validate_amount(self) -> tuple[float, float]:
        """Validate the transfer amount.

        Returns:
            tuple[float, float]: The validated transfer amount and the current amount.

        Raises:
            Exception: If the amount is invalid or insufficient.
        """
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            self.show_error("Invalid amount")
            raise Exception

        current_amount = float(
            self.parent_window.balance_frame.balance_amount_label.cget("text")
        )

        if amount < 0 or not amount:
            self.show_error("Invalid amount")
            raise Exception
        elif current_amount < amount:
            self.show_error("Invalid amount")
            raise Exception
        else:
            return amount, current_amount

    def transfer(
        self, amount: float, current_amount: float, recipient_account: str, reason: str
    ) -> None:
        """Perform the transfer operation.

        Args:
            amount (float): The transfer amount.
            current_amount (float): The current balance amount.
            recipient_account (str): The recipient account number.
            reason (str): The reason for the transfer.
        """
        action = "transfer"
        datestamp = datetime.now()

        self.parent_window.balance_frame.balance_amount_label.configure(
            text=current_amount - amount
        )
        self.account.balance = current_amount - amount

        self.add_action_to_treeview(amount, action, recipient_account, datestamp)
        self.add_action_to_db(amount, action, recipient_account, datestamp, reason)

        self.clear_exchanged_balance()

        self.close()

    def add_action_to_treeview(
        self, amount: float, action: str, recipient_account: str, datestamp: datetime
    ) -> None:
        """Add the transfer action to the treeview.

        Args:
            amount (float): The transfer amount.
            action (str): The action type.
            recipient_account (str): The recipient account number.
            datestamp (datetime): The date and time of the transfer.
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
        """Add the transfer action to the temporary database.

        Args:
            amount (float): The transfer amount.
            action (str): The action type.
            recipient_account (str): The recipient account number.
            datestamp (datetime): The date and time of the transfer.
            reason (str): The reason for the transfer.
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

    def clear_exchanged_balance(self) -> None:
        """Clear the exchanged balance in the parent window."""
        self.parent_window.balance_exchange_frame.exchange_balance_amount_label.configure(
            text=""
        )
        self.parent_window.balance_exchange_frame.exchange_currency_label.configure(
            text=""
        )

    def show_error(self, text: str) -> None:
        """Show an error message box.

        Args:
            text (str): The error message text.
        """
        # parent=self keeps the popup window in front
        messagebox.showerror("Error", text, parent=self)

    def on_closing(self):
        """Handle the closing event of the TransferWindow."""
        if messagebox.askokcancel("Quit", "Do you want to quit?", parent=self):
            self.destroy()

    def close(self) -> None:
        """Close the TransferWindow."""

        self.destroy()
