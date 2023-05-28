import tkinter as tk
from tkinter import ttk
import customtkinter as ctk # type: ignore
import sys 
sys.path.append("src")
from holder import Holder # type: ignore
import logging

# setting up logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler("./gui_logs/treeview_frame.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class TreeViewFrame(ctk.CTkFrame):
    """A custom Tkinter frame for displaying a tree view of records.

    This frame is used to display a tree view of records, including actions, amounts,
    recipient accounts, and dates. It provides methods to add records and load history data.

    Args:
        parent (tkinter.Widget): The parent widget to which this frame belongs.
        holder (Holder): The holder object containing the holder information.
        temp_db (dict): A temporary database object containing history records.
    """
    def __init__(self, parent, holder: Holder, temp_db: dict):
        """Initialize the current frame.

        Args:
            parent (tkinter.Widget): The parent widget to which this frame belongs.
            holder (Holder): The holder object containing the holder information.
            temp_db (dict): A temporary database object containing history records.

        """
        super().__init__(parent)

        self.parent_window = parent
        self.temp_db = temp_db
        self.holder = holder
        self.counter = 0

        # style
        self.style = ttk.Style()
        # theme
        self.style.theme_use("clam")
        # treeview background
        self.style.configure(
            "Treeview",
            background="white",
            foreground="white",
            rowheight=25,
            fieldbackground="#242424",
        )
        # change selected rows
        self.style.map("Treeview", background=[("selected", "#2fa572")])

        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("Action", "Amount", "Recipient account", "Date")
        self.tree["displaycolumns"] = (0,1,2,3)
        # format columns
        self.tree.column("#0", width=0, stretch=False)
        self.tree.column("Action", anchor="center", width=5)
        self.tree.column("Amount", anchor="center", width=5)
        self.tree.column("Recipient account", anchor="center", width=80)
        self.tree.column("Date", anchor="center", width=80)

        # Headings
        self.tree.heading("0", text="", anchor="center")
        self.tree.heading("Action", text="Action", anchor="center")
        self.tree.heading("Amount", text="Amount", anchor="center")
        self.tree.heading(
            "Recipient account", text="Recipient account", anchor="center"
        )
        self.tree.heading("Date", text="Date", anchor="center")

        # create striped rows tags
        self.tree.tag_configure("oddrow", background="#3b3b3b")
        self.tree.tag_configure("evenrow", background="#4f4f4f")

        self.load_history()

    def add_record(
        self, action: str, amount: float, recipient_account: str, datestamp: str
    ) -> None:
        """Add a record to the tree view.

        Args:
            action (str): The action of the record.
            amount (float): The amount of the record.
            recipient_account (str): The recipient account of the record.
            datestamp (str): The datestamp of the record.

        Returns:
            None

        """
        val = (action.capitalize(), amount, recipient_account, datestamp)

        if self.counter % 2 == 0:
            self.tree.insert(
                parent="",
                index=0,
                iid=str(self.counter),
                text="",
                values=val,
                tags=("evenrow",),
            )
        else:
            self.tree.insert(
                parent="",
                index=0,
                iid=str(self.counter),
                text="",
                values=val,
                tags=("oddrow",),
            )
        self.counter += 1

    def load_history(self) -> None:
        """Load history records into the tree view.

        Returns:
            None

        """
        # Add data
        self.history_record = self.temp_db["history"]
        for record in self.history_record:
            val = (
                record["action"].capitalize(),
                record["amount"],
                record["recipient_account"],
                record["datestamp"],
            )
            if record["id"] == self.holder.id:
                if self.counter % 2 == 0:
                    self.tree.insert(
                        parent="",
                        index=0,
                        iid=str(self.counter),
                        text="",
                        values=val,
                        tags=("evenrow",),
                    )
                else:
                    self.tree.insert(
                        parent="",
                        index=0,
                        iid=str(self.counter),
                        text="",
                        values=val,
                        tags=("oddrow",),
                    )
            self.counter += 1

        self.tree.pack(fill=tk.BOTH, expand=True, padx=(5, 5), pady=(5, 5))
