import random


class Card:
    def __init__(self, type_of_card, value):
        self.type_of_card = type_of_card
        self.value = value


class Deck:

    def __init__(self):
        self.cards = [None] * 36
        suits = ['heart', 'diamond', 'club', 'spade']
        values = ['6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        for suit in suits:
            for value in values:
                i = random.randint(0, 35)
                while self.cards[i]:
                    i = random.randint(0, 35)
                self.cards[i] = Card(suit, value)

    def shuffle(self):
        return random.sample(self.cards, len(self.cards))

    def current_number(self):
        return len(self.cards)

    def get_card(self):
        temp = self.cards.pop()
        return temp.type_of_card, temp.value


a = Deck()
b = Deck()
print(a.get_card())
print(a.current_number())
print(b.current_number())
