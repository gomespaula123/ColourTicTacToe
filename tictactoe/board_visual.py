# visual for board
import pygame
from PIL import Image, ImageDraw
import glob


class BoardVisual:

    def __init__(self, game):
        print("this exists")
        # self.row_length = int(math.sqrt(len(self.board)))
        # self.create_board()
        self.game = game
        # im = Image.open("Black.png")
        colourimages_list = []
        # screen = pygame.display.set_mode((700, 700))

    def create_window(self):
        print("it has been called for once")
        background_colour = (255, 255, 255)
        black_im = pygame.image.load('Black.png')
        green_im = pygame.image.load('Green.png')
        blue_im = pygame.image.load('Blue.png')
        screen = pygame.display.set_mode((700, 700))
        screen.fill(background_colour)
        screen.blit(black_im, (50, 50))
        screen.blit(green_im, (250, 50))
        screen.blit(blue_im, (450, 50))

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





