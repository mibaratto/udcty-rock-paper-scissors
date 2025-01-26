
import random
import time

moves = ['rock', 'paper', 'scissors']


def beats(move1, move2):
    return ((move1 == 'rock' and move2 == 'scissors')
            or (move1 == 'scissors' and move2 == 'paper')
            or (move1 == 'paper' and move2 == 'rock'))


class Player:
    def __init__(self):
        self.listOpponentMoves = []
        self.listMymoves = []

    def move(self):
        return 'rock'

    def learn(self, my_move, opponent_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            self.humanmove = input(
                "Rock, paper or scissors?\nWhat would you like to play?\n"
                ).lower()
            if self.humanmove in moves:
                return self.humanmove
            else:
                print("\nPlease, enter a valid answer.\n")


class ReflectPlayer(Player):
    def move(self):
        if len(self.listOpponentMoves) == 0:
            return "paper"
        else:
            return self.listOpponentMoves.pop()

    def learn(self, my_move, opponent_move):
        self.listOpponentMoves.append(opponent_move)


class CyclePlayer(Player):
    def move(self):
        if len(self.listMymoves) == 0:
            return "paper"
        else:
            lastmove = self.listMymoves.pop()
            if lastmove == "paper":
                return "rock"
            elif lastmove == "rock":
                return "scissors"
            else:
                return "paper"

    def learn(self, my_move, opponent_move):
        self.listMymoves.append(my_move)


class Game:
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        time.sleep(1)
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nYou played: {move1.upper()} | "
              f"Opponent played: {move2.upper()}\n")
        time.sleep(1)
        if move1 == move2:
            print("** YOU TIE THIS ROUND! **\n")
        else:
            self.vencedor = beats(move1, move2)
            if self.vencedor is True:
                print("** YOU WIN THIS ROUND! **\n")
                self.score1 = self.score1 + 1
            else:
                print("** YOU LOSE THIS ROUND! **\n")
                self.score2 = self.score2 + 1
        time.sleep(1)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!\nLET'S GO!\n")
        time.sleep(1)
        for round in range(3):
            print(f"---ROUND {round + 1}:")
            self.play_round()
            print(f"Your points: {self.score1} | "
                  f"Opponent points: {self.score2}\n")
        print("------GAME OVER------\n")
        if self.score1 > self.score2:
            print("** YOU WIN THE GAME **")
        elif self.score1 == self.score2:
            print("** YOU TIE THE GAME **")
        else:
            print("** YOU LOSE THE GAME **")
        print(f"\nYour total points: {self.score1} | "
              f" Opponent total points: {self.score2}")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
