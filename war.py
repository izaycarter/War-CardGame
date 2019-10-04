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
        # generates deck from deck class
        self.deck = Deck()
        # creates two players from player class
        self.player_one = Player("Isaiah")
        self.player_two = Player("Arianna")
        # splits deck evenlly to each player
        self.player_one.hand = self.deck.cards[::2]
        self.player_two.hand = self.deck.cards[1::2]
        self.play()

    def play(self):
        try:
            while len(self.player_one.hand) > 0 and len(self.player_two.hand) > 0:
                shuffle(self.player_one.hand)

                my_card = self.player_one.hand.pop(0)
                other_card = self.player_two.hand.pop(0)


                if my_card.value > other_card.value:
                    self.player_one.hand.extend([my_card,other_card])

                elif my_card.value < other_card.value:
                    self.player_two.hand.extend([my_card,other_card])

                elif my_card.value == other_card.value:
                    current_pot = [my_card, other_card]
                    if len(self.player_one.hand) >= 2 and len(self.player_two.hand) >= 2:
                        while my_card.value == other_card.value:

                            my_flip_card = self.player_one.hand.pop(0)
                            other_flip_card = self.player_two.hand.pop(0)
                            current_pot.extend([my_flip_card,other_flip_card])

                            my_card = self.player_one.hand.pop(0)
                            other_card = self.player_two.hand.pop(0)

                            if my_card.value > other_card.value:
                                current_pot.extend([my_card,other_card])
                                self.player_one.hand.extend(current_pot)

                            elif my_card.value < other_card.value:
                                current_pot.extend([my_card,other_card])
                                self.player_two.hand.extend(current_pot)

                    else:

                        my_card = self.player_one.hand.pop(0)
                        other_card = self.player_two.hand.pop(0)

                        if my_card.value > other_card.value:
                            current_pot.extend([my_card, other_card])
                            self.player_one.hand.extend(current_pot)

                        elif my_card.value < other_card.value:
                            current_pot.extend([my_card, other_card])
                            self.player_two.hand.extend(current_pot)
        except:
            pass

        if len(self.player_one.hand) == 0:
            print("YOU LOST")

        elif len(self.player_two.hand) == 0:
            print("YOU WIN!!!")


game = Game()
