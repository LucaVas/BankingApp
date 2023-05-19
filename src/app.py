from bank import Bank
from holder import Holder
from account import Account
from gui_app import App, WelcomeWindow


app = WelcomeWindow()
app.mainloop()

holder_info = App.holder_info
password_info = App.password

holder = Holder(App.holder_info[0],App.holder_info[1],App.holder_info[2],password_info[0])
print(repr(holder))

