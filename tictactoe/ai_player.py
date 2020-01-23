

class AIPlayer:

    def __init__(self, game):
        # print("what do I put here")
        self.game = game

    def set_board(self, boardvisual):
        self.boardvisual = boardvisual

    def testai_playerfunction(self):
        print("test AI called function")

    def calculate_next_move1(self):
        print("next move 1")
        # print(current_board)
        # for next_move in current_board.get_possible_moves():
            # next_score =
        score_move_pairs = []

        for next_move in self.get_possible_moves.possible_moves:
            next_score = self.min_max(self.boardvisual.positions_status, next_move, self.mark)
            score_move_pairs.append((next_score, next_move))

            # if there is no score/move pair, return 0
            if not score_move_pairs:
                return 0

            # otherwise
            else:
                # compute the max score/move
                highest_score, best_move = max(score_move_pairs)
                # return the move
                return best_move


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
                return best_move

    def min_max(self, current_board, move, mark):
        # depth = 8
        # the  next  board  is a (deep) copy of the  current  board
        next_board = current_board.deep_copy()

        # place  the  move  for  the  mark on the  next  board --> put best move there
        next_board.place_move(move, mark)

        # check if the next board (next_board.board) is in the dictionary, if it is, use that value
        if tuple(next_board.board) in self.memo:
            return self.memo[(tuple(next_board.board))]

        # if it is a win  return  10 --> 100
        if next_board.check_win(mark):
            return 100
        # if the  board  is full  return 0
        if next_board.board_full():
            return 0

        # compute  the  minimum  score  of all  possible  moves
        score = []
        for possible_move in next_board.get_possible_moves():
            '''depth -= 1
            if depth <= -1:
                score.append(self.get_heuristic_value(next_board, mark))  # as your opponent wants to minimize your score, add your scores to list based on heuristics
                self.counter += 1
                return min(score)  # picks the one where your score is lowest'''
            score_value = self.max_min(next_board, possible_move, self.other_mark(mark))
            score.append(score_value)

        self.memo[(tuple(next_board.board))] = min(score)
        self.counter += 1
        # print("minmax counter", self.get_counter())
        # print("depth minmax", depth)

        # return the minimum score
        return min(score)

    def max_min(self, current_board, move, mark):
        # depth = 8
        # the next_board is a(deep) copy of the current_board
        next_board = current_board.deep_copy()

        # place  the  move  for  the  mark on the  next  board
        next_board.place_move(move, mark)

        # check if the next board (next_board.board) is in the dictionary, if it is, use that value
        if tuple(next_board.board) in self.memo:
            return self.memo[(tuple(next_board.board))]

        # if it is a win  return  -10 --> -100
        if next_board.check_win(mark):
            return -100
        # if the  board  is full  return 0
        if next_board.board_full():
            return 0

        # compute  the  maximum  score  of all  possible  moves
        score = []
        for possible_move in next_board.get_possible_moves():
            depth -= 1
            if depth <= -1:
                score.append(-1 * (self.get_heuristic_value(next_board, mark)))  # add the scores of the possible moves of your opponent
                self.counter += 1
                return max(score)
            score_value = self.min_max(next_board, possible_move, self.other_mark(mark))
            score.append(score_value)

        self.memo[(tuple(next_board.board))] = max(score)
        self.counter += 1
        print("maxmin counter", self.get_counter())
        # print("depth maxmin", depth)

        # return the maximum score
        return max(score)

    def other_mark(self, mark):
        if mark == "X":
            return "O"
        else:
            return "X"

    def get_possible_moves(self):
        possible_moves = []
        for i in range(0, 9):
            if self.boardvisual.positions_status[i] == 0:
                possible_moves.append(self.boardvisual.positions_status[i])
                print("it got added")
                print(i)
        # for self.boardvisual.positions_status in possible_moves:
             #print i

        #print(possible_moves)