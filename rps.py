import os
import random


SYMBOLS = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",

    """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",

    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

MOVES = ["rock", "paper", "scissors"]


class Player:
    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(MOVES)


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Enter your move (rock/paper/scissors): ").lower()
            if choice in MOVES:
                return choice
            else:
                print("Invalid choice. Choose from rock, paper, "
                      "or scissors.")


def beats(one, two):
    return (
            (one == "rock" and two == "scissors")
            or (one == "scissors" and two == "paper")
            or (one == "paper" and two == "rock")
    )


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0

    def play_round(self):
        move1 = self.player1.move()
        move2 = self.player2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if move1 == move2:
            print("It's a tie!")
        elif beats(move1, move2):
            print("Player 1 wins!")
            self.player1_score += 1
        else:
            print("Player 2 wins!")
            self.player2_score += 1

        self.player1.learn(move1, move2)
        self.player2.learn(move2, move1)

        for symbol, move in zip(SYMBOLS, MOVES):
            if move1 == move:
                print("Player 1 played:")
                print(symbol)
            if move2 == move:
                print("Player 2 played:")
                print(symbol)

        print(f"Player 1 score: {self.player1_score}  "
              f"Player 2 score: {self.player2_score}")

    def display_final_score(self):
        print("\nFinal Score:")
        print(f"Player 1 score: {self.player1_score}  "
              f"Player 2 score: {self.player2_score}")


def play_game():
    os.system("clear")
    print("\t\t\t\t-------- 🔥Janken🔥 --------")
    print('Game of Rock Paper Scissors, also known '
          'as "Janken" in Japanese\n')

    human_player = HumanPlayer()
    computer_player = RandomPlayer()

    while True:
        game = Game(human_player, computer_player)

        for _ in range(3):  # Play 3 rounds
            game.play_round()

        game.display_final_score()  # Display final scores

        while True:
            game_checker = input("Type 'quit' to end the game "
                                 "or 'continue' to play again: ")
            if game_checker.strip().lower() == "quit":
                exit()
            elif game_checker.strip() == "continue":
                os.system("clear")
                print("\t\t\t\t-------- 🔥Janken🔥 --------")
                print('Game of Rock Paper Scissors, also known as '
                      '"Janken" in Japanese\n')
                break
            else:
                print("Invalid input. Please type 'quit' or 'continue.'")


if __name__ == "__main__":
    play_game()
