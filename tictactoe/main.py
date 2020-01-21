import pygame

# Reference note: http://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/creating-pygame-window/


# class Game:

    # def __init__(self):
        # pygame.init()


background_colour = (255,255,255)
(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False