from bank import Bank
from holder import Holder
from account import Account
from gui_app import App, WelcomeWindow


app = WelcomeWindow()
app.mainloop()

holder_info = App.main_content[0]
password_info = App.main_content[1]

holder = Holder(holder_info["first"],holder_info["last"],holder_info["birth_date"],password_info["password"])
print(repr(holder))

