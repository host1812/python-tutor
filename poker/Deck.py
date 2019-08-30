from Card import Card
from random import shuffle as rshuffle

class Deck:
    def __init__(self):
        self.cards = [Card(s,v) for s in ("Hearts", "Diamonds", "Clubs", "Spades") for v in ("A","J","Q","K","2","3","4","5","6","7","8","9","10")]

    def count(self):
        return len(self.cards)

    def _deal(self, n=1):
        if len(self.cards) <= 0:
            raise ValueError("All cards have been dealt")
        
        result = []
        cards_to_deal = min(n,len(self.cards))
        for i in range(cards_to_deal):
            result.append(self.cards.pop())
        return result

    def deal_card(self):
        return self._deal()

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError("Only full decks can be shuffled")
        rshuffle(self.cards)

    def deal_hand(self, n):
        return self._deal(n)

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

deck = Deck()
print(deck.cards)
deck.shuffle()
print(deck.cards)
# print(deck.cards)
# print(deck)
# print(deck.count())

# print(deck.deal_card())
# deck.shuffle()
# print(deck.deal_card())
# print(deck.deal_card())
# print(deck.count())

# print(deck.deal_hand(15))
# print(deck.count())

# print(deck.deal_hand(25))
# print(deck.count())

# print(deck.deal_hand(5))
# print(deck.count())

# print(deck.deal_hand(9))
# print(deck.count())