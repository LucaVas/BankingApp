from datetime import datetime

class Holder():
    def __init__(self, first: str, last: str, birth_date: str, password: bytes):
        self.id = 0
        self.first_name = first
        self.last_name = last
        self.birth_date = datetime.strptime(birth_date, "%d%m%Y").date()
        self.password = password
        self.is_blocked = False
        self.onboarding_date = datetime.now()

    def __str__(self) -> str:
        return f"Account holder: {self.first_name} {self.last_name}.\nDate of Birth: {self.birth_date}\nOnboarding date: {self.onboarding_date}\nAccount blocked: {self.is_blocked}"
    
    def __repr__(self) -> str:
        return f"Holder({self.id},'{self.first_name}','{self.last_name}',Birth:{self.birth_date},Blocked:{self.is_blocked},Onboarded:{self.onboarding_date},Password:{str(self.password, 'utf-8')})"
    
    def block(self, is_blocked: bool) -> None:
        if is_blocked is True:
            self.is_blocked = True
        elif is_blocked is False:
            self.is_blocked = False
        else:
            raise ValueError
