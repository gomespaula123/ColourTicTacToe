

class AIPlayer:

    def __init__(self, game):
        # print("what do I put here")
        self.game = game

    def set_board(self, boardvisual):
        self.boardvisual = boardvisual

    def testai_playerfunction(self):
        print("test AI called function")

    '''# from tutorial assignment
    def calculate_next_move(self, current_board):
        print("calculate_next_move")
        # for every possible move, add a pair of a min_max score and the move to a list scores.
        score_move_pairs = []
        for next_move in current_board.get_possible_moves():
            next_score = self.min_max(current_board, next_move, self.mark)
            score_move_pairs.append((next_score, next_move))

            # if there is no score/move pair, return 0
            if not score_move_pairs:
                return 0

            # otherwise
            else:
                # compute the max score/move
                highest_score, best_move = max(score_move_pairs)
                # return the move
                return best_move'''