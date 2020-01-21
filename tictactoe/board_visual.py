# visual for board
import pygame
from PIL import Image, ImageDraw
import glob
import random


class BoardVisual:

    def __init__(self, game):
        print("this exists")
        # self.row_length = int(math.sqrt(len(self.board)))
        # self.create_board()
        self.game = game
        # im = Image.open("Black.png")
        colourimages_list = []
        # screen = pygame.display.set_mode((700, 700))

    def create_window(self, screen):
        print("it has been called for once")
        background_colour = (255, 255, 255)
        # black_im = pygame.image.load('Black.png')
        # green_im = pygame.image.load('Green.png')
        # blue_im = pygame.image.load('Blue.png')
        # screen = pygame.display.set_mode((700, 700))
        screen.fill(background_colour)
        self.getcolour_images(screen)
        # screen.blit(black_im, (50, 50))
        # screen.blit(green_im, (250, 50))
        # screen.blit(blue_im, (450, 50))

        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def place_fields(self):
        print("here it creates the fields")
        # im = Image.open(r"C:\Users\gomes\PycharmProjects\ColourTicTacToe\ColourImages\Black.png")
        imtest = pygame.image.load('Black.png')
        # screen = pygame.display.set_mode((700, 700))
        # screen.blit(imtest, (0, 0))
        # pygame.display.flip()

    def getcolour_images(self, screen):
        print("it does the thing now food")
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
        colourimages_list = [black_im, blue_im, cyan_im, green_im, magenta_im, red_im, white_im, yellow_im]
        random.shuffle(colourimages_list)
        screen.blit(colourimages_list[0], (50, 50))
        screen.blit(colourimages_list[1], (250, 50))
        screen.blit(colourimages_list[2], (450, 50))
        screen.blit(colourimages_list[3], (50, 250))
        screen.blit(colourimages_list[4], (250, 250))
        screen.blit(colourimages_list[5], (450, 250))
        screen.blit(colourimages_list[6], (50, 450))
        screen.blit(colourimages_list[7], (250, 450))

        screen.blit(emptysqr_im, (450, 450))

        screen.blit(board_im, (45, 50))





        # screen.blit(random.choice(colourimages_list), (50, 50))
        # screen.blit(random.choice(colourimages_list), (250, 50))
        # screen.blit(random.choice(colourimages_list), (450, 50))
        # screen.blit(random.choice(colourimages_list), (50, 250))
        # screen.blit(random.choice(colourimages_list), (250, 250))
        # screen.blit(random.choice(colourimages_list), (450, 250))
        # screen.blit(random.choice(colourimages_list), (50, 450))
        # screen.blit(random.choice(colourimages_list), (250, 450))
        # screen.blit(random.choice(colourimages_list), (450, 450))








