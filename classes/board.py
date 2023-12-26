# Imports
import pygame
from .constants import ROWS, COLS, SQUARE_SIZE, LINE_COLOR, FILL_COLOR, PLAYER_X, PLAYER_O, LINE_THICKNESS
from .player import Player


class Board:
    """Represents the game board on which the game is being played."""

    def __init__(self):
        """Creates a board object & initializes data members."""
        self.board = []
        self.player_x = Player(PLAYER_X)
        self.player_o = Player(PLAYER_O)
        self._create_board()

    def _create_board(self):
        """Creates a representation of the game board as a list that can be updated throughout play."""
        # Initializes all grid positions to zero
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)

    @staticmethod
    def _draw_grid_lines(window):
        """Draws the grind lines on the background window."""
        window.fill(FILL_COLOR)
        for col in range(1, COLS):
            pygame.draw.line(window, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, COLS * SQUARE_SIZE),
                             LINE_THICKNESS)
            pygame.draw.line(window, LINE_COLOR, (0, col * SQUARE_SIZE), (COLS * SQUARE_SIZE, col * SQUARE_SIZE),
                             LINE_THICKNESS)

    def draw(self, window):
        """Draws the grid window and also updates the player glyphs according to the board list."""
        self._draw_grid_lines(window)
        for row in range(ROWS):
            for col in range(COLS):
                position = self.board[row][col]
                if position != 0:
                    position.draw_glyph(window, col, row)

    @staticmethod
    def _list_element_count(element_list):
        """Returns the number of list elements if a condition is a win or no longer viable. Else None."""
        list_element_count = len(set(element_list))
        if 0 not in element_list:
            # Winner.
            if list_element_count == 1:
                return 1
            # Can't Win.
            else:
                return 2
        # Can't Win.
        elif list_element_count == 3:
            return 3
        # Keep playing.
        return 0

    def impossible_condition(self, condition_list):
        """Returns True if condition cannot accommodate a winner based on the current board."""
        if self._list_element_count(condition_list) > 1:
            return True
        return False

    def winner_condition(self, condition_list):
        """Returns True if condition is a winner."""
        if self._list_element_count(condition_list) == 1:
            return True
        return False
