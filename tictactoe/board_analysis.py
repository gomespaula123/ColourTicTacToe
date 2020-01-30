

class BoardAnalysis:

    def __init__(self, game):
        self.game = game
        # self.boardvisual = boardvisual
        # self.humanplayer = humanplayer  # test
        # self.boardvisual = boardvisual

    def set_board(self, boardvisual):
        self.boardvisual = boardvisual

    # def get_positions(self):
    #     # self.boardvisual.positions_status[6] = 2
    #     print(*self.boardvisual.positions_status)
    #     # self.boardvisual.getcolour_images()

    def check_win_circle(self, game_being_analysed):
        win = False
        # check horizontal first
        if ((game_being_analysed[0] == 1 and game_being_analysed[1] == 1 and
             game_being_analysed[2] == 1)
            or (game_being_analysed[3] == 1 and game_being_analysed[4] == 1 and
                game_being_analysed[5] == 1)
            or (game_being_analysed[6] == 1 and game_being_analysed[7] == 1 and
                game_being_analysed[8] == 1)
            # check vertical
            or (game_being_analysed[0] == 1 and game_being_analysed[3] == 1 and
                game_being_analysed[6] == 1)
            or (game_being_analysed[1] == 1 and game_being_analysed[4] == 1 and
                game_being_analysed[7] == 1)
            or (game_being_analysed[2] == 1 and game_being_analysed[5] == 1 and
                game_being_analysed[8] == 1)
            # check diagonal
            or (game_being_analysed[0] == 1 and game_being_analysed[4] == 1 and
                game_being_analysed[8] == 1)
            or (game_being_analysed[6] == 1 and game_being_analysed[4] == 1 and
                game_being_analysed[2] == 1)):
            win = True
            # print(lose)
            # print("you lost")
            # self.quit_game()
        return win

    def check_win_square(self, game_being_analysed):
        win = False
        # check horizontal first
        if ((game_being_analysed[0] == 2 and game_being_analysed[1] == 2 and
             game_being_analysed[2] == 2)
            or (game_being_analysed[3] == 2 and game_being_analysed[4] == 2 and
                game_being_analysed[5] == 2)
            or (game_being_analysed[6] == 2 and game_being_analysed[7] == 2 and
                game_being_analysed[8] == 2)
            # check vertical
            or (game_being_analysed[0] == 2 and game_being_analysed[3] == 2 and
                game_being_analysed[6] == 2)
            or (game_being_analysed[1] == 2 and game_being_analysed[4] == 2 and
                game_being_analysed[7] == 2)
            or (game_being_analysed[2] == 2 and game_being_analysed[5] == 2 and
                game_being_analysed[8] == 2)
            # check diagonal
            or (game_being_analysed[0] == 2 and game_being_analysed[4] == 2 and
                game_being_analysed[8] == 2)
            or (game_being_analysed[6] == 2 and game_being_analysed[4] == 2 and
                game_being_analysed[2] == 2)):
            win = True
            # print(win)
            # print("you won")
        return win

    def check_full(self, game_being_analysed):
        full = False
        if 0 not in game_being_analysed:
            full = True
        return full

    def win_questionmark(self, mark, this_game_here):
        if mark == 1:
            return self.check_win_circle(this_game_here)
        elif mark == 2:
            return self.check_win_square(this_game_here)
