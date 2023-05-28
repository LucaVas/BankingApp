from typing import Optional
import logging

# setting up logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler("currency.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class Currency:
    list_of_currencies = [
        "AUD",
        "CHF",
        "CZK",
        "DKK",
        "EUR",
        "GBP",
        "HRK",
        "HUF",
        "JPY",
        "NOK",
        "PLN",
        "RON",
        "RUB",
        "SEK",
        "USD",
    ]

    def __init__(self, exchange_rates: dict[str, float]) -> None:
        self.exchange_rates = exchange_rates
        self.currencies = self.list_of_currencies
        logger.info(f"Currency object created succesfully. {self.__repr__()}")

    def __str__(self) -> str:
        return f"List of currencies availabke: {self.currencies}"

    def __repr__(self) -> str:
        return f"Currency({self.exchange_rates}, {self.currencies})"

    def get_exchange(self, currency: str) -> Optional[float]:
        """
        Function which accepts a foreign currency str value, and returns the current conversion rate float
        """
        return self.exchange_rates.get(currency)
