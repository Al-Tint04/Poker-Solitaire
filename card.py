class Card(object):

    def __init__(self, face, suit: str):
        face = str(face).capitalize()
        suit = str(suit).capitalize()
        # Suits: Icon in CHSD order
        self._suits = {"Clubs": "\u2663",
                       "Hearts": "\u2665",
                       "Spades": "\u2660",
                       "Diamonds": "\u2666"}

        # card.py faces, use index for value
        self._faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        self._face = face
        self._suit = suit
        self._icon = self._suits.get(self._suit)
        self._ptvalue = ((self._faces.index(self._face)) + 2)

    def __str__(self):
        return "{} of {}".format(self._face, self._suit)

    def __repr__(self):
        return self.__str__()

    def shorthand(self) -> str:
        if self._face == "10":
            return "{}{}".format(self._face[:2], self._icon)
        else:
            return "{}{}".format(self._face[0], self._icon)

    def long_short(self) -> str:
        return f"{self.__str__()} ({self.shorthand()})"

    # <editor-fold desc="Getters">
    @property
    def face(self) -> str:
        return self._face

    @property
    def suit(self) -> str:
        return self._suit

    @property
    def icon(self) -> str:
        return self._icon

    @property
    def ptvalue(self) -> int:
        return self._ptvalue

    # </editor-fold>

    # <editor-fold desc="Setters">
    @face.setter
    def face(self, new_face):
        new_face = str(new_face).capitalize()
        if new_face in self._faces:
            self._face = new_face
            self._ptvalue = self._faces.index(self._face) + 2
        else:
            print("Error: Invalid card face.")

    @suit.setter
    def suit(self, new_suit):
        new_suit = new_suit.capitalize()
        if new_suit in self._suits:
            self._suit = new_suit
            self._icon = self._suits.get(self._suit)
        else:
            print("Error: Invalid card suit.")

    # </editor-fold>
