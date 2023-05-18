from datetime import date, datetime

class Holder():
    def __init__(self):
        self.id = 0
        self.first_name = "Luca"
        self.last_name = "Vassos"
        self.birth_date = date(1994, 5, 14)
        self.password = ""
        self.is_blocked = False
        self.onboarding_date = datetime.now()

    def __str__(self) -> str:
        return f"Account holder: {self.first_name} {self.last_name}.\nDate of Birth: {self.birth_date}\nOnboarding date: {self.onboarding_date}\nAccount blocked: {self.is_blocked}"
    
    def __repr__(self) -> str:
        return f"Holder({self.id},'{self.first_name}','{self.last_name}',Birth:{self.birth_date},Blocked:{self.is_blocked},Onboarded:{self.onboarding_date})"
