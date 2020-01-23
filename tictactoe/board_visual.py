# visual for board
import pygame
from PIL import Image, ImageDraw
import random


class BoardVisual:

    def __init__(self, game, humanplayer, boardanalysis, aiplayer):
        self.game = game
        self.humanplayer = humanplayer  # test
        self.aiplayer = aiplayer
        self.boardanalysis = boardanalysis
        self.positions_status = [0, 0, 1, 0, 0, 0, 0, 0, 1]


    def create_window(self, screen):
        background_colour = (255, 255, 255)
        self.screen = screen
        screen.fill(background_colour)
        self.getcolour_images()

        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def getcolour_images(self):
        # print("it does the thing now food")
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
        self.colourimages_list = [black_im, blue_im, cyan_im, green_im, magenta_im, red_im, white_im, yellow_im]

        positions_list = [(50, 50), (250, 50), (450, 50), (50, 250), (250, 250), (450, 250), (50, 450), (250, 450), (450, 450)]
        # random.shuffle(self.colourimages_list)
        self.change_positions()
        self.boardanalysis.get_positions()
        # self.boardanalysis.check_lose()
        # self.boardanalysis.check_win()

        for i in range(0, 9):
            if self.positions_status[i] == 0:
                self.screen.blit(self.colourimages_list[i], positions_list[i])
            elif self.positions_status[i] == 1:  # draw circle
                self.screen.blit(c_mark, positions_list[i])
            elif self.positions_status[i] == 2:  # draw square
                self.screen.blit(s_mark, positions_list[i])

        self.screen.blit(board_im, (45, 50))
        pygame.display.update()
        self.boardanalysis.check_lose()
        self.boardanalysis.check_win()
        # self.boardanalysis.test_function1()
        self.aiplayer.testai_playerfunction()
        self.aiplayer.get_possible_moves()
        self.aiplayer.calculate_next_move1()
        # self.aiplayer.calculate_next_move(self.positions_status)
        # self.aiplayer.calculate_next_move(self.positions_status)
        self.humanplayer.webcam_setup()
        # send the list of positions status to board analysis

        # self.boardanalysis.test_function1()

    def change_positions(self):
        random.shuffle(self.colourimages_list)




