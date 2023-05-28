from __future__ import annotations
import shortuuid
import random
import logging

# setting up logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler("account.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class Account:
    def __init__(
        self,
        owner_id: int,
        balance: float,
        interest_rate: str,
        currency: str = "EUR",
        id=shortuuid.uuid(),
    ) -> None:
        self.id = id
        self.account_number = self.create_account_number()
        self.owner_id = owner_id
        self.is_active = True
        self._balance = balance
        self.currency = currency
        self._interest_rate = float(interest_rate)

        logger.info(f"Account object created succesfully. {self.__repr__()}")

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
            logger.info("Interest rate set succesfully.")
        except TypeError:
            logger.exception("TypeError")
            raise TypeError("Incorrect type of interest rate.")

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, amount: float) -> None:
        try:
            self._balance = float(amount)
            logger.info("Balance set successfully.")
        except TypeError:
            logger.exception("TypeError")
            raise TypeError("Incorrect type of amount")

    def change_status(self, is_active: bool) -> None:
        if is_active is True:
            self.is_active = True
            logger.info("Account activated.")
        elif is_active is False:
            self.is_active = False
            logger.info("Account deactivated.")
        else:
            logger.error("Account status not set.")
            raise ValueError

    def add_money(self, amount: float) -> None:
        self.balance += amount
        logger.info(f"Amount added to balance successfully. New balance: {self.balance}")

    def change_interest_rate(self, rate: float) -> None:
        self.interest_rate = rate
        logger.info(f"Interest rate changed successfully. New interest rate {self.interest_rate}")
    

    def create_account_number(self) -> str:
        rand_digits = random.randint(10**15, (10**16) - 1)
        logger.info(f"Account number created succesfully: LT99{rand_digits}")
        return f"LT99{rand_digits}"

    @classmethod
    def load(cls, id: int, db: dict) -> Account:
        for holder in db["holders"]:
            if holder["id"] == id:
                current_account = Account(
                    id,
                    holder["accounts"][0]["balance"],
                    str(holder["accounts"][0]["interest_rate"]),
                    holder["accounts"][0]["base_currency"],
                )
                current_account.id = holder["accounts"][0]["id"]
                current_account.account_number = holder["accounts"][0]["number"]
                current_account.is_active = holder["accounts"][0]["is_active"]

                logger.info("Account loaded succesfully.")
                return current_account
            else:
                continue
        
        logger.error("Account not loaded.")
        raise ValueError
