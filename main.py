from utils import load_operations, get_instances, get_executed_operations, operations_sorter
from settings import OPERATIONS_PATH

def main():
    """
    Главная функция программы
    """
    operation = load_operations(OPERATIONS_PATH)
    instances = get_instances(operation)
    executed_operations = get_executed_operations(instances)
    sorted_operations = operations_sorter(executed_operations)
    for operation in sorted_operations[:5]:
        print(operation)


if __name__ == "__main__":
    main()