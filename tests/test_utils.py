from utils import get_instances, load_operations, get_executed_operations, operations_sorter
from objects import Operation

def test_get_instance(operation_dict, test_path="test_operations.json"):
    operations = get_instances(operation_dict)
    load = load_operations(test_path)
    assert isinstance(operations, list)
    assert isinstance(operations[0], Operation)
    assert len(operations) == 2 #а не 3
    assert operations[0].transaction_id == 550607912
    assert load == {"test_text": "text_for_test"}


def test_get_executed_operations(operation_instance):
    operations = get_executed_operations(operation_instance)
    assert isinstance(operations, list)
    assert isinstance(operations[0], Operation)
    assert len(operations) == 1
    assert operations[0].state == "EXECUTED"

def test_operations_sorter(operation_instance):
    operations = operations_sorter(operation_instance)
    assert isinstance(operations, list)
    assert isinstance(operations[0], Operation)
    assert len(operations) == 2
    assert operations[0].date > operations[1].date