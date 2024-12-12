from playing_cards.deck import Deck
from playing_cards.card import Card
import re


class Bank(object):

    def __init__(self):
        self._size = 0
        self._const_refill = True
        self._bank = []

    def __str__(self):
        _bank_s = ""
        for _position in range(len(self._bank)):
            _bank_s += f"{_position + 1}: "
            if isinstance(self._bank[_position], Card):
                _bank_s += self._bank[_position].long_short()
            else:
                _bank_s += "*****"

            if _position != len(self._bank) - 1:
                _bank_s += ", "
        return _bank_s

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, bank_size):
        self._size = bank_size

    @property
    def const_refill(self):
        return self._const_refill

    @const_refill.setter
    def const_refill(self, refill):
        self._const_refill = refill

    def ask_refill(self):
        while True:
            _const_refill_ans = input("Would you like to constantly refill your bank? [1/Yes, 0/No]\n")
            if _const_refill_ans.lower() == "yes" or _const_refill_ans == "1":
                self._const_refill = True
                return True
            elif _const_refill_ans.lower() == "no" or _const_refill_ans == "0":
                self._const_refill = False
                return False
            else:
                print("It was a yes or no question c'mon man!")
                continue

    def ask_size(self):
        while True:
            try:
                self._size = int(input("How many cards would you like in your bank at a time?\n"))
            except ValueError:
                self._size = None
                print("You must be a little slow, cause that's not a whole number.")

            if self._size is None:
                pass
            elif self._size > 25 or self._size < 1:
                print("Your bank cannot be larger than 25 cards or less than 1.")
            else:
                return self._size

    def fill(self, deck: Deck):
        _ele = 0
        try:
            for _ele in range(self._size):
                if isinstance(self._bank[_ele], str):
                    self._bank[_ele] = deck.draw()
        except IndexError:
            if _ele > self._size:
                print("How did we get here? You went beyond the range of the bank.")
            else:
                for _ele in range(self._size - len(self._bank)):
                    self._bank.append(deck.draw())

    def get_card(self, index: int):
        try:
            return self._bank[index]

        except IndexError:
            return None

    def select_card(self) -> Card:
        numeric_const_pattern = r"[-+]?(?:\d*\.*\d+)"  # regex for extracting +/- ints and floats
        rx = re.compile(numeric_const_pattern, re.VERBOSE)
        if self._size == 1:
            _card = self._bank.pop(0)
            self._bank.append("*****")
            return _card
        while True:
            _position = input("Enter position of desired card:\n")
            if len(_position) == 1:
                _position = rx.findall(_position)
                try:
                    _position = int(_position[0]) - 1
                except ValueError:
                    print("You need to enter a positive integer for this one buddy. Try again.")

                if _position in range(self._size):
                    if isinstance(self.get_card(_position), Card):
                        _card = self._bank.pop(_position)
                        self._bank.append("*****")
                        return _card
                    else:
                        print("That's not part of your hand anymore, its just a placeholder. Pick one of the cards.")
                else:
                    print("Position out of bounds, pick something inside the range of cards in your bank this time.")
            else:
                print("Only enter one number.")

    def check_empty(self) -> bool:
        for _i in range(len(self._bank)):
            if isinstance(self._bank[_i], Card):
                return False
        return True
