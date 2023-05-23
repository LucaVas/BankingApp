import requests
from requests import Response
import json
from decouple import config

API_KEY = config('EXCHANGE_KEY')
    
class ApiFetcher():
    def __init__(self, url: str, key:str, base_currency: str):
        self.url = url
        self.key = key
        self.base_currency = base_currency


    def fetch(self) -> dict:
        response = requests.get(f"{self.url}{self.key}&base_currency={self.base_currency}")
        data = self.parse(response)
        return data
        # return self.prettify(data)

    def parse(self, r: Response) -> dict:
        return r.json()

    def prettify(self, json_data: dict) -> str:
        return json.dumps(json_data, indent = 3)



def fetch_api(url: str, key: str, base_currency: str):
    api_fetcher = ApiFetcher(url, key, base_currency)
    return api_fetcher.fetch()

data = fetch_api("https://api.freecurrencyapi.com/v1/latest?apikey=", API_KEY, "EUR")
print(data['data'])