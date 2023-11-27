# Утилиты для чтения файлов
import json


def load_operations(data: str):
    """
    Открывает json-файл на чтение
    :param data: путь к файлу
    :return: json-файл с операциями
    """
    with open(data, "r", encoding="utf-8") as file:
        return json.load(file)