from Card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(s,v) for s in ("Hearts", "Diamonds", "Clubs", "Spades") for v in ("A","J","Q","K","2","3","4","5","6","7","8","9","10")]

    def count(self):
        return len(self.cards)

    def _deal(self, n=1):
        if len(self.cards) <= 0:
            raise ValueError("All cards have been dealt")
        
        result = []
        if n < len(self.cards):
            for i in range(n):
                result.append(self.cards.pop())
        return result

    def deal_card(self):
        return self._deal()

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

deck = Deck()

print(deck.cards)
print(deck)
print(deck.count())

print(deck.deal_card())
print(deck.deal_card())
print(deck.deal_card())
print(deck.count())