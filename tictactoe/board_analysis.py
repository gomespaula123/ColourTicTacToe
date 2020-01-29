import sys
import pygame
import cv2

class BoardAnalysis:

    def __init__(self, game):
        self.game = game
        # self.boardvisual = boardvisual
        # self.humanplayer = humanplayer  # test
        # self.boardvisual = boardvisual

    def set_board(self, boardvisual):
        self.boardvisual = boardvisual

    def get_positions(self):
        # self.boardvisual.positions_status[6] = 2
        print(*self.boardvisual.positions_status)
        # self.boardvisual.getcolour_images()

    def check_lose(self, game_being_analysed):
        lose = False
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
            lose = True
            print(lose)
            print("you lost")
            # self.quit_game()
        return lose

    def check_win(self, game_being_analysed):
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
            print(win)
            print("you won")
        return win

    def check_full(self, game_being_analysed):
        full = False
        if 0 not in game_being_analysed:
            full = True
            print(full)
            print("board is full")



    def quit_game(self):
        # self.video_capture.release()
        cv2.destroyAllWindows()
        pygame.quit()
        sys.exit()




    # def test_function1(self):
        # print("test_function1")
        # self.humanplayer.webcam_setup()

