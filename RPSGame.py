__author__ = 'Greg Richards'

import Game


class RPSGame(Game.Game):
    # # this class simulates two players playing a game of rock, paper, scissors
    def __init__(self):
        super(RPSGame, self).__init__()

    def get_result(self, moves):
        # unpack the tuple that was passed as a parameter
        move1, move2 = moves
        x = self.is_legal(move1)
        y = self.is_legal(move2)

        if x and y:
            if move1 == move2:
                result = (0, 0)
            elif (move1 == 0 and move2 != 1) \
                    or (move1 == 1 and move2 != 2) \
                    or (move1 == 2 and move2 != 0):
                # result is tuple with points each player has earned respectively
                result = (1, 0)
            else:
                result = (0, 1)
        elif x and not y:
            result = (1, 0)
        elif not x and y:
            result = (0, 1)
        else:
            result = (0, 0)
        return result

    def is_legal(self, move):
        return isinstance(move,int) and (move in (0, 1, 2))
