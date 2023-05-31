from __future__ import annotations
from datetime import datetime, date
import shortuuid # type: ignore
import logging

# setting up logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler("./main_logs/holder.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class Holder:
    def __init__(self, first: str, last: str, birth_date: date, id=shortuuid.uuid()):
        self.id = id
        self.first_name = first
        self.last_name = last
        self.birth_date = birth_date
        self._password: bytes
        self.is_blocked = False
        self.onboarding_date = datetime.now()
        self.last_access = datetime.now()
        self.accounts: list[str] = ["XXXX"]
        self.connected_accounts: list[str] = []

        logger.info(f"Holder object created successfully. {self.__repr__()}")

    def __str__(self) -> str:
        return f"Account holder: {self.first_name} {self.last_name}.\nDate of Birth: {self.birth_date}\nOnboarding date: {self.onboarding_date}\nAccount blocked: {self.is_blocked}"

    def __repr__(self) -> str:
        return f"Holder({self.id},'{self.first_name}','{self.last_name}',Birth:{self.birth_date},Blocked:{self.is_blocked},Onboarded:{self.onboarding_date})"

    @property
    def password(self) -> bytes:
        return self._password

    @password.setter
    def password(self, password: bytes) -> None:
        self._password = password

    def block(self, is_blocked: bool) -> None:
        if is_blocked is True:
            self.is_blocked = True
            logger.info("Holder blocked.")
        elif is_blocked is False:
            self.is_blocked = False
            logger.info("Holder unblocked.")
        else:
            logger.error("Holder 'is_blocked' attribute cannot be set.")
            raise ValueError

    @classmethod
    def load(cls, login_window, db: dict) -> Holder | None:
        for holder in db["holders"]:
            if holder["id"] == login_window.id:
                current_holder = Holder(
                    holder["first"],
                    holder["last"],
                    date.fromisoformat(holder["birth_date"]),
                )
                current_holder.id = holder["id"]
                current_holder.password = bytes(holder["password"], "utf-8")
                current_holder.is_blocked = holder["is_blocked"]
                current_holder.onboarding_date = datetime.fromisoformat(
                    holder["onboarding_date"]
                )
                current_holder.last_access = login_window.last_access
                current_holder.accounts = [
                    account["number"] for account in holder["accounts"]
                ]
                current_holder.connected_accounts = [
                    account for account in holder["connected_accounts"]
                ]

                logger.info(f"Current holder loaded correctly: {current_holder}")
                return current_holder
            else:
                continue
        
        logger.error("Current holder cannot be loaded.")
        raise Exception
