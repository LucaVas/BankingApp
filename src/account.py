from currency import Currency
    
        
class Account:
    def __init__(self, owner_id: int, balance: float, interest_rate: str, currency: str = "EUR") -> None:
        self.id = 451
        self.account_number = "LT1234567890"
        self.owner_id = owner_id
        self.is_active = True
        self._balance = balance
        self.currency = currency
        self._interest_rate = float(interest_rate)

    def __str__(self) -> str:
        return f"This account holds {self.balance:.2f} {self.currency}. The account's interest rate is {self.interest_rate}."

    def __repr__(self) -> str:
        return f"Account({self.id},{self.owner_id},Active:{self.is_active},{self.balance},{self.currency},{self.interest_rate:.2f}%)"
    
    @property
    def interest_rate(self) -> float:
        return self._interest_rate
    
    @interest_rate.setter
    def interest_rate(self, rate: float) -> None:
        try:
            self._interest_rate = float(rate)
        except TypeError:
            raise TypeError("Incorrect type of interest rate.")

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, amount: float) -> None:
        try:
            self._balance = float(amount)
        except TypeError:
            raise TypeError("Incorrect type of amount")

    def change_status(self, is_active: bool) -> None:
        if is_active is True:
            self.is_active = True
        elif is_active is False:
            self.is_active = False
        else:
            raise ValueError

    def add_money(self, amount: float) -> None:
        self.balance += amount
        print(f"Balance updated. New balance: {self.balance} {self.currency}.")
    
    def change_interest_rate(self, rate: float) -> None:
        self.interest_rate = rate
        print(f"Interest rate updated. New interest rate: {self.interest_rate:.2f} %.")