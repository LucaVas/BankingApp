class Bank:
    def __init__(self, market_data: dict, company_info: dict[str, str]):
        self.name = company_info.get("Name")
        self.year = 1956
        self.shares_amount = company_info.get("SharesOutstanding")
        self.share_price = self.calculate_shares(market_data)[0]
        self.shares_delta = self.calculate_shares(market_data)[1]

    def __str__(self) -> str:
        return f"{self.name} was founded in {self.year}. The current amount of shares is {self.shares_amount} at {self.share_price:.2f} $ each. The last market change saw the bank with a result of {self.shares_delta:.2f} %."

    def __repr__(self) -> str:
        return f"Bank('{self.name}', {self.year}, {self.shares_amount}, {self.share_price}, {self.shares_delta})"

    def calculate_shares(self, market_data: dict) -> tuple[float, float]:
        list_of_changes = list(market_data["Time Series (5min)"])
        last = list_of_changes[0]
        previous = list_of_changes[1]

        share_last_price = float(market_data["Time Series (5min)"][last]["4. close"])
        delta = float(market_data["Time Series (5min)"][last]["4. close"]) - float(
            market_data["Time Series (5min)"][previous]["4. close"]
        )
        return share_last_price, delta
