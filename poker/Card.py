class Card:
    def __init__(self, suit, value):
        self.set_suit(suit)
        self.set_value(value)

    def __repr__(self):
        return f"{self._value} of {self._suit}"

    def set_suit(self, v):
        if v not in ("Hearts", "Diamonds", "Clubs", "Spades"):
            raise ValueError("suite should be one of: ('Hearts', 'Diamonds', 'Clubs', 'Spades')")
        self._suit = v

    def get_suit(self):
        return self._suit

    def set_value(self, v):
        if v not in ("A","J","Q","K","2","3","4","5","6","7","8","9","10"):
            raise ValueError('suite should be one of: ("A","J","Q","K","2","3","4","5","6","7","8","9","10")')
        self._value = v

    def get_value(self):
        return self._value

    suit = property(get_suit, set_suit)
    value = property(get_value, set_value)