import os
from dotenv import load_dotenv
import requests


load_dotenv()


def get_transaction(transaction: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    amount = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    if currency == "RUB":
        return float(amount)
    elif currency == "USD" or "EUR":
        try:
            API_URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"
            API_KEY = os.getenv("API_KEY")
            response = (requests.get
                        (API_URL.format(to="RUB", from_=currency, amount=amount), headers={"apikey": API_KEY}))
            if response.status_code == 200:
                data = response.json()
                return data["result"]
            else:
                print(f"Ошибка конвертации: {response.status_code}")
                return 0.0
        except requests.exceptions.RequestException as e:
            print(f"Ошибка конвертации: {e}")
            return 0.0
    else:
        print("Ошибка ввода")
        return 0.0
