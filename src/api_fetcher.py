import requests
from requests import Response
import json
import logging

# setting up logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler("api_fetcher.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class ApiFetcher:
    def __init__(self, url: str, key: str, base_currency: str):
        self.url = url
        self.key = key
        self.base_currency = base_currency

        logger.info("ApiFetcher created.")

    def fetch(self) -> dict:
        if self.base_currency == "":
            try:
                response = requests.get(f"{self.url}{self.key}")
            except Exception as e:
                logger.exception("Api fetcher exception")
            data = self.parse(response)
        else:
            try:
                response = requests.get(
                    f"{self.url}{self.key}&base_currency={self.base_currency}"
                )
            except Exception:
                logger.exception("Api fetcher exception")
            data = self.parse(response)
        
        logger.info(f"API fetched succesfully")
        return data
        # return self.prettify(data)

    def parse(self, r: Response) -> dict:
        return r.json()

    def prettify(self, json_data: dict) -> str:
        return json.dumps(json_data, indent=3)
