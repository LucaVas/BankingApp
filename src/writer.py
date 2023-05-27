import json
from datetime import datetime


class Writer:
    def __init__(self, fname: str) -> None:
        self.fname = fname

    def __repr__(self) -> str:
        return f"Reader({self.fname})"

    def temp_write_history(
        self,
        holder,
        action: str,
        amount: float,
        recipient: str,
        datestamp: datetime,
        reason,
        db: dict,
    ) -> None:
        output = db.get("history")
        data = {
            "id": holder.id,
            "action": action,
            "amount": amount,
            "reason": reason,
            "recipient_account": recipient,
            "datestamp": str(datestamp),
        }

        output.append(data)

    def temp_write(self, holder, account, db: dict) -> None:
        output = db.get("holders")
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
        output.append(data)

    def write_to_file(self, data: dict) -> None:
        try:
            with open(self.fname, "r+") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            print("File does not exist.")
