import pytest
from src.keyboard import Keyboard


@pytest.mark.parametrize('Keyboard, expected', [
    (Keyboard("HyperX", 5000, 100), 500000),
    (Keyboard("Corsair", 8000, 250), 2_000_000)
])
def test_item_calculate(Keyboard, expected):
    assert Keyboard.calculate_total_price() == expected


@pytest.mark.parametrize('s, expected', [
    ('7', 7),
    ('7.03', 7),
    ('15', 15)
])
def test_str_to_num(s, expected):
    assert Keyboard.string_to_number(s) == expected


@pytest.mark.parametrize('keyboard, expected', [
    (Keyboard.all[0], Keyboard.all[0].name),
    (Keyboard.all[1], Keyboard.all[1].name)
])
def test_name_getter(keyboard, expected):
    assert keyboard.name == expected


@pytest.mark.parametrize('keyboard, new_name, expected', [
    (Keyboard.all[0], "Dark Project", "Dark Proje"),
    (Keyboard.all[1], "Razer", "Razer")
])
def test_name_getter(keyboard, new_name, expected):
    keyboard.name = new_name
    assert keyboard.name == expected


@pytest.mark.parametrize('keyboard, expected', [
    (Keyboard("HyperX", 5000, 100), "Keyboard('HyperX', 5000, 100)"),
    (Keyboard("Razer", 8000, 250), "Keyboard('Razer', 8000, 250)")
])
def test_repr(keyboard, expected):
    assert repr(keyboard) == expected


@pytest.mark.parametrize('keyboard, expected', [
    (Keyboard("HyperX", 5000, 100), 'HyperX'),
    (Keyboard("Razer", 8000, 250), 'Razer')
])
def test_str(keyboard, expected):
    assert str(keyboard) == expected


@pytest.mark.parametrize('keyboard, other, expected', [
    (Keyboard("HyperX", 5000, 100), Keyboard("Razer", 5000, 140), 240),
    (Keyboard("SteelSeries", 8000, 153), Keyboard("Dark Project", 10000, 534), 687)
])
def test_add(keyboard, other, expected):
    assert keyboard + other == expected


@pytest.mark.parametrize('keyboard, language, expected', [
    (Keyboard("HyperX", 5000, 100), "EN", "RU")
])
def test_change_lang(keyboard, language, expected):
    assert keyboard.language == language
    keyboard.change_lang()
    assert keyboard.language == expected