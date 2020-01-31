

class AIPlayer:

    def __init__(self, game, boardanalysis):
        # Inheritance of variables
        self.game = game
        self.boardanalysis = boardanalysis

        # Defining local variables
        self.next_board = None
        self.boardvisual = None
        self.memo = dict()

        # Defining local constants
        self.mark = 1
        self.maxdepth = 2

    # Inherent boardvisual as well
    def set_board(self, boardvisual):
        self.boardvisual = boardvisual

    # Returns the best possible move that the AI can think of according to a minimax algorithm with a limited \
    # depth heuristic that is defined by the maxdepth constant
    def do_move(self):
        self.boardvisual.positions_status[self.calculate_next_move(self.boardvisual.positions_status)] = self.mark

    def calculate_next_move(self, current_board):
        score_move_pairs = []
        for next_move in self.get_possible_moves(current_board):
            next_score = self.min_max(current_board, next_move, self.mark, 0)
            score_move_pairs.append((next_score, next_move))

            # If there is no score/move pair, return -1 (should give an error)
        if not score_move_pairs:
            return -1

        # Otherwise
        else:
            # Compute the max score/move
            highest_score, best_move = max(score_move_pairs)
            # Return the best move found
            return best_move

    def min_max(self, current_board, move, mark, depth):

        # The next board is a copy of the current board
        next_board = current_board.copy()

        # Place a move for the mark on the next board
        next_board[move] = mark

        # If this iteration is a win return 100
        if self.boardanalysis.win_questionmark(mark, next_board):
            return 100
        # If this iteration has a full board return 0
        if self.boardanalysis.check_full(next_board):
            return 0

        # Compute the minimum score of all possible moves
        score = []
        for possible_move in self.get_possible_moves(next_board):
            depth += 1
            if depth >= self.maxdepth:
                # As your opponent wants to minimize your score, add your scores to list based on heuristics
                score.append(self.get_heuristic_value(next_board, mark))
                return min(score)  # Picks the one where your score is lowest
            score_value = self.max_min(next_board, possible_move, self.other_mark(mark), depth)
            score.append(score_value)

        # return the minimum score
        if len(score) == 0:
            return 0
        return min(score)

    def max_min(self, current_board, move, mark, depth):
        # The next_board is copy of the current_board
        next_board = current_board.copy()

        # Place the move for the mark on the next board
        next_board[move] = mark

        # If this iteration is a win return 100
        if self.boardanalysis.win_questionmark(mark, next_board):
            return -100
        # If this iteration has a full board return 0
        if self.boardanalysis.check_full(next_board):
            return 0

        # Compute the maximum score of all possible moves
        score = []
        for possible_move in self.get_possible_moves(next_board):
            depth += 1
            if depth >= self.maxdepth:
                # Add the scores of the possible moves of your opponent
                score.append(-1 * (self.get_heuristic_value(next_board, mark)))
                return max(score)
            score_value = self.min_max(next_board, possible_move, self.other_mark(mark), depth)
            score.append(score_value)

        # Return the maximum score
        if len(score) == 0:
            return 0
        return max(score)

    # Shifts between marks
    def other_mark(self, mark):
        if mark == 2:
            return 1
        else:
            return 2

    # Compiles a list of all places that can have moves played at
    def get_possible_moves(self, current_board):
        possible_moves = []
        for i in range(0, 9):
            if current_board[i] == 0:
                possible_moves.append(i)
        return possible_moves

    def get_heuristic_value(self, current_board, mark):
        value_mark1 = 0
        value_mark2 = 0
        value_othermark1 = 0
        value_othermark2 = 0

        # START: MARK
        # adding horizontal value_mark2
        if (current_board[0] == mark and current_board[1] == 0 and current_board[2] == mark) \
                or (current_board[0] == 0 and current_board[1] == mark and current_board[2] == mark) \
                or (current_board[0] == mark and current_board[1] == mark and current_board[2] == 0):
            value_mark2 += 1
        if (current_board[3] == mark and current_board[4] == 0 and current_board[5] == mark) \
                or (current_board[3] == 0 and current_board[4] == mark and current_board[5] == mark) \
                or (current_board[3] == mark and current_board[4] == mark and current_board[5] == 0):
            value_mark2 += 1
        if (current_board[6] == mark and current_board[7] == 0 and current_board[8] == mark) \
                or (current_board[6] == 0 and current_board[7] == mark and current_board[8] == mark) \
                or (current_board[6] == mark and current_board[7] == mark and current_board[8] == 0):
            value_mark2 += 1

        # adding horizontal value_mark1
        if (current_board[0] == mark and current_board[1] == 0 and current_board[2] == 0) \
                or (current_board[0] == 0 and current_board[1] == mark and current_board[2] == 0) \
                or (current_board[0] == 0 and current_board[1] == 0 and current_board[2] == mark):
            value_mark1 += 1
        if (current_board[3] == mark and current_board[4] == 0 and current_board[5] == 0) \
                or (current_board[3] == 0 and current_board[4] == mark and current_board[5] == 0) \
                or (current_board[3] == 0 and current_board[4] == 0 and current_board[5] == mark):
            value_mark1 += 1
        if (current_board[6] == mark and current_board[7] == 0 and current_board[8] == 0) \
                or (current_board[6] == 0 and current_board[7] == mark and current_board[8] == 0) \
                or (current_board[6] == 0 and current_board[7] == 0 and current_board[8] == mark):
            value_mark1 += 1

        # adding vertical value_mark2
        if (current_board[0] == mark and current_board[3] == 0 and current_board[6] == mark) \
                or (current_board[0] == 0 and current_board[3] == mark and current_board[6] == mark) \
                or (current_board[0] == mark and current_board[3] == mark and current_board[6] == 0):
            value_mark2 += 1
        if (current_board[1] == mark and current_board[4] == 0 and current_board[7] == mark)\
                or (current_board[1] == 0 and current_board[4] == mark and current_board[7] == mark) \
                or (current_board[1] == mark and current_board[4] == mark and current_board[7] == 0):
            value_mark2 += 1
        if (current_board[2] == mark and current_board[5] == 0 and current_board[8] == mark)\
                or (current_board[2] == 0 and current_board[5] == mark and current_board[8] == mark) \
                or (current_board[2] == mark and current_board[5] == mark and current_board[8] == 0):
            value_mark2 += 1

        # adding vertical value_mark1
        if (current_board[0] == mark and current_board[3] == 0 and current_board[6] == 0) \
                or (current_board[0] == 0 and current_board[3] == mark and current_board[6] == 0) \
                or (current_board[0] == 0 and current_board[3] == 0 and current_board[6] == mark):
            value_mark1 += 1
        if (current_board[1] == mark and current_board[4] == 0 and current_board[7] == 0) \
                or (current_board[1] == 0 and current_board[4] == mark and current_board[7] == 0) \
                or (current_board[1] == 0 and current_board[4] == 0 and current_board[7] == mark):
            value_mark1 += 1
        if (current_board[2] == mark and current_board[5] == 0 and current_board[8] == 0) \
                or (current_board[2] == 0 and current_board[5] == mark and current_board[8] == 0)\
                or (current_board[2] == 0 and current_board[5] == 0 and current_board[8] == mark):
            value_mark1 += 1

        # adding diagonal value_mark2
        if (current_board[0] == mark and current_board[4] == 0 and current_board[8] == mark) \
                or (current_board[0] == 0 and current_board[4] == mark and current_board[8] == mark) \
                or (current_board[0] == mark and current_board[4] == mark and current_board[8] == 0):
            value_mark2 += 1
        if (current_board[6] == mark and current_board[4] == 0 and current_board[2] == mark) \
                or (current_board[6] == 0 and current_board[4] == mark and current_board[2] == mark) \
                or (current_board[6] == mark and current_board[4] == mark and current_board[2] == 0):
            value_mark2 += 1

        # adding diagonal value_mark1
        if (current_board[0] == mark and current_board[4] == 0 and current_board[8] == 0) \
                or (current_board[0] == 0 and current_board[4] == mark and current_board[8] == 0) \
                or (current_board[0] == 0 and current_board[4] == 0 and current_board[8] == mark):
            value_mark1 += 1
        if (current_board[6] == mark and current_board[4] == 0 and current_board[2] == 0)\
                or (current_board[6] == 0 and current_board[4] == mark and current_board[2] == 0) \
                or (current_board[6] == 0 and current_board[4] == 0 and current_board[2] == mark):
            value_mark1 += 1
        # END: MARK

        # START: OTHER MARK
        mark = self.other_mark(mark)
        # adding horizontal value_othermark2
        if (current_board[0] == mark and current_board[1] == 0 and current_board[2] == mark) \
                or (current_board[0] == 0 and current_board[1] == mark and current_board[2] == mark) \
                or (current_board[0] == mark and current_board[1] == mark and current_board[2] == 0):
            value_othermark2 += 1
        if (current_board[3] == mark and current_board[4] == 0 and current_board[5] == mark) \
                or (current_board[3] == 0 and current_board[4] == mark and current_board[5] == mark) \
                or (current_board[3] == mark and current_board[4] == mark and current_board[5] == 0):
            value_othermark2 += 1
        if (current_board[6] == mark and current_board[7] == 0 and current_board[8] == mark) \
                or (current_board[6] == 0 and current_board[7] == mark and current_board[8] == mark) \
                or (current_board[6] == mark and current_board[7] == mark and current_board[8] == 0):
            value_othermark2 += 1

        # adding horizontal value_othermark1
        if (current_board[0] == mark and current_board[1] == 0 and current_board[2] == 0) \
                or (current_board[0] == 0 and current_board[1] == mark and current_board[2] == 0) \
                or (current_board[0] == 0 and current_board[1] == 0 and current_board[2] == mark):
            value_othermark1 += 1
        if (current_board[3] == mark and current_board[4] == 0 and current_board[5] == 0) \
                or (current_board[3] == 0 and current_board[4] == mark and current_board[5] == 0) \
                or (current_board[3] == 0 and current_board[4] == 0 and current_board[5] == mark):
            value_othermark1 += 1
        if (current_board[6] == mark and current_board[7] == 0 and current_board[8] == 0) \
                or (current_board[6] == 0 and current_board[7] == mark and current_board[8] == 0) \
                or (current_board[6] == 0 and current_board[7] == 0 and current_board[8] == mark):
            value_othermark1 += 1

        # adding vertical value_othermark2
        if (current_board[0] == mark and current_board[3] == 0 and current_board[6] == mark) \
                or (current_board[0] == 0 and current_board[3] == mark and current_board[6] == mark) \
                or (current_board[0] == mark and current_board[3] == mark and current_board[6] == 0):
            value_othermark2 += 1
        if (current_board[1] == mark and current_board[4] == 0 and current_board[7] == mark) \
                or (current_board[1] == 0 and current_board[4] == mark and current_board[7] == mark) \
                or (current_board[1] == mark and current_board[4] == mark and current_board[7] == 0):
            value_othermark2 += 1
        if (current_board[2] == mark and current_board[5] == 0 and current_board[8] == mark) \
                or (current_board[2] == 0 and current_board[5] == mark and current_board[8] == mark) \
                or (current_board[2] == mark and current_board[5] == mark and current_board[8] == 0):
            value_othermark2 += 1

        # adding vertical value_othermark1
        if (current_board[0] == mark and current_board[3] == 0 and current_board[6] == 0) \
                or (current_board[0] == 0 and current_board[3] == mark and current_board[6] == 0) \
                or (current_board[0] == 0 and current_board[3] == 0 and current_board[6] == mark):
            value_othermark1 += 1
        if (current_board[1] == mark and current_board[4] == 0 and current_board[7] == 0) \
                or (current_board[1] == 0 and current_board[4] == mark and current_board[7] == 0) \
                or (current_board[1] == 0 and current_board[4] == 0 and current_board[7] == mark):
            value_othermark1 += 1
        if (current_board[2] == mark and current_board[5] == 0 and current_board[8] == 0) \
                or (current_board[2] == 0 and current_board[5] == mark and current_board[8] == 0) \
                or (current_board[2] == 0 and current_board[5] == 0 and current_board[8] == mark):
            value_othermark1 += 1

        # adding diagonal value_othermark2
        if (current_board[0] == mark and current_board[4] == 0 and current_board[8] == mark) \
                or (current_board[0] == 0 and current_board[4] == mark and current_board[8] == mark) \
                or (current_board[0] == mark and current_board[4] == mark and current_board[8] == 0):
            value_othermark2 += 1
        if (current_board[6] == mark and current_board[4] == 0 and current_board[2] == mark) \
                or (current_board[6] == 0 and current_board[4] == mark and current_board[2] == mark) \
                or (current_board[6] == mark and current_board[4] == mark and current_board[2] == 0):
            value_othermark2 += 1

        # adding diagonal value_othermark1
        if (current_board[0] == mark and current_board[4] == 0 and current_board[8] == 0) \
                or (current_board[0] == 0 and current_board[4] == mark and current_board[8] == 0) \
                or (current_board[0] == 0 and current_board[4] == 0 and current_board[8] == mark):
            value_othermark1 += 1
        if (current_board[6] == mark and current_board[4] == 0 and current_board[2] == 0) \
                or (current_board[6] == 0 and current_board[4] == mark and current_board[2] == 0) \
                or (current_board[6] == 0 and current_board[4] == 0 and current_board[2] == mark):
            value_othermark1 += 1
        # END: OTHERMARK

        # Heuristic formula: in favour of "mark"
        return (3 * value_mark2 + value_mark1) - (3 * value_othermark2 + value_othermark1)
