import pytest
import csv
from src.item import Item


@pytest.mark.parametrize('Item, expected', [
    (Item("Телевизор", 40_000, 100), 4_000_000),
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
    ('../src/items.csv', len(Item.all) + file_len)
])
def test_instantiate_from_csv(file, expected):
    Item.instantiate_from_csv(file)
    assert len(Item.all) == expected


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
    (Item.all[0], "Item('Телевизор', 40000, 100)"),
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
