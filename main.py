import sys
from bank import Bank
from card import Card
from deck import Deck
from table import Table


def test() -> int:
    print(str(Table().total_scores_str))

    return 1

def main() -> int:
    dealt = 0
    deck = Deck()
    deck.shuffle()
    table = Table()
    temp_table = table
    bank = Bank()
    selected_card: Card
    selected_position: list
    auto_refill: bool

    # Instructions
    print("\nWelcome to Poker Square / Poker Solitaire!\n")
    print("Your objective is to make the best poker hands on a 5 x 5 grid both horizontally and vertically.")
    print("There are two points systems for hands, The American and the English. Please google a refrence page to play along with.\n")
    print("You may choose to draw one card at a time, or multiple cards at once.")
    print("You may also choose whether you refill your card bank every turn or wait until it is empty.\n")
    print("'Cause I'm a nice programmer, and I care for your well being and enjoyment over my own sanity.\n")
    print("For more detailed rules, please refer to the game's wiki, or google it, youtube it, idc.")
    print("That's all from me, have fun!\n")

    # handicaps
    bank_size = bank.ask_size()
    if bank_size == 1:
        auto_refill = True
    elif bank_size == 25:
        auto_refill = False
    else:
        auto_refill = bank.ask_refill()

    bank.fill(deck)
   
    while table.is_full() is False:
        dealt += bank_size

        print(table)
        print(bank)

        selected_card = bank.select_card()

        selected_position = table.select_location()
        table.play_card(selected_card, *selected_position)
        if auto_refill == True or bank.check_empty() == True:
            bank.fill(deck)

    print(table)
    table.score()
    print(f"Total scores: {table.total_scores_str}")
    if table.total_scores.get("english") >= 70 and table.total_scores.get("American") >= 200 :
        print("WOW! You won by all standards (A \u2265 200 & B \u2265 70), Congratulations, and nice work!")

    elif table.total_scores.get("American") >= 200:
        print("You Won by American standards (A \u2265 200), Congratulations!")

    elif table.total_scores.get("english") >= 70:
        print("You Won by english standards (B \u2265 70, Congratulations!")
    else:
        print("Bummer, you lost, better luck next time.")


    return 1

if __name__ == '__main__':
    sys.exit(main())
    #sys.exit(test())
