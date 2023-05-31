import json
import logging

# setting up logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler("./main_logs/reader.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class Reader:
    def __init__(self, fname: str) -> None:
        self.fname = f"../{fname}"
        logger.info(f"Reader object successfully created: {self.__repr__()}")

    def __repr__(self) -> str:
        return f"Reader({self.fname})"

    def read_file(self) -> dict:
        try:
            with open(self.fname, "r+") as file:
                file_data = json.load(file)
                file.seek(0)
        except FileNotFoundError:
            logger.exception("FileNotFoundError")
            print("File does not exist.")
            file_data = {}
        
        logger.info(f"File read successfully: {file_data}")
        return file_data
