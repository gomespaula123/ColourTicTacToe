# visual for board
import pygame
from PIL import Image, ImageDraw
import random


class BoardVisual:

    def __init__(self, game, humanplayer, boardanalysis, aiplayer):
        self.game = game
        self.humanplayer = humanplayer  # test
        self.boardanalysis = boardanalysis
        self.aiplayer = aiplayer
        self.colourimages_list = None

        # Test the display of plays
        self.positions_status = [0, 0, 0, 0, 0, 0, 0, 0, 1]
        self.ai_turn = None


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
        self.draw_new_board()

        self.boardanalysis.check_win_circle(self.positions_status)
        self.boardanalysis.check_win_square(self.positions_status)
#        print(self.ai_turn)
        self.boardanalysis.check_full(self.positions_status)
        if self.ai_turn:
            self.aiplayer.do_move()
        print("waiting on your move")
        self.humanplayer.human_move()
        print("got here")

        # send the list of positions status to board analysis

        # self.boardanalysis.test_function1()

    def change_positions(self):
        random.shuffle(self.colourimages_list)

    def draw_new_board(self):
        # loading all the images:
        black_im = pygame.image.load('Black.png')
        blue_im = pygame.image.load('Blue.png')
        cyan_im = pygame.image.load('Cyan.png')
        green_im = pygame.image.load('Green.png')
        magenta_im = pygame.image.load('Magenta.png')
        red_im = pygame.image.load('Red.png')
        white_im = pygame.image.load('White.png')
        yellow_im = pygame.image.load('Yellow.png')
        board_im = pygame.image.load('boardimage.png')
        # emptysqr_im = pygame.image.load('emptybox.png')
        c_mark = pygame.image.load('Circle.png')
        s_mark = pygame.image.load('Square.png')

        self.colourimages_list = [(black_im, 0), (blue_im, 1), (cyan_im, 2), (green_im, 3),
                                  (magenta_im, 4), (red_im, 5), (white_im, 6), (yellow_im, 7)]

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