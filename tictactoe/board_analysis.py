
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

    # def test_function1(self):
        # print("test_function1")
        # self.humanplayer.webcam_setup()

