import pytest
from objects import Operation


@pytest.fixture
def operation_instance():
    test_operation_1 = Operation(
        transaction_id=484201274,
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
        to="МИР 9425591958944146"
    )
    test_operation_2 = Operation(transaction_id=608117766,
        date="2018-10-08T09:05:05.282282",
        state="CANCELED",
        operation_amount={
            "amount": "77302.31",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        description="Перевод с карты на счет",
        out_from="Visa Gold 652718339647772",
        to="Счет 385738166545817896"
                                 )

    return [test_operation_1, test_operation_2]


@pytest.fixture()
def operation_dict():
    return [{
    "id": 550607912,
    "state": "EXECUTED",
    "date": "2018-07-31T12:25:32.579413",
    "operationAmount": {
      "amount": "34380.08",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 8532498887072395",
    "to": "Счет 44238164562083919420"
  },
    {
        "id": 260972664,
        "state": "CANCELED",
        "date": "2018-01-23T01:48:30.477053",
        "operationAmount": {
            "amount": "2974.30",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 3414396880443483",
        "to": "Visa Gold 2684274847577419"
    },
        {}
    ]