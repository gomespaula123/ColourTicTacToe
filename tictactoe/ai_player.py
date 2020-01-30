# from tictactoe import board_analysis

class AIPlayer:

    def __init__(self, game, boardanalysis):
        # print("what do I put here")
        self.next_board = None
        self.mark = 1
        self.game = game
        self.memo = dict()
        self.counter = 0
        self.boardanalysis = boardanalysis
        self.maxdepth = 3

    def set_board(self, boardvisual):
        self.boardvisual = boardvisual

    def do_move(self):
        print(self.boardvisual.positions_status)
        self.boardvisual.positions_status[self.calculate_next_move(self.boardvisual.positions_status)] = self.mark
        print(self.boardvisual.positions_status)

    def calculate_next_move(self, current_board):
        # current_board = self.boardvisual.positions_status
        score_move_pairs = []
        for next_move in self.get_possible_moves(current_board):
            next_score = self.min_max(current_board, next_move, self.mark, 0)
            score_move_pairs.append((next_score, next_move))

            # if there is no score/move pair, return -1 (should give an error)
        if not score_move_pairs:
            return -1

        # otherwise
        else:
            # compute the max score/move
            highest_score, best_move = max(score_move_pairs)
            # return the move
            print("best move:", best_move)
            return best_move

    #
    # '''def calculate_next_move(self, current_board):
    #     print("calculate_next_move")
    #     # for every possible move, add a pair of a min_max score and the move to a list scores.
    #     score_move_pairs = []
    #
    #     for next_move in current_board.get_possible_moves():
    #         next_score = self.min_max(current_board, next_move, self.mark)
    #         score_move_pairs.append((next_score, next_move))
    #
    #         # if there is no score/move pair, return 0
    #         if not score_move_pairs:
    #             return 0
    #
    #         # otherwise
    #         else:
    #             # compute the max score/move
    #             highest_score, best_move = max(score_move_pairs)
    #             # return the move
    #             return best_move'''

    def min_max(self, current_board, move, mark, depth):
        # depth = 8

        # the  next  board  is a (deep) copy of the  current  board
        next_board = current_board.copy()

        # place  the  move  for  the  mark on the  next  board --> put best move there
        # original here: next_board.place_move(move, mark)
        next_board[move] = mark
        # next_board.place_move(move, mark)

        # # check if the next board (next_board.board) is in the dictionary, if it is, use that value
        # if tuple(next_board) in self.memo:
        #     return self.memo[(tuple(next_board))]

        # if it is a win  return  10 --> 100
        if self.boardanalysis.win_questionmark(mark, next_board):
            print("some good")
            return 100
        # if the  board  is full  return 0
        if self.boardanalysis.check_full(next_board):
            print("some meh")
            return 0

        # compute  the  minimum  score  of all  possible  moves
        score = []
        for possible_move in self.get_possible_moves(next_board):
            depth += 1
            if depth >= self.maxdepth:
                score.append(self.get_heuristic_value(next_board,
                                                      mark))  # as your opponent wants to minimize your score, add your scores to list based on heuristics
                self.counter += 1
                return min(score)  # picks the one where your score is lowest
            score_value = self.max_min(next_board, possible_move, self.other_mark(mark), depth)
            score.append(score_value)

        # self.memo[(tuple(next_board))] = min(score)
        self.counter += 1
        # print("minmax counter", self.get_counter())
        # print("depth minmax", depth)

        # return the minimum score
        if len(score) == 0:
            return 0
        return min(score)

    def max_min(self, current_board, move, mark, depth):
        # depth = 8
        # the next_board is a(deep) copy of the current_board
        next_board = current_board.copy()

        # place  the  move  for  the  mark on the  next  board
        next_board[move] = mark
        # next_board.place_move(move, mark)

        # check if the next board (next_board.board) is in the dictionary, if it is, use that value
        if tuple(next_board) in self.memo:
            return self.memo[(tuple(next_board))]

        # if it is a win  return  -10 --> -100
        if self.boardanalysis.win_questionmark(mark, next_board):
            print("some bad")
            return -100
        # if the  board  is full  return 0
        if self.boardanalysis.check_full(next_board):
            print("some meh")
            return 0

        # compute  the  maximum  score  of all  possible  moves
        score = []
        for possible_move in self.get_possible_moves(next_board):
            depth += 1
            if self.maxdepth >= -1:
                score.append(-1 * (self.get_heuristic_value(next_board,
                                                            mark)))  # add the scores of the possible moves of your opponent
                self.counter += 1
                return max(score)
            score_value = self.min_max(next_board, possible_move, self.other_mark(mark), depth)
            score.append(score_value)

        # self.memo[(tuple(next_board))] = max(score)
        self.counter += 1
        # print("maxmin counter", self.get_counter())
        # print("depth maxmin", depth)

        # return the maximum score
        if len(score) == 0:
            return 0
        return max(score)

    def other_mark(self, mark):
        if mark == 2:
            return 1
        else:
            return 2

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

        # heuristic formula: in favour of "mark"
        return (3 * value_mark2 + value_mark1) - (3 * value_othermark2 + value_othermark1)
