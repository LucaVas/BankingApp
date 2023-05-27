import json


class Reader:
    def __init__(self, fname: str) -> None:
        self.fname = fname

    def __repr__(self) -> str:
        return f"Reader({self.fname})"

    def read_file(self) -> dict:
        try:
            with open(self.fname, "r+") as file:
                file_data = json.load(file)
                file.seek(0)
        except FileNotFoundError:
            print("File does not exist.")
            file_data = {}

        return file_data
