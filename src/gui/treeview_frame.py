import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class TreeViewFrame(ctk.CTkFrame):
    def __init__(self, parent, holder, temp_db: dict):
        super().__init__(parent)

        self.parent_window = parent
        self.temp_db = temp_db
        self.holder = holder

        # style
        self.style = ttk.Style()
        # theme
        self.style.theme_use("clam")
        # treeview background
        self.style.configure("Treeview", 
            background="white",
            foreground="white",
            rowheight=25,
            fieldbackground="#242424")
        # change selected rows
        self.style.map("Treeview",
            background=[("selected", "#2fa572")])

        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("Action", "Amount", "Recipient account", "Date")
        # format columns
        self.tree.column("#0", width=0, stretch="no")
        self.tree.column("Action", anchor="center", width=5)
        self.tree.column("Amount", anchor="center", width=5)
        self.tree.column("Recipient account", anchor="center", width=80)
        self.tree.column("Date", anchor="center", width=80)

        # Headings
        self.tree.heading("0", text="",anchor="center")
        self.tree.heading("Action", text="Action",anchor="center")
        self.tree.heading("Amount", text="Amount",anchor="center")
        self.tree.heading("Recipient account", text="Recipient account", anchor="center")
        self.tree.heading("Date", text="Date", anchor="center")

        # create striped rows tags
        self.tree.tag_configure("oddrow", background="#3b3b3b")
        self.tree.tag_configure("evenrow", background="#4f4f4f")


        # Add data
        self.history_record = self.temp_db["history"]
        self.counter = 0
        for record in self.history_record:
            if record["id"] == self.holder.id:
                if self.counter % 2 == 0:
                    self.tree.insert(parent='', 
                                index='end', 
                                iid=self.counter, 
                                text="", 
                                values=(
                                    record["action"].capitalize(), 
                                    record["amount"], 
                                    record["recipient_account"], 
                                    record["datestamp"]),
                                tags=("evenrow",))
                else:
                    self.tree.insert(parent='', 
                                index='end', 
                                iid=self.counter, 
                                text="", 
                                values=(
                                    record["action"].capitalize(), 
                                    record["amount"], 
                                    record["recipient_account"], 
                                    record["datestamp"]),
                                tags=("oddrow",))        
            self.counter += 1
        
        
        self.tree.pack(fill=tk.BOTH, expand=True, padx=(5,5), pady=(5,5))

