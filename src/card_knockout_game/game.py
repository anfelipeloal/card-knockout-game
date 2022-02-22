from src.card_knockout_game.deck import Deck
import time

class Game:
    deck = []
    deck_player_1 = []
    wins_player_1 = 0
    deck_player_2 = []
    wins_player_2 = 0
    draw = 0

    def __init__(self) -> None:
        self.deck = Deck()
        self.reset_data()
        self.run_game()
        self.get_game_results()

    def reset_data(self) -> None:
        self.wins_player_1 = 0
        self.wins_player_2 = 0
        self.draw = 0
        self.split_deck()

    def split_deck(self) -> None:
        full_deck = self.deck.getDeck()
        self.deck_player_1 = full_deck[:26]
        self.deck_player_2 = full_deck[26:]

    def run_game(self) -> None:
        self.print_decks()
        for i in range(len(self.deck_player_1)):
            self.print_turn(self.deck_player_1[i], self.deck_player_2[i])
            if self.deck_player_1[i] > self.deck_player_2[i]:
                self.wins_player_1 += 1
                print(f"Player 1 winner of the turn {i+1}")
            elif self.deck_player_2[i] > self.deck_player_1[i]:
                self.wins_player_2 += 1
                print(f"Player 2 winner of this turn {i+1}")
            else:
                self.draw += 1
                print("Draw!")

            print("-----------------------------------------------")
            time.sleep(1)


    def print_decks(self) -> None:
        print(">>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<")
        print("---------------------DECKS---------------------")
        print("-----------------------------------------------")
        print(f"Player 1 deck: {self.deck_player_1}")
        print("-----------------------------------------------")
        print(f"Player 2 deck: {self.deck_player_2}")
        print(">>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<")

    def print_turn(self, card_player_1, card_player_2) -> None:
        print(f"Player 1 card value: {card_player_1}")
        print(f"Player 2 card value: {card_player_2}")

    def get_game_results(self) -> None:
        print(">>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<")
        print("--------------------RESULTS--------------------")
        print(">>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<")
        print(f"Player 1 wins: {self.wins_player_1}")
        print(f"Player 2 wins: {self.wins_player_2}")
        print(f"Draws: {self.draw}")
        print("-----------------------------------------------")
        if self.wins_player_1 > self.wins_player_2:
            print("PLAYER 1 WINS!!")
        elif self.wins_player_2 > self.wins_player_1:
            print("PLAYER 2 WINS!!")
        else:
            print("DRAW!!")
        print("-----------------------------------------------")
