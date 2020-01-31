import cv2
import numpy as np
# tutorial used to get started: https://towardsdatascience.com/https-medium-com-dilan-jay-face-detection-model-on-webcam-using-python-72b382699ee9


class HumanPlayer:

    def __init__(self, game):
        # Inheritance of variables
        self.game = game

        # Defining local variables
        self.screen = None
        self.boardvisual = None
        self.video_capture = cv2.VideoCapture(0)

        # Initialize the variables used for the color detection
        self.brown_found = False
        self.blue_found = False
        self.cyan_found = False
        self.green_found = False
        self.magenta_found = False
        self.red_found = False
        self.yellow_found = False
        self.orange_found = False

        # For redundancy testing
        self.intensity = 3  # Increases the amount of times that the test is ran
        self.none_found = True
        self.spot_counter = 0

        # Time for the player to present the color that they want to play
        self.timer_counter_magigy = 10  # ..
        self.timer_counter = self.timer_counter_magigy

    # Inherent boardvisual as well
    def set_board(self, boardvisual):
        self.boardvisual = boardvisual

    def human_move(self):
        while True:  # Listening to the player

            # Timer for the shuffling of the colors in the board
            self.timer_counter -= 1
            if self.timer_counter < 1:
                self.boardvisual.draw_new_board()
                self.timer_counter = self.timer_counter_magigy

            # Capture frame-by-frame
            ret, frame = self.video_capture.read()
            self.look_for_colours(frame)

            # Interupt shedule for the keyboard presses
            k = cv2.waitKey(1)

            # Redundancy testing
            if not self.red_found and not self.green_found and not self.blue_found \
                    and not self.cyan_found and not self.yellow_found and not self.magenta_found \
                    and not self.brown_found and not self.orange_found:
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
                                self.boardvisual.play_round()  # Recurses into a new game round rendering the game loop
                            else:
                                print("try another move")
                elif not self.none_found:
                    print("yellow?")
                    self.spot_counter += 1
                self.yellow_found = False

            elif self.orange_found or k == ord('w'):  # If orange played)
                if self.spot_counter > self.intensity or k == ord('q'):
                    print("ORANGE!")
                    for place_in_color_list in range(0, 8):
                        if self.boardvisual.colourimages_list[place_in_color_list][1] == 6:  # Looks for the orange tag
                            if self.boardvisual.positions_status[place_in_color_list] == 0:
                                self.boardvisual.positions_status[place_in_color_list] = 2
                                self.boardvisual.ai_turn = True
                                self.spot_counter = 0
                                self.boardvisual.play_round()  # Recurses into a new game round rendering the game loop
                            else:
                                print("try another move")
                elif not self.none_found:
                    print("orange?")
                    self.spot_counter += 1
                self.yellow_found = False

            elif self.green_found or k == ord('e'):  # If green played
                if self.spot_counter > self.intensity or k == ord('e'):
                    print("GREEN!")
                    for place_in_color_list in range(0, 8):
                        if self.boardvisual.colourimages_list[place_in_color_list][1] == 3:  # Looks for the green tag
                            if self.boardvisual.positions_status[place_in_color_list] == 0:
                                self.boardvisual.positions_status[place_in_color_list] = 2
                                self.boardvisual.ai_turn = True
                                self.spot_counter = 0
                                self.boardvisual.play_round()  # Recurses into a new game round rendering the game loop
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
                                self.boardvisual.play_round()  # Recurses into a new game round rendering the game loop
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
                                self.boardvisual.play_round()  # Recurses into a new game round rendering the game loop
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
                                self.boardvisual.play_round()  # Recurses into a new game round rendering the game loop
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
                                self.boardvisual.play_round()  # Recurses into a new game round rendering the game loop
                            else:
                                print("try another move")
                elif not self.none_found:
                    print("magenta?")
                    self.spot_counter += 1
                self.magenta_found = False

            elif self.brown_found or k == ord('x'):  # If brown played
                if self.spot_counter > self.intensity or k == ord('x'):
                    print("brown!")
                    for place_in_color_list in range(0, 8):
                        if self.boardvisual.colourimages_list[place_in_color_list][1] == 0:  # Looks for the brown tag
                            if self.boardvisual.positions_status[place_in_color_list] == 0:
                                self.boardvisual.positions_status[place_in_color_list] = 2
                                self.boardvisual.ai_turn = True
                                self.spot_counter = 0
                                self.boardvisual.play_round()  # Recurses into a new game round rendering the game loop
                            else:
                                print("try another move")
                elif not self.none_found:
                    print("brown?")
                    self.spot_counter += 1
                self.brown_found = False

            elif k == ord('c'):  # Empty, reserved for testing
                if self.boardvisual.positions_status[8] == 0:
                    self.boardvisual.positions_status[8] = 2
                    self.boardvisual.ai_turn = True
                    self.boardvisual.play_round()  # Recurses into a new game round rendering the game loop
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
        self.brown_questionmark(frame)
        self.blue_questionmark(frame)
        self.cyan_questionmark(frame)
        self.green_questionmark(frame)
        self.magenta_questionmark(frame)
        self.red_questionmark(frame)
        self.yellow_questionmark(frame)
        self.orange_questionmark(frame)

    def brown_questionmark(self, frame):
        # Determine the spotting range of brown
        lower_range = np.array([50, 70, 120])
        upper_range = np.array([100, 100, 140])

        # Filter out from the capture the brown object
        paper_colour_tag = cv2.inRange(frame, lower_range, upper_range)

        # Determine if there is indeed an object in the image
        height = int(format(paper_colour_tag.shape[0]))
        width = int(format(paper_colour_tag.shape[1]))
        whiteness = 0
        for i in range(0, height - 1, 4):
            for j in range(0, width - 1, 4):
                if paper_colour_tag[i, j] > 200:
                    whiteness += 1
        if whiteness >= 1500:  # Sensitivity to color
            # Object confirmed
            self.brown_found = True
            self.none_found = False

    def blue_questionmark(self, frame):
        # Determine the spotting range of BLUE
        lower_range = np.array([110, 50, 0])
        upper_range = np.array([150, 70, 30])

        # Filter out from the capture the BLUE object
        paper_colour_tag = cv2.inRange(frame, lower_range, upper_range)

        # Determine if there is indeed an object in the image
        height = int(format(paper_colour_tag.shape[0]))
        width = int(format(paper_colour_tag.shape[1]))
        whiteness = 0
        for i in range(0, height - 1, 4):
            for j in range(0, width - 1, 4):
                if paper_colour_tag[i, j] > 200:
                    whiteness += 1
        if whiteness >= 1500:  # Sensitivity to color
            # Object confirmed
            self.blue_found = True
            self.none_found = False

    def cyan_questionmark(self, frame):
        # Determine the spotting range of CYAN
        lower_range = np.array([70, 60, 10])
        upper_range = np.array([100, 80, 50])

        # Filter out from the capture the CYAN object
        paper_colour_tag = cv2.inRange(frame, lower_range, upper_range)

        # Determine if there is indeed an object in the image
        height = int(format(paper_colour_tag.shape[0]))
        width = int(format(paper_colour_tag.shape[1]))
        whiteness = 0
        for i in range(0, height - 1, 4):
            for j in range(0, width - 1, 4):
                if paper_colour_tag[i, j] > 200:
                    whiteness += 1
        if whiteness >= 1500:  # Sensitivity to color
            # Object confirmed
            self.cyan_found = True
            self.none_found = False

    def green_questionmark(self, frame):
        # Determine the spotting range of GREEN
        lower_range = np.array([40, 60, 20])
        upper_range = np.array([80, 90, 50])

        # Filter out from the capture the GREEN object
        paper_colour_tag = cv2.inRange(frame, lower_range, upper_range)

        # Determine if there is indeed an object in the image
        height = int(format(paper_colour_tag.shape[0]))
        width = int(format(paper_colour_tag.shape[1]))
        whiteness = 0
        for i in range(0, height - 1, 4):
            for j in range(0, width - 1, 4):
                if paper_colour_tag[i, j] > 200:
                    whiteness += 1
        if whiteness >= 1500:  # Sensitivity to color
            # Object confirmed
            self.green_found = True
            self.none_found = False

    def magenta_questionmark(self, frame):
        # Determine the spotting range of MAGENTA
        lower_range = np.array([70, 60, 140])
        upper_range = np.array([100, 90, 160])

        # Filter out from the capture the MAGENTA object
        paper_colour_tag = cv2.inRange(frame, lower_range, upper_range)

        # Determine if there is indeed an object in the image
        height = int(format(paper_colour_tag.shape[0]))
        width = int(format(paper_colour_tag.shape[1]))
        whiteness = 0
        for i in range(0, height - 1, 4):
            for j in range(0, width - 1, 4):
                if paper_colour_tag[i, j] > 200:
                    whiteness += 1
        if whiteness >= 1500:  # Sensitivity to color
            # Object confirmed
            self.magenta_found = True
            self.none_found = False

    def red_questionmark(self, frame):
        # Determine the spotting range of RED
        lower_range = np.array([20, 30, 110])
        upper_range = np.array([60, 70, 140])

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
        if whiteness >= 1500:  # Sensitivity to color
            # Object confirmed
            self.red_found = True
            self.none_found = False

    def yellow_questionmark(self, frame):
        # Determine the spotting range of YELLOW
        lower_range = np.array([50, 110, 110])
        upper_range = np.array([80, 130, 130])

        # Filter out from the capture the YELLOW object
        paper_colour_tag = cv2.inRange(frame, lower_range, upper_range)

        # Determine if there is indeed an object in the image
        height = int(format(paper_colour_tag.shape[0]))
        width = int(format(paper_colour_tag.shape[1]))
        whiteness = 0
        for i in range(0, height - 1, 4):
            for j in range(0, width - 1, 4):
                if paper_colour_tag[i, j] > 200:
                    whiteness += 1
        if whiteness >= 1500:  # Sensitivity to color
            # Object confirmed
            self.yellow_found = True
            self.none_found = False

    def orange_questionmark(self, frame):
        # Determine the spotting range of ORANGE
        lower_range = np.array([50, 80, 140])
        upper_range = np.array([80, 100, 160])

        # Filter out from the capture the YELLOW object
        paper_colour_tag = cv2.inRange(frame, lower_range, upper_range)

        # Determine if there is indeed an object in the image
        height = int(format(paper_colour_tag.shape[0]))
        width = int(format(paper_colour_tag.shape[1]))
        whiteness = 0
        for i in range(0, height - 1, 4):
            for j in range(0, width - 1, 4):
                if paper_colour_tag[i, j] > 200:
                    whiteness += 1
        if whiteness >= 1500:  # Sensitivity to color
            # Object confirmed
            self.orange_found = True
            self.none_found = False
