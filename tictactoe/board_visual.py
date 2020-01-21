# visual for board
import pygame


class BoardVisual:
    def __init__(self):
        self.board = [" "] * 9
        # self.row_length = int(math.sqrt(len(self.board)))

    def create_board(self):
        print("it has been called for once")
        background_colour = (255, 255, 255)
        screen = pygame.display.set_mode((700, 700))
        self.screen.fill(background_colour)
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
