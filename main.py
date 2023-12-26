# Imports
import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_n, K_y, MOUSEBUTTONDOWN, QUIT
from classes.constants import WIDTH, HEIGHT, SQUARE_SIZE
from classes.game import Game

# Initialize pygame
pygame.init()

# Frames per second
FPS = 60

# Set game window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')


def get_col_row_from_mouse(position):
    """Takes mouse position as argument and returns the corresponding row & column position in the game grid."""
    x_coord, y_coord = position
    row = y_coord // SQUARE_SIZE
    col = x_coord // SQUARE_SIZE
    return col, row


def main():
    """Main game loop"""
    running = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    while running:
        # Sets tempo of the loop
        clock.tick(FPS)

        for event in pygame.event.get():
            # If the red 'x' is clicked
            if event.type == QUIT:
                running = False

            elif event.type == KEYDOWN:
                # If the 'esc' key is pressed
                if event.key == K_ESCAPE:
                    running = False

                # Game Over
                if game.outcome() is not None:
                    # Play again?
                    if event.key == K_y:
                        game.reset()
                    elif event.key == K_n:
                        running = False

            # If mouse button clicked
            elif event.type == MOUSEBUTTONDOWN and game.outcome() is None:
                position = pygame.mouse.get_pos()
                col, row = get_col_row_from_mouse(position)
                game.turn(col, row)

        # Update board
        game.update()

    pygame.quit()


if __name__ == '__main__':
    main()
