from src.item import Item
from src.instatiate_csv_error import InstatiateCSVError

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv("item.csv")
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    try:
        Item.instantiate_from_csv()
    except InstatiateCSVError as ex:
        print(ex.message)
    # InstantiateCSVError: Файл item.csv поврежден
