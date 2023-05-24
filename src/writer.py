import json
from datetime import datetime, date
from reader import Reader

class Writer():
    def __init__(self, fname: str) -> None:
        self.fname = fname

    def __repr__(self) -> str:
        return f"Reader({self.fname})"

    def temp_write(self, holder, account, db: dict) -> None:
        output = db["holders"]
        data = {
            "id": holder.id,
            "first": holder.first_name,
            "last": holder.last_name,
            "birth_date": str(holder.birth_date),
            "password": str(holder.password),
            "is_blocked": holder.is_blocked,
            "onboarding_date": str(holder.onboarding_date),
            "accounts": [{
                "id": account.id,
                "number": account.account_number,
                "base_currency": account.currency,
                "balance": account.balance,
                "interest_rate": account.interest_rate,
                "is_active": account.is_active  
                }
            ],
            "connected_accounts": holder.connected_accounts          
        }   
        output.append(data)
        
    def write_to_file(self, data: dict) -> None:
        try:
            with open(self.fname, "w") as file:
                json.dump(data, file, indent=4)
        except (FileNotFoundError):
            print("File does not exist.")
    

