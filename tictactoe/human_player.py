import cv2
# from tictactoe.board_visual import BoardVisual
# from tictactoe.main import Game
# from tictactoe import main
import numpy as np
    
# reference the tutorial !!!!!!!!!!!!!!!!! https://towardsdatascience.com/https-medium-com-dilan-jay-face-detection-model-on-webcam-using-python-72b382699ee9

# make that once a colour is detected, the webcam shuts down and the board gets updated


class HumanPlayer:

    def __init__(self, game):
        # print("what do I put here")
        self.screen = None
        self.game = game
        # self.boaranalysis = boardanalysis # test
        # self.board_visual = BoardVisual(self.game)
        # self.main = Game()
        self.video_capture = cv2.VideoCapture(0)
        self.red_found = False

    def set_board(self, boardvisual):
        self.boardvisual = boardvisual


    def webcam_setup(self):
        while True:
            # Capture frame-by-frame
            ret, frame = self.video_capture.read()
            self.look_for_colours(frame)
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
                # this is a test :)

                # end of test
                self.boardvisual.getcolour_images()
                # self.boardvisual.create_window(self.screen)
                # self.main.get_webcaminput(self)

            # check input,
            elif k == ord('q'):  # position 0
                if self.boardvisual.positions_status[0] == 0:
                    self.boardvisual.positions_status[0] = 2
                    self.boardvisual.getcolour_images()
                else:
                    print("try another move")

            elif k == ord('w'):  # position 1
                if self.boardvisual.positions_status[1] == 0:
                    self.boardvisual.positions_status[1] = 2
                    self.boardvisual.getcolour_images()
                else:
                    print("try another move")

            elif k == ord('e'):  # position 2
                if self.boardvisual.positions_status[2] == 0:
                    self.boardvisual.positions_status[2] = 2
                    self.boardvisual.getcolour_images()
                else:
                    print("try another move")

            elif k == ord('a'):  # position 3
                if self.boardvisual.positions_status[3] == 0:
                    self.boardvisual.positions_status[3] = 2
                    self.boardvisual.getcolour_images()
                else:
                    print("try another move")

            elif k == ord('s'):  # position 4
                if self.boardvisual.positions_status[4] == 0:
                    self.boardvisual.positions_status[4] = 2
                    self.boardvisual.getcolour_images()
                else:
                    print("try another move")

            elif self.red_found:    # position 5
                print("RED!")
                if self.boardvisual.positions_status[5] == 0:
                    self.boardvisual.positions_status[5] = 2
                    self.boardvisual.getcolour_images()
                else:
                    print("try another move")
                self.red_found = False

            elif k == ord('z'):  # position 6
                if self.boardvisual.positions_status[6] == 0:
                    self.boardvisual.positions_status[6] = 2
                    self.boardvisual.getcolour_images()
                else:
                    print("try another move")

            elif k == ord('x'):  # position 7
                if self.boardvisual.positions_status[7] == 0:
                    self.boardvisual.positions_status[7] = 2
                    self.boardvisual.getcolour_images()
                else:
                    print("try another move")

            elif k == ord('c'):  # position 8
                if self.boardvisual.positions_status[8] == 0:
                    self.boardvisual.positions_status[8] = 2
                    self.boardvisual.getcolour_images()
                else:
                    print("try another move")

    # When everything is done, release the capture
        self.video_capture.release()
        cv2.destroyAllWindows()

    def look_for_colours(self, frame):
        # Determine the spotting range of RED
        lower_range = np.array([55, 70, 160])
        upper_range = np.array([70, 110, 205])

        # Filter out from the capture the RED object
        paperThing = cv2.inRange(frame, lower_range, upper_range)

        # Determine if there is indeed an object in the image
        hight = int(format(paperThing.shape[0]))
        width = int(format(paperThing.shape[1]))
        whiteness = 0
        for i in range(0, hight - 1, 4):
            for j in range(0, width - 1, 4):
                if paperThing[i, j] > 200:
                    whiteness = whiteness + 1
        if whiteness >= 2000:
            # Object confirmed
            self.red_found = True