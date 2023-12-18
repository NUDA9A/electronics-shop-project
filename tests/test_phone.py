import pytest
import csv
from src.phone import Phone


@pytest.mark.parametrize('Phone, expected', [
    (Phone("Iphone", 50_000, 100, 1), 5_000_000),
    (Phone("Samsung", 60_000, 250, 2), 15_000_000)
])
def test_item_calculate(Phone, expected):
    assert Phone.calculate_total_price() == expected


@pytest.mark.parametrize('s, expected', [
    ('7', 7),
    ('7.03', 7),
    ('15', 15)
])
def test_str_to_num(s, expected):
    assert Phone.string_to_number(s) == expected


@pytest.mark.parametrize('phone, expected', [
    (Phone.all[0], Phone.all[0].name),
    (Phone.all[1], Phone.all[1].name)
])
def test_name_getter(phone, expected):
    assert phone.name == expected


@pytest.mark.parametrize('phone, new_name, expected', [
    (Phone.all[0], "Iphone", "Iphone"),
    (Phone.all[1], "Samsung", "Samsung")
])
def test_name_getter(phone, new_name, expected):
    phone.name = new_name
    assert phone.name == expected


@pytest.mark.parametrize('phone, expected', [
    (Phone("Iphone", 50_000, 100, 1), "Phone('Iphone', 50000, 100, 1)"),
    (Phone("Samsung", 60_000, 250, 2), "Phone('Samsung', 60000, 250, 2)")
])
def test_repr(phone, expected):
    assert repr(phone) == expected


@pytest.mark.parametrize('phone, expected', [
    (Phone("Iphone", 50_000, 100, 1), 'Iphone'),
    (Phone("Samsung", 60_000, 250, 2), 'Samsung')
])
def test_str(phone, expected):
    assert str(phone) == expected


@pytest.mark.parametrize('phone, other, expected', [
    (Phone("Iphone", 50_000, 100, 1), Phone("Samsung", 50_000, 140, 2), 240),
    (Phone("REDMI NOTE 865 XXL PRO SUPER", 50_000, 153, 45), Phone("Samsung", 50_000, 534, 2), 687)
])
def test_add(phone, other, expected):
    assert phone + other == expected
