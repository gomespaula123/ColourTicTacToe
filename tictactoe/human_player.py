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
        self.intensity = 2  # Increases the amount of times that the test is ran
        self.none_found = True
        self.spot_counter = 0

        # Time for the player to present the color that they want to play
        self.timer_counter_magigy = 10  # No clue about the ratio of ticks per second doe...
        self.timer_counter = self.timer_counter_magigy

    def set_board(self, boardvisual):
        self.boardvisual = boardvisual

    def human_move(self):
        while True:  # Officially the game loop
            self.timer_counter -= 1
            if self.timer_counter < 1:
                self.boardvisual.draw_new_board()
                self.timer_counter = self.timer_counter_magigy

            # Capture frame-by-frame
            ret, frame = self.video_capture.read()
            self.look_for_colours(frame)

            k = cv2.waitKey(100)

            # Redundancy testing
            if not self.red_found and not self.green_found and not self.blue_found \
                    and not self.cyan_found and not self.yellow_found and not self.magenta_found \
                    and not self.black_found and not self.white_found:
                self.none_found = True
                if self.spot_counter > 0:
                    print("neh...")
                self.spot_counter = 0

            # Display the resulting frame
            cv2.imshow('Windowname', frame)

            # Makes the play depending on either keyboard input or the colour detection
            if self.yellow_found or k == ord('q'):  # If yellow played
                if self.spot_counter > self.intensity or k == ord('q'):
                    print("YELLOW!")
                    for place_in_color_list in range(0, 8):
                        if self.boardvisual.colourimages_list[place_in_color_list][1] == 7:  # Looks for the yellow tag
                            if self.boardvisual.positions_status[place_in_color_list] == 0:
                                self.boardvisual.positions_status[place_in_color_list] = 2
                                self.boardvisual.ai_turn = True
                                self.spot_counter = 0
                                self.boardvisual.play_round()
                            else:
                                print("try another move")
                elif not self.none_found:
                    print("yellow?")
                    self.spot_counter += 1
                self.yellow_found = False

            elif k == ord('w'):  # Empty play (saved for white)
                if self.boardvisual.positions_status[1] == 0:
                    self.boardvisual.positions_status[1] = 2
                    self.boardvisual.ai_turn = True
                    self.boardvisual.play_round()
                else:
                    print("try another move")

            elif self.green_found or k == ord('e'):  # If green played
                if self.spot_counter > self.intensity or k == ord('e'):
                    print("GREEN!")
                    for place_in_color_list in range(0, 8):
                        if self.boardvisual.colourimages_list[place_in_color_list][1] == 3:  # Looks for the green tag
                            if self.boardvisual.positions_status[place_in_color_list] == 0:
                                self.boardvisual.positions_status[place_in_color_list] = 2
                                self.boardvisual.ai_turn = True
                                self.spot_counter = 0
                                self.boardvisual.play_round()
                            else:
                                print("try another move")
                elif not self.none_found:
                    print("green?")
                    self.spot_counter += 1
                self.green_found = False

            elif self.cyan_found or k == ord('a'):  # If cyan played
                if self.spot_counter > self.intensity or k == ord('a'):
                    print("CYAN!")
                    for place_in_color_list in range(0, 8):
                        if self.boardvisual.colourimages_list[place_in_color_list][1] == 2:  # Looks for the cyan tag
                            if self.boardvisual.positions_status[place_in_color_list] == 0:
                                self.boardvisual.positions_status[place_in_color_list] = 2
                                self.boardvisual.ai_turn = True
                                self.spot_counter = 0
                                self.boardvisual.play_round()
                            else:
                                print("try another move")
                elif not self.none_found:
                    print("cyan?")
                    self.spot_counter += 1
                self.cyan_found = False

            elif self.blue_found or k == ord('s'):  # If blue played
                if self.spot_counter > self.intensity or k == ord('s'):
                    print("BLUE!")
                    for place_in_color_list in range(0, 8):
                        if self.boardvisual.colourimages_list[place_in_color_list][1] == 1:  # Looks for the blue tag
                            if self.boardvisual.positions_status[place_in_color_list] == 0:
                                self.boardvisual.positions_status[place_in_color_list] = 2
                                self.boardvisual.ai_turn = True
                                self.spot_counter = 0
                                self.boardvisual.play_round()
                            else:
                                print("try another move")
                elif not self.none_found:
                    print("blue?")
                    self.spot_counter += 1
                self.blue_found = False

            elif self.red_found or k == ord('d'):  # If red played
                if self.spot_counter > self.intensity or k == ord('d'):
                    print("RED!")
                    for place_in_color_list in range(0, 8):
                        if self.boardvisual.colourimages_list[place_in_color_list][1] == 5:  # Looks for the red tag
                            if self.boardvisual.positions_status[place_in_color_list] == 0:
                                self.boardvisual.positions_status[place_in_color_list] = 2
                                self.boardvisual.ai_turn = True
                                self.spot_counter = 0
                                self.boardvisual.play_round()
                            else:
                                print("try another move")
                elif not self.none_found:
                    print("red?")
                    self.spot_counter += 1
                self.red_found = False

            elif self.magenta_found or k == ord('z'):  # If magenta played
                if self.spot_counter > self.intensity or k == ord('z'):
                    print("MAGENTA!")
                    for place_in_color_list in range(0, 8):
                        if self.boardvisual.colourimages_list[place_in_color_list][1] == 4:  # Looks for the magenta tag
                            if self.boardvisual.positions_status[place_in_color_list] == 0:
                                self.boardvisual.positions_status[place_in_color_list] = 2
                                self.boardvisual.ai_turn = True
                                self.spot_counter = 0
                                self.boardvisual.play_round()
                            else:
                                print("try another move")
                elif not self.none_found:
                    print("magenta?")
                    self.spot_counter += 1
                self.magenta_found = False

            elif self.black_found or k == ord('x'):  # If black played
                if self.spot_counter > self.intensity or k == ord('x'):
                    print("BLACK!")
                    for place_in_color_list in range(0, 8):
                        if self.boardvisual.colourimages_list[place_in_color_list][1] == 0:  # Looks for the black tag
                            if self.boardvisual.positions_status[place_in_color_list] == 0:
                                self.boardvisual.positions_status[place_in_color_list] = 2
                                self.boardvisual.ai_turn = True
                                self.spot_counter = 0
                                self.boardvisual.play_round()
                            else:
                                print("try another move")
                elif not self.none_found:
                    print("black?")
                    self.spot_counter += 1
                self.black_found = False

            elif k == ord('c'):  # Empty, reserved for testing
                if self.boardvisual.positions_status[8] == 0:
                    self.boardvisual.positions_status[8] = 2
                    self.boardvisual.ai_turn = True
                    self.boardvisual.play_round()
                else:
                    print("try another move")

            # Serves to increase and decrease the amount of time between the color changes in game
            elif k == ord('n'):
                self.timer_counter_magigy += 1
                print(self.timer_counter_magigy)
            elif k == ord('m'):
                self.timer_counter_magigy -= 1
                print(self.timer_counter_magigy)

    def look_for_colours(self, frame):
        # self.black_questionmark(frame)
        self.blue_questionmark(frame)
        self.cyan_questionmark(frame)
        self.green_questionmark(frame)
        self.magenta_questionmark(frame)
        self.red_questionmark(frame)
        self.yellow_questionmark(frame)
        # self.white_questionmark(frame)

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
                    whiteness += 1
        if whiteness >= 1500:
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
                    whiteness += 1
        if whiteness >= 1500:
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
                    whiteness += 1
        if whiteness >= 1500:
            # Object confirmed
            self.cyan_found = True
            self.none_found = False

    def green_questionmark(self, frame):
        # Determine the spotting range of GREEN
        lower_range = np.array([90, 90, 50])
        upper_range = np.array([120, 120, 80])

        # Filter out from the capture the RED object
        paper_colour_tag = cv2.inRange(frame, lower_range, upper_range)

        # Determine if there is indeed an object in the image
        height = int(format(paper_colour_tag.shape[0]))
        width = int(format(paper_colour_tag.shape[1]))
        whiteness = 0
        for i in range(0, height - 1, 4):
            for j in range(0, width - 1, 4):
                if paper_colour_tag[i, j] > 200:
                    whiteness += 1
        if whiteness >= 1500:
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
                    whiteness += 1
        if whiteness >= 1500:
            # Object confirmed
            self.magenta_found = True
            self.none_found = False

    def red_questionmark(self, frame):
        # Determine the spotting range of RED
        lower_range = np.array([20, 40, 140])
        upper_range = np.array([50, 70, 160])

        # Filter out from the capture the RED object
        paper_colour_tag = cv2.inRange(frame, lower_range, upper_range)

        # Determine if there is indeed an object in the image
        height = int(format(paper_colour_tag.shape[0]))
        width = int(format(paper_colour_tag.shape[1]))
        whiteness = 0
        for i in range(0, height - 1, 4):
            for j in range(0, width - 1, 4):
                if paper_colour_tag[i, j] > 200:
                    whiteness += 1
        if whiteness >= 1500:
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
                    whiteness += 1
        if whiteness >= 1500:
            # Object confirmed
            self.yellow_found = True
            self.none_found = False

    def white_questionmark(self, frame):
        print("?")