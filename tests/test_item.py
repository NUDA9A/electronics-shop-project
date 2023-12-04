import pytest
from src import item


@pytest.mark.parametrize('Item, expected', [
    (item.Item("Телевизор", 40_000, 100), 4_000_000),
    (item.Item("Ноутбук", 60_000, 250), 15_000_000)
])
def test_item_calculate(Item, expected):
    assert Item.calculate_total_price() == expected

