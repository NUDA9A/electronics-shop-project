import pytest
import csv
from src.item import Item
from src.instatiate_csv_error import InstatiateCSVError


@pytest.mark.parametrize('Item, expected', [
    (Item("Телевизор", 50_000, 100), 5_000_000),
    (Item("Ноутбук", 60_000, 250), 15_000_000)
])
def test_item_calculate(Item, expected):
    assert Item.calculate_total_price() == expected


@pytest.mark.parametrize('s, expected', [
    ('7', 7),
    ('7.03', 7),
    ('15', 15)
])
def test_str_to_num(s, expected):
    assert Item.string_to_number(s) == expected


file_len = 0
with open('../src/items.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        file_len += 1


@pytest.mark.parametrize('file, expected', [
    ('../src/items.csv', len(Item.all) + file_len + 4),
    ('aasdas.csv', len(Item.all) + file_len + 4),
    ('../homework-6/items.csv', len(Item.all) + file_len + 4)
])
def test_instantiate_from_csv(file, expected):
    try:
        Item.instantiate_from_csv(file)
        assert len(Item.all) == expected
    except InstatiateCSVError:
        assert True


@pytest.mark.parametrize('item, expected', [
    (Item.all[0], Item.all[0].name),
    (Item.all[1], Item.all[1].name)
])
def test_name_getter(item, expected):
    assert item.name == expected


@pytest.mark.parametrize('item, new_name, expected', [
    (Item.all[0], "Плазма", "Плазма"),
    (Item.all[1], "Макбук", "Макбук")
])
def test_name_getter(item, new_name, expected):
    item.name = new_name
    assert item.name == expected


@pytest.mark.parametrize('item, expected', [
    (Item.all[0], "Item('Телевизор', 50000, 100)"),
    (Item.all[1], "Item('Ноутбук', 60000, 250)")
])
def test_repr(item, expected):
    assert repr(item) == expected


@pytest.mark.parametrize('item, expected', [
    (Item.all[0], 'Телевизор'),
    (Item.all[1], 'Ноутбук')
])
def test_str(item, expected):
    assert str(item) == expected


@pytest.mark.parametrize('item, other, expected', [
    (Item("Телевизор", 50_000, 100), Item("Телевизор", 50_000, 140), 240),
    (Item("Телевизор", 50_000, 153), Item("Телевизор", 50_000, 534), 687)
])
def test_add(item, other, expected):
    assert item + other == expected
