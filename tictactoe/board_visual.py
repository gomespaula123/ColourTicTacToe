# visual for board
import pygame


class BoardVisual:

    def __init__(self, game):
        print("this exists")
        # self.row_length = int(math.sqrt(len(self.board)))
        # self.create_board()
        self.game = game

    def create_window(self):
        print("it has been called for once")
        background_colour = (255, 255, 255)
        screen = pygame.display.set_mode((700, 700))
        screen.fill(background_colour)
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def create_fields(self):
        print("here it creates the fields")

