import json
from datetime import datetime
import logging
from typing import Union

# setting up logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler("./main_logs/writer.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


class Writer:
    def __init__(self, fname: str) -> None:
        self.fname = f"../{fname}"
        logger.info(f"Writer object created succesfully. {self.__repr__()}")

    def __repr__(self) -> str:
        return f"Reader({self.fname})"

    def temp_write_history(
        self,
        holder,
        action: str,
        amount: float,
        recipient: str,
        datestamp: datetime,
        reason: str,
        db: dict,
    ) -> None:
        output = db["history"]
        data = {
            "id": holder.id,
            "action": action,
            "amount": amount,
            "reason": reason,
            "recipient_account": recipient,
            "datestamp": str(datestamp),
        }

        logger.info(f"Action data added succesfully to temporary database: {data}")
        output.append(data)

    def temp_write(self, holder, account, db: dict) -> None:
        output = db["holders"]
        data = {
            "id": holder.id,
            "first": holder.first_name,
            "last": holder.last_name,
            "birth_date": str(holder.birth_date),
            "password": holder.password.decode("utf-8"),
            "is_blocked": holder.is_blocked,
            "onboarding_date": str(holder.onboarding_date),
            "last_access": str(holder.last_access),
            "accounts": [
                {
                    "id": account.id,
                    "number": account.account_number,
                    "base_currency": account.currency,
                    "balance": account.balance,
                    "interest_rate": account.interest_rate,
                    "is_active": account.is_active,
                }
            ],
            "connected_accounts": holder.connected_accounts,
        }

        for idx, holder in enumerate(output):
            if holder["id"] == data["id"]:
                output[idx] = data
                return
            continue

        logger.info(f"Holder data succesfully written to temporary database: {data}")
        output.append(data)

    def write_to_file(self, data: dict) -> None:
        try:
            with open(self.fname, "r+") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            logger.exception("FileNotFoundError")

        logger.info("Temporary database written to database succesfully.")
