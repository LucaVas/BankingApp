class Bank:
    def __init__(self):
        self.name = "Luca's bank"
        self.year = 2023
        self.shares_amount = 100
        self.share_price = 50.0
        self.shares_delta = 2.5

    def __str__(self) -> str:
        return f"{self.name} was founded in {self.year}. The current amount of shares is {self.shares_amount} at {self.share_price:.2f} $ each. The last market change saw the bank with a result of {self.shares_delta:.2f} %."

    def __repr__(self) -> str:
        return f"Bank('{self.name}', {self.year}, {self.shares_amount}, {self.share_price}, {self.shares_delta})"