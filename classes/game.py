# Imports
import pygame
from .constants import FILL_COLOR, LINE_COLOR, WIDTH, HEIGHT, ROWS, COLS
from .board import Board


class Game:
    """Represents the current game being played"""

    # class constants
    FONT_SIZE = WIDTH // 20
    TOTAL_TURNS = ROWS * COLS
    TOTAL_CONDITIONS = ROWS + COLS + 2  # Rows, Columns, and Diagonals

    def __init__(self, window):
        """Creates game object and initializes window data member."""
        self.window = window
        self._init()

    def _init(self):
        """Initializes other data members which can be used for a reset."""
        self.board = Board()
        self.current_player = self.board.player_x
        self.turn_counter = 0

    def reset(self):
        """Resets board for a new game."""
        self._init()

    def update(self):
        """Updates the game by redrawing the board."""
        self.board.draw(self.window)
        if self.outcome() is not None:
            outcome = self.outcome()
            # If tied, display appropriate message/invite to play again.
            if outcome == 'Tie':
                self._display_message("It's a Tie! Play again: y or n?")

            # If winner, display appropriate message/invite to play again.
            else:
                text = outcome + " is the winner! Play again: y or n?"
                self._display_message(text)

        # Update Board
        pygame.display.update()

    def outcome(self):
        """Checks all conditions for winner. Returns player or 'Tie' if met, else None."""
        # Board list
        board_list = self.board.board

        # Dictionary of unwinnable conditions
        impossible_dict = {}

        # Across
        for row in range(ROWS):
            if self.board.impossible_condition(board_list[row]):
                key = 'across' + str(row)
                impossible_dict[key] = 'impossible'
            elif self.board.winner_condition(board_list[row]):
                return board_list[row][0].team

        # Down
        for col in range(COLS):
            column_list = []
            for row in range(ROWS):
                column_list.append(board_list[row][col])
            if self.board.impossible_condition(column_list):
                key = 'down' + str(col)
                impossible_dict[key] = 'impossible'
            elif self.board.winner_condition(column_list):
                return column_list[0].team

        # Diagonals
        diagonal_list = []
        for row in range(ROWS):
            diagonal_list.append(board_list[row][row])
        if self.board.impossible_condition(diagonal_list):
            impossible_dict['forward_diagonal'] = 'impossible'
        elif self.board.winner_condition(diagonal_list):
            return diagonal_list[0].team
        diagonal_list.clear()

        for row in range(ROWS):
            diagonal_list.append(board_list[row][ROWS - 1 - row])
        if self.board.impossible_condition(diagonal_list):
            impossible_dict['backward_diagonal'] = 'impossible'
        elif self.board.winner_condition(diagonal_list):
            return diagonal_list[0].team

        # Tie
        if self.turn_counter >= self.TOTAL_TURNS or len(impossible_dict) >= self.TOTAL_CONDITIONS:
            return 'Tie'

    def turn(self, col, row):
        """Runs turn for current player."""
        # Valid move
        if self.board.board[row][col] == 0:
            self.board.board[row][col] = self.current_player
            self._change_player()
            self.turn_counter += 1

        # If move is invalid
        else:
            self._display_message('Invalid Move. Try Again!')
            pygame.display.update()
            pygame.time.wait(900)  # Display message for 0.9 seconds only

    def _change_player(self):
        """Swaps to other player."""
        if self.current_player == self.board.player_x:
            self.current_player = self.board.player_o
        else:
            self.current_player = self.board.player_x

    def _display_message(self, message):
        """Displays message to middle of game board."""
        font = pygame.font.SysFont('comicsans', self.FONT_SIZE)
        text = font.render(message, True, FILL_COLOR, LINE_COLOR)
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 2)
        self.window.blit(text, text_rect)
