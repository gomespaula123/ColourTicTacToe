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

        # Initialize the variables used for the human interaction
        self.black_found = False
        self.blue_found = False
        self.cyan_found = False
        self.green_found = False
        self.magenta_found = False
        self.red_found = False
        self.yellow_found = False
        self.white_found = False

        # For redundancy testing
        self.intensity = 4  # Increases the amount of times that the test is ran
        self.none_found = True
        self.spot_counter = 0

    def set_board(self, boardvisual):
        self.boardvisual = boardvisual


    def webcam_setup(self):
        while True:
            # Capture frame-by-frame
            ret, frame = self.video_capture.read()
            self.look_for_colours(frame)

            k = cv2.waitKey(1)

            # Redundancy testing
            if not self.red_found and not self.green_found and not self.blue_found:
                print('no red green nor blue')
                if not self.cyan_found and not self.yellow_found and not self.magenta_found:
                    if not self.black_found and not self.white_found:
                        self.none_found = True
                        self.spot_counter = 0

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
                print(self.spot_counter)
                # self.boardvisual.create_window(self.screen)
                # self.main.get_webcaminput(self)

            # check input,
            elif self.yellow_found or k == ord('q'):  # position 0
                if self.spot_counter > self.intensity:
                    print("YELLOW!")
                    if self.boardvisual.positions_status[0] == 0:
                        self.boardvisual.positions_status[0] = 2
                        self.boardvisual.getcolour_images()
                    else:
                        print("try another move")
                elif not self.none_found:
                    self.spot_counter = self.spot_counter + 1
                self.yellow_found = False

            elif k == ord('w'):  # position 1
                if self.boardvisual.positions_status[1] == 0:
                    self.boardvisual.positions_status[1] = 2
                    self.boardvisual.getcolour_images()
                else:
                    print("try another move")

            elif self.green_found or k == ord('e'):  # position 2
                if self.spot_counter > self.intensity:
                    print("GREEN!")
                    if self.boardvisual.positions_status[2] == 0:
                        self.boardvisual.positions_status[2] = 2
                        self.boardvisual.getcolour_images()
                    else:
                        print("try another move")
                elif not self.none_found:
                    self.spot_counter = self.spot_counter + 1
                self.green_found = False

            elif self.cyan_found or k == ord('a'):  # position 3
                if self.spot_counter > self.intensity:
                    print("CYAN!")
                    if self.boardvisual.positions_status[3] == 0:
                        self.boardvisual.positions_status[3] = 2
                        self.boardvisual.getcolour_images()
                    else:
                        print("try another move")
                elif not self.none_found:
                    self.spot_counter = self.spot_counter + 1
                self.cyan_found = False

            elif self.blue_found or k == ord('s'):  # position 4
                if self.spot_counter > self.intensity:
                    print("BLUE!")
                    if self.boardvisual.positions_status[4] == 0:
                        self.boardvisual.positions_status[4] = 2
                        self.boardvisual.getcolour_images()
                    else:
                        print("try another move")
                elif not self.none_found:
                    self.spot_counter = self.spot_counter + 1
                self.blue_found = False

            elif self.red_found or k == ord('d'):    # position 5
                if self.spot_counter > self.intensity:
                    print("RED!")
                    if self.boardvisual.positions_status[5] == 0:
                        self.boardvisual.positions_status[5] = 2
                        self.boardvisual.getcolour_images()
                    else:
                        print("try another move")
                elif not self.none_found:
                    self.spot_counter = self.spot_counter + 1
                self.red_found = False

            elif self.magenta_found or k == ord('z'):  # position 6
                if self.spot_counter > self.intensity:
                    print("MAGENTA!")
                    if self.boardvisual.positions_status[6] == 0:
                        self.boardvisual.positions_status[6] = 2
                        self.boardvisual.getcolour_images()
                    else:
                        print("try another move")
                elif not self.none_found:
                    self.spot_counter = self.spot_counter + 1
                self.magenta_found = False

            elif self.black_found or k == ord('x'):  # position 7
                if self.spot_counter > self.intensity:
                    print("BLACK!")
                    if self.boardvisual.positions_status[7] == 0:
                        self.boardvisual.positions_status[7] = 2
                        self.boardvisual.getcolour_images()
                    else:
                        print("try another move")
                elif not self.none_found:
                    self.spot_counter = self.spot_counter + 1
                self.black_found = False

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
        self.black_questionmark(frame)
        self.blue_questionmark(frame)
        self.cyan_questionmark(frame)
        self.green_questionmark(frame)
        self.magenta_questionmark(frame)
        self.red_questionmark(frame)
        self.yellow_questionmark(frame)
        self.white_questionmark(frame)



    def black_questionmark(self, frame):
        # Determine the spotting range of BLACK
        lower_range = np.array([35, 35, 40])
        upper_range = np.array([80, 65, 80])

        # Filter out from the capture the RED object
        paper_colour_tag = cv2.inRange(frame, lower_range, upper_range)

        # Determine if there is indeed an object in the image
        height = int(format(paper_colour_tag.shape[0]))
        width = int(format(paper_colour_tag.shape[1]))
        whiteness = 0
        for i in range(0, height - 1, 4):
            for j in range(0, width - 1, 4):
                if paper_colour_tag[i, j] > 200:
                    whiteness = whiteness + 1
        if whiteness >= 2000:
            # Object confirmed
            self.black_found = True
            self.none_found = False

    def blue_questionmark(self, frame):
        # Determine the spotting range of BLUE
        lower_range = np.array([140, 80, 40])
        upper_range = np.array([170, 110, 80])

        # Filter out from the capture the RED object
        paper_colour_tag = cv2.inRange(frame, lower_range, upper_range)

        # Determine if there is indeed an object in the image
        height = int(format(paper_colour_tag.shape[0]))
        width = int(format(paper_colour_tag.shape[1]))
        whiteness = 0
        for i in range(0, height - 1, 4):
            for j in range(0, width - 1, 4):
                if paper_colour_tag[i, j] > 200:
                    whiteness = whiteness + 1
        if whiteness >= 2000:
            # Object confirmed
            self.blue_found = True
            self.none_found = False

    def cyan_questionmark(self, frame):
        # Determine the spotting range of CYAN
        lower_range = np.array([140, 80, 40])
        upper_range = np.array([170, 110, 80])

        # Filter out from the capture the RED object
        paper_colour_tag = cv2.inRange(frame, lower_range, upper_range)

        # Determine if there is indeed an object in the image
        height = int(format(paper_colour_tag.shape[0]))
        width = int(format(paper_colour_tag.shape[1]))
        whiteness = 0
        for i in range(0, height - 1, 4):
            for j in range(0, width - 1, 4):
                if paper_colour_tag[i, j] > 200:
                    whiteness = whiteness + 1
        if whiteness >= 2000:
            # Object confirmed
            self.cyan_found = True
            self.none_found = False

    def green_questionmark(self, frame):
        # Determine the spotting range of GREEN
        lower_range = np.array([70, 80, 40])
        upper_range = np.array([115, 110, 80])

        # Filter out from the capture the RED object
        paper_colour_tag = cv2.inRange(frame, lower_range, upper_range)

        # Determine if there is indeed an object in the image
        height = int(format(paper_colour_tag.shape[0]))
        width = int(format(paper_colour_tag.shape[1]))
        whiteness = 0
        for i in range(0, height - 1, 4):
            for j in range(0, width - 1, 4):
                if paper_colour_tag[i, j] > 200:
                    whiteness = whiteness + 1
        if whiteness >= 2000:
            # Object confirmed
            self.green_found = True
            self.none_found = False

    def magenta_questionmark(self, frame):
        # Determine the spotting range of MAGENTA
        lower_range = np.array([90, 65, 140])
        upper_range = np.array([130, 95, 175])

        # Filter out from the capture the RED object
        paper_colour_tag = cv2.inRange(frame, lower_range, upper_range)

        # Determine if there is indeed an object in the image
        height = int(format(paper_colour_tag.shape[0]))
        width = int(format(paper_colour_tag.shape[1]))
        whiteness = 0
        for i in range(0, height - 1, 4):
            for j in range(0, width - 1, 4):
                if paper_colour_tag[i, j] > 200:
                    whiteness = whiteness + 1
        if whiteness >= 2000:
            # Object confirmed
            self.magenta_found = True
            self.none_found = False

    def red_questionmark(self, frame):
        # Determine the spotting range of RED
        lower_range = np.array([65, 60, 150])
        upper_range = np.array([95, 90, 170])

        # Filter out from the capture the RED object
        paper_colour_tag = cv2.inRange(frame, lower_range, upper_range)

        # Determine if there is indeed an object in the image
        height = int(format(paper_colour_tag.shape[0]))
        width = int(format(paper_colour_tag.shape[1]))
        whiteness = 0
        for i in range(0, height - 1, 4):
            for j in range(0, width - 1, 4):
                if paper_colour_tag[i, j] > 200:
                    whiteness = whiteness + 1
        if whiteness >= 2000:
            # Object confirmed
            self.red_found = True
            self.none_found = False

    def yellow_questionmark(self, frame):
        # Determine the spotting range of YELLOW
        lower_range = np.array([85, 120, 125])
        upper_range = np.array([120, 140, 150])

        # Filter out from the capture the RED object
        paper_colour_tag = cv2.inRange(frame, lower_range, upper_range)

        # Determine if there is indeed an object in the image
        height = int(format(paper_colour_tag.shape[0]))
        width = int(format(paper_colour_tag.shape[1]))
        whiteness = 0
        for i in range(0, height - 1, 4):
            for j in range(0, width - 1, 4):
                if paper_colour_tag[i, j] > 200:
                    whiteness = whiteness + 1
        if whiteness >= 2000:
            # Object confirmed
            self.yellow_found = True
            self.none_found = False

    def white_questionmark(self, frame):
        print("?")