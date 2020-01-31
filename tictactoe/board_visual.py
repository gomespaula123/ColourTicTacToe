import pygame
import random
import cv2


# Runs all the code that relates to anything that causes the gameboard to change
class BoardVisual:

    def __init__(self, game, humanplayer, boardanalysis, aiplayer):
        # Inheritance of variables
        self.game = game
        self.humanplayer = humanplayer
        self.boardanalysis = boardanalysis
        self.aiplayer = aiplayer

        # Defining local variables
        self.screen = None
        self.colourimages_list = None
        self.ai_turn = None

        # Creating the starting game board with the ai’s first move already made as a mean of heuristic
        self.positions_status = [0, 0, 0, 0, 0, 0, 0, 0, 1]

    def create_window(self, screen):
        background_colour = (255, 255, 255)
        self.screen = screen
        screen.fill(background_colour)
        self.play_round()
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def play_round(self):
        if self.ai_turn:
            self.aiplayer.do_move()
            self.draw_new_board()
        else:
            self.draw_new_board()  # Updates the game window

        if self.boardanalysis.check_win_circle(self.positions_status):
            print("GAME OVER")
            self.quit_game()

        if self.boardanalysis.check_win_square(self.positions_status):
            print("CONGRATULATIONS: YOU WIN")
            self.quit_game()

        if self.boardanalysis.check_full(self.positions_status):
            self.quit_game()

        print("Waiting on your move")
        self.humanplayer.human_move()

    # Renders the current game board
    def draw_new_board(self):
        # loading all the images:
        brown_im = pygame.image.load('Brown.png')
        blue_im = pygame.image.load('Blue.png')
        cyan_im = pygame.image.load('Cyan.png')
        green_im = pygame.image.load('Green.png')
        magenta_im = pygame.image.load('Magenta.png')
        red_im = pygame.image.load('Red.png')
        orange_im = pygame.image.load('Orange.png')
        yellow_im = pygame.image.load('Yellow.png')
        board_im = pygame.image.load('boardimage.png')
        c_mark = pygame.image.load('Circle.png')
        s_mark = pygame.image.load('Square.png')

        self.colourimages_list = [(brown_im, 0), (blue_im, 1), (cyan_im, 2), (green_im, 3),
                                  (magenta_im, 4), (red_im, 5), (orange_im, 6), (yellow_im, 7)]

        positions_list = [(50, 50), (250, 50), (450, 50), (50, 250), (250, 250),
                          (450, 250), (50, 450), (250, 450), (450, 450)]

        self.change_positions()

        for i in range(0, 9):
            if self.positions_status[i] == 0:
                self.screen.blit(self.colourimages_list[i][0], positions_list[i])
            elif self.positions_status[i] == 1:  # draw circle
                self.screen.blit(c_mark, positions_list[i])
            elif self.positions_status[i] == 2:  # draw square
                self.screen.blit(s_mark, positions_list[i])

        self.screen.blit(board_im, (45, 50))
        pygame.display.update()

    # Randomly replaces the colors on the game board
    def change_positions(self):
        random.shuffle(self.colourimages_list)

    def quit_game(self):
        cv2.VideoCapture.release(self.humanplayer.video_capture)
        cv2.destroyAllWindows()
        pygame.quit()
        exit()
