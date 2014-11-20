__author__ = 'g_ric_000'


class RPSGame(Game):
    ## this class simulates two players playing rock, paper, scissors
    def __init__(self):


        def play_game(self, player1, player2):
            result = ""
            move1 = player1.get_move()
            move2 = player2.get_move()
            if self.is_valid_move(move1) and self.is_valid_move(move2):
                if move1 == move2:
                    result = "The match has ended in a tie!"
                elif (move1 == "rock" and move2 == "scissors") or (move1 == "paper" and move2 == "rock") or (move1 == "scissors" and move2 == "paper"):
                        result = "Player1 is the winner!"
                else:
                    result = "Player2 is the winner!"
            else:
                result = "Valid moves were not made by both teams."
            return result

        def is_valid_move(self, move):
            return move in ('rock', 'paper', 'scissors')
