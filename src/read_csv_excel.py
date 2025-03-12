import os
import pandas as pd


cur_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(cur_dir, "../logs/read_csv_excel.log")
abs_file_path = os.path.abspath(path)


def read_file_csv(file_path: str) -> list[dict]:
    """Чтение CSV-файла"""
    try:
        transactions_df = pd.read_csv(file_path, delimiter=";")
        result = transactions_df.to_dict(orient="records")
        return result
    except Exception:
        return []


def read_file_excel(file_path: str) -> list[dict]:
    """Чтение EXCEL-файла"""
    try:
        transactions_df = pd.read_excel(file_path, delimiter=";")
        result = transactions_df.to_dict(orient="records")
        return result
    except Exception:
        return []
