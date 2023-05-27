# Banking Application

The BankingApp is a Python GUI application built using Tkinter and CustomTkinter libraries. 
It provides a graphical interface for managing bank accounts, performing currency exchange, and displaying account transaction history. The application offers various frames and widgets to visualize account information, perform transactions, and interact with the user.

For the purpose of this application, I used the name and information of the "Bank of America Corp.".

## Features

- **BalanceFrame**: Displays the current balance of an account, including the amount and currency.
- **BankInfoFrame**: Provides information about the bank, such as the number of shares, share price, and shares price delta.
- **ExchangeFrame**: Allows users to perform currency exchange by selecting the desired currency and displaying the exchanged balance below the current account balance.
- **HolderInfoFrame**: Shows details about the account holder, including the holder's name, currency, and interest rate chosen.
- **TreeViewFrame**: Displays a tree view of transaction history, including the action, amount, recipient account, and date.

## Dependencies

The application relies on the following dependencies:

- Python 3.x
- Tkinter: Python's standard library for creating graphical user interfaces.
- customtkinter: A custom module/library that extends the functionality of Tkinter and provides custom widgets.
- python-decouple: Library responsible for uploading your API keys from the .env file.
- python_bcrypt: Library responsible for hashing password.
- Requests: Library responsible for handling API requests.
- shortuuid: Library responsible for creating short unique ID for accounts and user.

APIs:

- Alpha Vantage, https://www.alphavantage.co : API for retrieving market information, useful to get market data about Bank of America Corp. 
- FreecurrencyAPI, https://freecurrencyapi.com : for retrieving currency exchange rates.

## Installation

1. Clone the repository: `git clone https://github.com/LucaVas/BankingApp.git`
2. Navigate to the project directory: `cd BankingApp`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Register new accounts in API dependency websites for personal API keys.
5. Create an .env file where you will store the API keys: `code .env`. API keys must be in the following structure: "EXCHANGE_KEY=your_key" and "MARKET_KEY=your_key"

## Usage

To run the Banking Application, position yourself in the main folder, and execute the following command:

```
python3 src/main.py
```

Upon running the application, the graphical user interface will be displayed, presenting various frames and widgets for interacting with the banking features. You can navigate through the different frames and perform actions such as checking the balance, exchanging currencies, and viewing transaction history.

## Contributions

Contributions to the Banking Application are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is not licensed. You are free to modify and distribute the application.

## Acknowledgments

The Banking Application was developed using the Tkinter library and customtkinter module.
