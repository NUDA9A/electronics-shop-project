from src.item import Item
from src.mixin_keyboard import MixinKeyboard


class Keyboard(Item, MixinKeyboard):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
