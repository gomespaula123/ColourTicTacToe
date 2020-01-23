# from tictactoe import board_analysis

class AIPlayer:

    def __init__(self, game, boardanalysis):
        # print("what do I put here")
        self.next_board = None
        self.mark = 2
        self.game = game
        self.memo = dict()
        self.counter = 0
        self.boardanalysis = boardanalysis

    def set_board(self, boardvisual):
        self.boardvisual = boardvisual

    def testai_playerfunction(self):
        print("test AI called function")

    def calculate_next_move1(self, current_board):
        # current_board = self.boardvisual.positions_status
        score_move_pairs = []
        print("got till line 21")
        for next_move in self.get_possible_moves(current_board):
            print("got till line 23")
            next_score = self.min_max(current_board, next_move, self.mark)
            print("it did do line 25")
            score_move_pairs.append((next_score, next_move))

            # if there is no score/move pair, return 0
            if not score_move_pairs:
                return 0

            # otherwise
            else:
                # compute the max score/move
                highest_score, best_move = max(score_move_pairs)
                # return the move
                print("best move", best_move)
                return best_move

    '''def calculate_next_move(self, current_board):
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

    def min_max(self, current_board, move, mark):
        # depth = 8

        # the  next  board  is a (deep) copy of the  current  board
        next_board = current_board.copy()
        print("it copied the board, 67")

        # place  the  move  for  the  mark on the  next  board --> put best move there
        # original here: next_board.place_move(move, mark)
        self.place_move(next_board, move, mark)
        # next_board.place_move(move, mark)

        # check if the next board (next_board.board) is in the dictionary, if it is, use that value
        if tuple(next_board) in self.memo:
            return self.memo[(tuple(next_board))]

        # if it is a win  return  10 --> 100
        if self.boardanalysis.check_win():
            return 100
        # if the  board  is full  return 0
        if self.boardanalysis.check_full():
            return 0

        # compute  the  minimum  score  of all  possible  moves
        score = []
        for possible_move in self.get_possible_moves(next_board):
            '''depth -= 1
            if depth <= -1:
                score.append(self.get_heuristic_value(next_board, mark))  # as your opponent wants to minimize your score, add your scores to list based on heuristics
                self.counter += 1
                return min(score)  # picks the one where your score is lowest'''
            score_value = self.max_min(next_board, possible_move, self.other_mark(mark))
            print("94 does this happen")
            score.append(score_value)

        # self.memo[(tuple(next_board))] = min(score)
        self.counter += 1
        # print("minmax counter", self.get_counter())
        # print("depth minmax", depth)

        # return the minimum score
        return min(score)

    def max_min(self, current_board, move, mark):
        # depth = 8
        # the next_board is a(deep) copy of the current_board
        next_board = current_board.copy()

        # place  the  move  for  the  mark on the  next  board
        self.place_move(next_board, move, mark)
        # next_board.place_move(move, mark)

        # check if the next board (next_board.board) is in the dictionary, if it is, use that value
        if tuple(next_board) in self.memo:
            return self.memo[(tuple(next_board))]

        # if it is a win  return  -10 --> -100
        if self.boardanalysis.check_lose():
            return -100
        # if the  board  is full  return 0
        if self.boardanalysis.check_full():
            return 0

        # compute  the  maximum  score  of all  possible  moves
        score = []
        for possible_move in self.get_possible_moves(next_board):
            '''depth -= 1
            if depth <= -1:
                score.append(-1 * (self.get_heuristic_value(next_board, mark)))  # add the scores of the possible moves of your opponent
                self.counter += 1
                return max(score)'''
            score_value = self.min_max(next_board, possible_move, self.other_mark(mark))
            score.append(score_value)

        # self.memo[(tuple(next_board))] = max(score)
        self.counter += 1
        # print("maxmin counter", self.get_counter())
        # print("depth maxmin", depth)

        # return the maximum score
        return max(score)

    '''def other_mark(self, mark):
        if mark == "X":
            return "O"
        else:
            return "X"'''
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
                # print("it got added")
                # print(i)
        # for self.boardvisual.positions_status in possible_moves:
                # print i
        print(possible_moves)
        return possible_moves

    def place_move(self, next_board, move, mark):
        print("called place move")
        # self.possible_moves[next_move] = 2
        # self.next_board[move] = 2
        # mark = 2
        next_board[move] = mark
        print(next_board[move])
        # original here: self.board[move] = mark
