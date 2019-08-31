# cards = [(s,v) for s in ("Hearts", "Diamonds", "Clubs", "Spades") for v in ("A","J","Q","K","2","3","4","5","6","7","8","9","10")]
cards = [(s,v) for s in ("Hearts", "Diamonds", "Clubs", "Spades") for v in range(100000)]
cards2 = [(s,v) for s in ("Hearts", "Diamonds", "Clubs", "Spades") for v in range(100000)]

def get_cards(n):
    result = []
    if n <= len(cards):
            for i in range(n):
                result.append(cards.pop())
    return result

def get_cards2(n):
    global cards2
    result = []
    if n <= len(cards2):
        result = cards2[-n:]
        cards2 = cards2[:len(cards2)-n]
    return result

# print(get_cards(52))
# print(f"cards have {len(cards)} left.")

# print(get_cards2(1))
# print(f"cards2 have {len(cards2)} left.")
# print(get_cards2(1))
# print(f"cards2 have {len(cards2)} left.")
# print(get_cards2(1))
# print(f"cards2 have {len(cards2)} left.")

# for n in range(1000):
#     get_cards2(52)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("get_cards(52)", setup="from __main__ import get_cards"))
    print(timeit.timeit("get_cards2(52)", setup="from __main__ import get_cards, get_cards2"))