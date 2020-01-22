# visual for board
import pygame
from PIL import Image, ImageDraw
import random
import cv2
from tictactoe.human_player import HumanPlayer


class BoardVisual:

    def __init__(self, game):
        # print("this exists")
        self.game = game
        self.human_player = HumanPlayer(self.game)
        # screen = pygame.display.set_mode((700, 700))

    def create_window(self, screen):
        # print("it has been called for once")
        background_colour = (255, 255, 255)
        # screen = pygame.display.set_mode((700, 700))
        screen.fill(background_colour)
        self.getcolour_images(screen)

        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    # def place_fields(self):
        # print("here it creates the fields")
        # im = Image.open(r"C:\Users\gomes\PycharmProjects\ColourTicTacToe\ColourImages\Black.png")
        # screen = pygame.display.set_mode((700, 700))
        # screen.blit(imtest, (0, 0))
        # pygame.display.flip()

    def getcolour_images(self, screen):
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
        emptysqr_im = pygame.image.load('emptybox.png')
        O_mark = pygame.image.load('Circle.png')
        colourimages_list = [black_im, blue_im, cyan_im, green_im, magenta_im, red_im, white_im, yellow_im]
        positions_list = [(50, 50), (250, 50), (450, 50), (50, 250), (250, 250), (450, 250), (50, 450), (250, 450), (450, 450)]
        random.shuffle(colourimages_list)
        screen.blit(colourimages_list[0], positions_list[0])
        screen.blit(colourimages_list[1], positions_list[1])
        screen.blit(colourimages_list[2], positions_list[2])
        screen.blit(colourimages_list[3], positions_list[3])
        screen.blit(colourimages_list[4], positions_list[4])
        screen.blit(colourimages_list[5], positions_list[5])
        screen.blit(colourimages_list[6], positions_list[6])
        screen.blit(colourimages_list[7], positions_list[7])
        # add all of the sets of x and y to a list "positions_list = [()]
        screen.blit(O_mark, positions_list[8])
        screen.blit(board_im, (45, 50))
        # self.human_player.get_webcaminput()
        self.human_player.webcam_setup()




        # screen.blit(random.choice(colourimages_list), (50, 50))
        # screen.blit(random.choice(colourimages_list), (250, 50))
        # screen.blit(random.choice(colourimages_list), (450, 50))
        # screen.blit(random.choice(colourimages_list), (50, 250))
        # screen.blit(random.choice(colourimages_list), (250, 250))
        # screen.blit(random.choice(colourimages_list), (450, 250))
        # screen.blit(random.choice(colourimages_list), (50, 450))
        # screen.blit(random.choice(colourimages_list), (250, 450))
        # screen.blit(random.choice(colourimages_list), (450, 450))








