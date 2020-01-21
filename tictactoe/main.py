import pygame
from tictactoe.board_visual import BoardVisual
# Reference note: http://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/creating-pygame-window/


class Game:

    def __init__(self):

        self.game = None
        pygame.init()
        self.board_visual = BoardVisual(self.game)

    def game_loop(self):
        print("prints game loop")
        self.draw_board()

    def draw_board(self):
        print("prints draw board")
        # self.screen.fill([255, 255, 255])
        screen = pygame.display.set_mode((700, 700))
        self.board_visual.create_window(screen)
        self.board_visual.place_fields()
        # self.board_visual.create_window()
        pygame.display.flip()


'''
background_colour = (255, 255, 255)
screen = pygame.display.set_mode((700, 700))
screen.fill(background_colour)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
'''

if __name__ == "__main__":
    game = Game()
    while True:
        game.game_loop()