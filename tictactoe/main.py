import pygame
from tictactoe.board_visual import BoardVisual
from tictactoe.human_player import HumanPlayer
from tictactoe.board_analysis import BoardAnalysis
from tictactoe.ai_player import AIPlayer
# Reference note: http://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/creating-pygame-window/


class Game:
    def __init__(self):
        self.game = None
        pygame.init()

        # Launch the video capture and the logic that allows the user to play the game
        self.human_player = HumanPlayer(self.game)

        # Holds the logic for the board such as determining if someone won
        self.board_analysis = BoardAnalysis(self.game)

        # AI engine for the opponent
        self.ai_player = AIPlayer(self.game, self.board_analysis)

        # Updates the renderer with what to show in the game board
        self.board_visual = BoardVisual(self.game, self.human_player, self.board_analysis, self.ai_player)

        # Includes the generated game board in the previously generated board logic engine
        self.board_analysis.set_board(self.board_visual)

        # Connects the players to the actual game such that they can interact with the board
        self.human_player.set_board(self.board_visual)
        self.ai_player.set_board(self.board_visual)

        # Move into the rendering process
        self.draw_board()

    def draw_board(self):
        print("Ready to start!")
        screen = pygame.display.set_mode((700, 700))
        pygame.display.flip()

        # Starts running the game loop
        self.board_visual.create_window(screen)


# Starts the game
if __name__ == "__main__":
    game = Game()
