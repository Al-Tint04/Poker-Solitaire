from playing_cards.card import Card
from collections import Counter


class Table(object):

    def __init__(self):
        self._columns = 5
        self._rows = 5
        self._table = [[f"*****" for _row in range(self._rows)] for _col in range(self._columns)]
        self._row_scores = {
            "American": {f"Row {_r + 1}": 0 for _r in range(self._rows)},
            "English": {f"Row {_r + 1}": 0 for _r in range(self._rows)},
        }
        self._col_scores = {
            "American": {f"Column {_c + 1}": 0 for _c in range(self._columns)},
            "English": {f"Column {_c + 1}": 0 for _c in range(self._columns)},
        }

        self._total_scores = {
            "American": 0,
            "English": 0}
        self.set_total_scores()

    @property
    def row_scores(self):
        return self._row_scores

    @property
    def col_scores(self):
        return self._col_scores

    @property
    def total_scores(self):
        return self._total_scores

    @property
    def total_scores_str(self) -> str:
        return f"American: {self.total_scores.get('American')}, " \
               f"English: {self.total_scores.get('English')}"

    def __str__(self):
        _table_s = "\n\t\t "
        for _c in range(self._columns):
            _table_s += f"{chr(65 + _c): ^5}  "
        _table_s += "\n\t\t " + (u'\u2500' * 35) + "\n"
        for _row in range(self._columns):
            _table_s += f"\t{_row + 1}\t"
            for _col in range(self._rows):
                if isinstance(self._table[_row][_col], Card):
                    _table_s += f"{self._table[_row][_col].shorthand(): ^7}"
                else:
                    _table_s += " {} ".format(self._table[_row][_col])
            _table_s += "| A:{}, E:{}\n".format(self._row_scores["American"][f"Row {_row + 1}"],
                                                self._row_scores["English"][f"Row {_row + 1}"])
            _table_s += "\n"

        _table_s += f"\t\t " + (u'\u2500' * 35) + "\n\t\t "

        for _row in range(self._columns):
            _table_s += " A:{:^3}|".format(self._col_scores["American"][f"Column {_row + 1}"])
        _table_s += "\n\t\t "
        for _row in range(self._columns):
            _table_s += " E:{:^3}|".format(self._col_scores["English"][f"Column {_row + 1}"])

        _table_s += f"\n\n\t{self.total_scores_str}"
        return _table_s

    def play_card(self, card: Card, column: int, row: int):
        self._table[row - 1][column - 1] = card

    def get_slot(self, column: int, row: int):
        return self._table[column][row]

    def column(self, column: int) -> list:
        return [row[column] for row in self._table]

    def row(self, row: int) -> list:
        return self._table[row]

    def rank(self, hand: list[Card]):
        try:
            isinstance(hand, list)
        except TypeError:
            return None

        if len(hand) != 5:
            return None

        _hand = hand
        _hand = sorted(_hand, key=lambda card: card.ptvalue)
        _hand_s = set(_hand[i].face for i in range(len(_hand)))
        _hand_faces = Counter(card.face for card in _hand)

        match len(_hand_s):

            case 2:
                if 4 in _hand_faces.values():
                    return [50, 16]  # Four of a kind
                else:
                    return [25, 10]  # "Full House"
            case 3:

                if 3 in _hand_faces.values():
                    return [10, 6]  # 3 of a Kind
                else:
                    return [5, 3]  # 2 Pair
            case 4:
                return [2, 1]  # pair
            case 5:
                _check_flush = self.flush(_hand)
                _check_straight = self.straight(_hand)

                if _check_straight is True:
                    if _check_flush is True:
                        if _hand[0].ptvalue == 10:
                            return [100, 30]  # Royal flush
                        else:
                            return [75, 30]  # straight flush
                    else:
                        return [15, 12]  # Straight
                elif _check_flush is True:
                    return [20, 5]  # Flush
                else:
                    return [0, 0]  # Junk

    @staticmethod
    def straight(hand: list[Card]) -> bool:
        count = 0
        _low_straight = ["2", "3", "4", "5", "Ace"]
        _hand_faces = [card.face for card in hand]
        if _low_straight == _hand_faces:
            return True
        for card in range(len(hand) - 1):
            if hand[card].ptvalue + 1 == hand[(card + 1)].ptvalue:
                count += 1

        if count == 4:
            return True
        else:
            return False

    @staticmethod
    def flush(hand: list[Card]) -> bool:
        _suit_set = {getattr(card, "suit") for card in hand}
        if len(_suit_set) == 1:
            return True
        else:
            return False

    def score(self):
        for _r in range(self._rows):
            self._row_scores["American"][f"Row {_r + 1}"] = self.rank(self.row(_r))[0]
            self._row_scores["English"][f"Row {_r + 1}"] = self.rank(self.row(_r))[1]


        for _c in range(self._columns):
            self._col_scores["American"][f"Column {_c + 1}"] = self.rank(self.column(_c))[0]
            self._col_scores["English"][f"Column {_c + 1}"] = self.rank(self.column(_c))[1]

        self.set_total_scores()


    def set_total_scores(self):
        self._total_scores = {
            "American": sum(self._row_scores["American"].values()) + sum(self._col_scores["American"].values()),
            "English": sum(self._row_scores["English"].values()) + sum(self._col_scores["English"].values())}

    @staticmethod
    def select_location() -> list:
        _mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

        while True:
            _coordinates = list(input("Enter Battleship Coordinate for your next play [A1 - E5]:\n").strip().upper())

            if len(_coordinates) != 2:
                print("Enter exactly two characters")
            elif _coordinates[0] not in 'ABCDE' or _coordinates[1] not in '12345':
                print("Haven't you played battleship? A1 - E5 only. And no going over the board.")
                continue
            else:
                _coordinates[0] = _mapping[_coordinates[0]]
                _coordinates[1] = int(_coordinates[1])
                return _coordinates



    def is_full(self) -> bool:
        for _row in range(self._rows):
            for _col in range(self._columns):
                if not isinstance(self._table[_row][_col], Card):
                    return False
        return True
