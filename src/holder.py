from datetime import datetime, date

class Holder():
    def __init__(self, first: str, last: str, birth_date: date):
        self.id = 99
        self.first_name = first
        self.last_name = last
        self.birth_date = birth_date
        self._password = b""
        self.is_blocked = False
        self.onboarding_date = datetime.now()
        self.accounts: list[str] = ["LT123456"]
        self.connected_accounts = ["LT123456789123"]

    def __str__(self) -> str:
        return f"Account holder: {self.first_name} {self.last_name}.\nDate of Birth: {self.birth_date}\nOnboarding date: {self.onboarding_date}\nAccount blocked: {self.is_blocked}"
    
    def __repr__(self) -> str:
        return f"Holder({self.id},'{self.first_name}','{self.last_name}',Birth:{self.birth_date},Blocked:{self.is_blocked},Onboarded:{self.onboarding_date},Password:{str(self.password, 'utf-8')})"
    
    @property
    def password(self) -> bytes:
        return self._password
    
    @password.setter
    def password(self, password: bytes) -> None:
        self._password = password

    def block(self, is_blocked: bool) -> None:
        if is_blocked is True:
            self.is_blocked = True
        elif is_blocked is False:
            self.is_blocked = False
        else:
            raise ValueError
