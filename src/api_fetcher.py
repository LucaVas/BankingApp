import requests
from requests import Response
import json


    
class ApiFetcher():
    def __init__(self, url: str, key:str, base_currency: str):
        self.url = url
        self.key = key
        self.base_currency = base_currency


    def fetch(self) -> dict:
        if self.base_currency == "":
            response = requests.get(f"{self.url}{self.key}")
            data = self.parse(response)
        else:
            response = requests.get(f"{self.url}{self.key}&base_currency={self.base_currency}")
            data = self.parse(response)
        
        return data
        # return self.prettify(data)

    def parse(self, r: Response) -> dict:
        return r.json()

    def prettify(self, json_data: dict) -> str:
        return json.dumps(json_data, indent = 3)