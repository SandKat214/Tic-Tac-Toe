# Imports
import pygame
from .constants import SQUARE_SIZE, FILL_COLOR, LINE_COLOR, PLAYER_X, LINE_THICKNESS


class Player:
    """Represents one of two players on the board."""

    # class constants
    PADDING = 20

    def __init__(self, team):
        """Creates Player object and initializes team."""
        self.team = team

    def draw_glyph(self, window, col, row):
        """Draws proper glyph according to object team."""
        if self.team == PLAYER_X:  # X
            # Coordinates are top left corner of grid square
            x_coord = col * SQUARE_SIZE
            y_coord = row * SQUARE_SIZE

            # Draw 'X'
            pygame.draw.line(window, LINE_COLOR, (x_coord + self.PADDING, y_coord + self.PADDING),
                             (x_coord + SQUARE_SIZE - self.PADDING, y_coord + SQUARE_SIZE - self.PADDING),
                             LINE_THICKNESS)
            pygame.draw.line(window, LINE_COLOR, (x_coord + SQUARE_SIZE - self.PADDING, y_coord + self.PADDING),
                             (x_coord + self.PADDING, y_coord + SQUARE_SIZE - self.PADDING), LINE_THICKNESS)

        else:  # O
            # Coordinates are center of grid square
            x_coord = (col * SQUARE_SIZE) + (SQUARE_SIZE // 2)
            y_coord = (row * SQUARE_SIZE) + (SQUARE_SIZE // 2)

            # Draw 'O'
            radius = SQUARE_SIZE // 2 - self.PADDING
            pygame.draw.circle(window, LINE_COLOR, (x_coord, y_coord), radius)
            pygame.draw.circle(window, FILL_COLOR, (x_coord, y_coord), radius - LINE_THICKNESS)
