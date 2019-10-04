from random import shuffle


class Card:
    def __init__(self,suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return str(self.value)

class Deck:

    def __init__(self):
        self.cards = []
        self.buildDeck()
        shuffle(self.cards)


    def buildDeck(self):
        value = range(2,15)
        suit = ["hearts","clubs","spades","diamonds"]
        for s in suit:
            for v in value:
                self.cards.append(Card(s,v))

    # def shuffle(self):
    #     random.shuffle(self.cards)





class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    # def draw(self):
    #     self.hand.append(deck.cards.pop())




class Game:

    def __init__(self):

        self.deck = Deck()

        self.player_one = Player("Isaiah")
        self.player_two = Player("Arianna")

        self.player_one.hand = self.deck.cards[::2]
        self.player_two.hand = self.deck.cards[1::2]

        print(len(self.player_one.hand))
        print(len(self.player_two.hand))

game = Game()
