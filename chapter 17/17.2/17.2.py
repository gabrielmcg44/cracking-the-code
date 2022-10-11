import random


class Deck:
    def __init__(self):
        self.cards = [number + suit
                      for number in [str(num) for num in range(1, 14)]
                      for suit in ["♥", "♦", "♣", "♠"]
                      ]

    def shuffle(self):  # O(N²)
        not_used = [card for card in self.cards]
        for i in range(52):
            index = random.randint(0, 51 - i)
            self.cards[i] = not_used[index]
            not_used.pop(index)

    def shuffle_better(self):  # O(N)
        for i in range(0, 51):
            index = random.randint(0, i)
            temp = self.cards[index]
            self.cards[index] = self.cards[i]
            self.cards[i] = temp


deck = Deck()
print(deck.cards)
deck.shuffle_better()
print(deck.cards)
