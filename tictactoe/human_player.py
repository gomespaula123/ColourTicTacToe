import cv2
# from tictactoe.board_visual import BoardVisual
# from tictactoe.main import Game
# from tictactoe import main
    
# reference the tutorial !!!!!!!!!!!!!!!!! https://towardsdatascience.com/https-medium-com-dilan-jay-face-detection-model-on-webcam-using-python-72b382699ee9

# make that once a colour is detected, the webcam shuts down and the board gets updated


class HumanPlayer:

    def __init__(self, game):
        # print("what do I put here")
        self.screen = None
        self.game = game
        # self.boardvisual = boardvisual # test
        # self.board_visual = BoardVisual(self.game)
        # self.main = Game()
        self.video_capture = cv2.VideoCapture(0)

    def set_board(self, boardvisual):
        self.boardvisual = boardvisual

    def webcam_setup(self):
        while True:
            # Capture frame-by-frame
            ret, frame = self.video_capture.read()
            k = cv2.waitKey(1)

    # Display the resulting frame
    # cv2.imshow(window_name, image)
            cv2.imshow('Windowname', frame)
            # print("does this happen??????????????????????????????")

            if k % 256 == 27:  # ESC Pressed
                break
            elif k % 256 == 32:  # SPACE pressed
                print("something")
                # self.board_visual.create_window(self.screen)
                # self.video_capture.release()
                # cv2.destroyAllWindows()
                #  self.game.draw_board()
                # self.main.draw_board
                self.boardvisual.getcolour_images(self.screen)
                # self.main.get_webcaminput(self)

    # When everything is done, release the capture
        self.video_capture.release()
        cv2.destroyAllWindows()