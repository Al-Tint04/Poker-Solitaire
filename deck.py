from card import Card
import random


class Deck(object):

    def __init__(self):

        # Suits: Icon in CHSD order
        self._suits = {"Clubs": "\u2663",
                       "Hearts": "\u2665",
                       "Spades": "\u2660",
                       "Diamonds": "\u2666"}

        # card.py faces, use index for value
        self._faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self._deck = []
        self.build()
        self._bank = []

    def __str__(self):
        _deck_s = ""
        _dl = self.deck_list()
        for i in range(len(self._deck)):
            _deck_s += "{}\n".format(_dl[i])
        return _deck_s

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.deck_list())

    def build(self):
        for s in self._suits:
            for f in self._faces:
                cardx = Card(f, s)
                self._deck.append(cardx)

    def deck_list(self) -> list:
        _deck_list = []
        for i in range(len(self._deck)):
            _deck_list.append(str(self._deck[i]))
        return _deck_list

    def shuffle(self):
        random.shuffle(self._deck)

    # for testing only
    def get_card(self, index: int) -> Card:
        return self._deck[index]

    def draw(self) -> Card:
        return self._deck.pop(0)

    def deal(self, cards: int):
        _pile = []
        for i in range(cards):
            _pile.append(self._deck.pop(0))
        return _pile

    def find_card(self, card: Card):

        _dl = self.deck_list()

        try:
            return _dl.index(card)

        except ValueError:
            return None

    # For Testing
    def put_card(self, card: Card, index: int):
        self._deck.insert(index, card)
