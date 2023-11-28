from datetime import datetime
from objects import Operation


def test_operation_date_converter(operation_instance):
    operation = Operation(transaction_id=484201274,
        date="2019-04-11T23:10:21.514616",
        state="EXECUTED",
        operation_amount={
            "amount": "62621.51",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        description="Перевод с карты на карту",
        out_from="МИР 8193813157568899",
        to="МИР 9425591958944146")
    assert operation.date_converter("2019-04-11T23:10:21.514616") == datetime.date(2019, 4, 11)


def test_payment_info_converter(operation_instance):
    operation = Operation(transaction_id=484201274,
        date="2019-04-11T23:10:21.514616",
        state="EXECUTED",
        operation_amount={
            "amount": "62621.51",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        description="Перевод с карты на карту",
        out_from="МИР 8193813157568899",
        to="МИР 9425591958944146")

    assert operation.payment_info_converter("МИР 8193813157568899") == "МИР 8193 81** **** 8899"