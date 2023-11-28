# Вспомогательные функции
# Утилиты для чтения файлов

import json
from objects import Operation


def load_operations(data: str):
    """
    Открывает json-файл на чтение
    :param data: путь к файлу
    :return: json-файл с операциями
    """
    with open(data, "r", encoding="utf-8") as file:
        return json.load(file)


# Принимает список со словарями из предыдущей функции
# Возвращает список с экземплярами класса Operation
# Разложение операции на список данных
def get_instances(operations):
    """
    Разложение операций
    на удобный список данных
    :param operations: операции из json-файла
    :return: список операций. Одна такая операция содержит класс Operation со своими атрибутами внутри
    """
    operation_instances = []
    for operation in operations:
        if operation:
            operation_instance = Operation(
                transaction_id = operation["id"],
                state = operation["state"],
                date = operation["date"],
                operation_amount = operation["operationAmount"],
                description = operation["description"],
                out_from = operation.get("from", ""),
                to = operation["to"]
                )
            operation_instances.append(operation_instance)
    return operation_instances


# Отсеивание невыполненных операций
# Чтобы работа велась только с выполненными
def get_executed_operations(operations):
    """
    Отсеивание операций.
    Создание списка с исключительно EXECUTED-операциями
    :param operations: список операций-классов
    :return: список EXECUTED-операций
    """
    executed_operations = []
    for operation in operations:
        if operation.state == "EXECUTED":
            executed_operations.append(operation)
    return executed_operations

def get_date(operation):
    """
    pass
    (Не стал применять "лямбду" - еще не разобрался)
    :param operation:
    :return:
    """
    return operation.date


def operations_sorter(operations: list[Operation]) -> list[Operation]:
    """
    Сортировка операций по дате
    :param operations: опрацию с данными даты в одном виде
    :return: операции с данными
    """
    operations.sort(key=get_date, reverse=True)
    return operations
