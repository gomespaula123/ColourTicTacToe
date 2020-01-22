
class BoardAnalysis:

    def __init__(self, game):
        # self.boardvisual = boardvisual
        self.game = game
        # self.humanplayer = humanplayer  # test
        # self.boardvisual = boardvisual

    def set_board(self, boardvisual):
        self.boardvisual = boardvisual

    def get_positions(self):
        # self.boardvisual.positions_status[6] = 2
        print(*self.boardvisual.positions_status)
        # self.boardvisual.getcolour_images()

    def check_lose(self):
        lose = False
        # check horizontal first
        if ((self.boardvisual.positions_status[0] == 1 and self.boardvisual.positions_status[1] == 1 and
             self.boardvisual.positions_status[2] == 1)
            or (self.boardvisual.positions_status[3] == 1 and self.boardvisual.positions_status[4] == 1 and
                self.boardvisual.positions_status[5] == 1)
            or (self.boardvisual.positions_status[6] == 1 and self.boardvisual.positions_status[7] == 1 and
                self.boardvisual.positions_status[8] == 1)
            # check vertical
            or (self.boardvisual.positions_status[0] == 1 and self.boardvisual.positions_status[3] == 1 and
                self.boardvisual.positions_status[6] == 1)
            or (self.boardvisual.positions_status[1] == 1 and self.boardvisual.positions_status[4] == 1 and
                self.boardvisual.positions_status[7] == 1)
            or (self.boardvisual.positions_status[2] == 1 and self.boardvisual.positions_status[5] == 1 and
                self.boardvisual.positions_status[8] == 1)
            # check diagonal
            or (self.boardvisual.positions_status[0] == 1 and self.boardvisual.positions_status[4] == 1 and
                self.boardvisual.positions_status[8] == 1)
            or (self.boardvisual.positions_status[6] == 1 and self.boardvisual.positions_status[4] == 1 and
                self.boardvisual.positions_status[2] == 1)):
            lose = True
            print(lose)
            print("you lost")

    def check_win(self):
        win = False
        # check horizontal first
        if ((self.boardvisual.positions_status[0] == 2 and self.boardvisual.positions_status[1] == 2 and
             self.boardvisual.positions_status[2] == 2)
            or (self.boardvisual.positions_status[3] == 2 and self.boardvisual.positions_status[4] == 2 and
                self.boardvisual.positions_status[5] == 2)
            or (self.boardvisual.positions_status[6] == 2 and self.boardvisual.positions_status[7] == 2 and
                self.boardvisual.positions_status[8] == 2)
            # check vertical
            or (self.boardvisual.positions_status[0] == 2 and self.boardvisual.positions_status[3] == 2 and
                self.boardvisual.positions_status[6] == 2)
            or (self.boardvisual.positions_status[1] == 2 and self.boardvisual.positions_status[4] == 2 and
                self.boardvisual.positions_status[7] == 2)
            or (self.boardvisual.positions_status[2] == 2 and self.boardvisual.positions_status[5] == 2 and
                self.boardvisual.positions_status[8] == 2)
            # check diagonal
            or (self.boardvisual.positions_status[0] == 2 and self.boardvisual.positions_status[4] == 2 and
                self.boardvisual.positions_status[8] == 2)
            or (self.boardvisual.positions_status[6] == 2 and self.boardvisual.positions_status[4] == 2 and
                self.boardvisual.positions_status[2] == 2)):
            win = True
            print(win)
            print("you won")




    # def test_function1(self):
        # print("test_function1")
        # self.humanplayer.webcam_setup()

