import random

class Card():
    def __init__(self, rank):
        self.rank = rank
    def __gt__(self, o):
        return self.rank > o.rank
    def __repr__(self):
        return str(self.rank)
    
class Player():
    def __init__(self, name):
        self.name = name
        self.stack = []
        self.score_pile = []

    def add_card(self, card):
        self.stack.append(card)
    
    def play_card(self):
        return self.stack.pop()
    
class Game():
    def __init__(self, players_names, num_cards):
        self.players = [Player(name) for name in players_names]
        self.deck = [Card(i) for i in range(1, num_cards+1)]
        self.score_board = {}
        random.shuffle(self.deck)
        
    
    def deal(self):
        player_to_deal = 0
        num_players = len(self.players)
        while self.deck:
            self.players[player_to_deal % num_players].add_card(self.deck.pop())
            player_to_deal += 1
    
    def start_game(self):
        # deal cards
        self.deal()

        # turn cards
        while True:
            winner = None
            max_card = Card(float('-inf'))
            for idx, player in enumerate(self.players):
                card = player.play_card()
                if card > max_card:
                    max_card = card
            
            print(cards)

card_game = Game(["a","b"], 52)
card_game.start_game()
