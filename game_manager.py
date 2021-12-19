import sys
import re
from board import Board
from client import *


class GameManager:

    def __init__(self):
        self._board = Board()
        self._current_player = None

    def marker_choice(self):
        while True:
            marker = input("Please choose your marker (x or o): ")
            if str(marker).isalpha() and len(marker) == 1:
                if marker.lower() == 'x' or marker.lower() == 'o':
                    return marker.lower()
            print("It's not a valid symbol.")

    def replay_choice(self):
        while True:
            answer_play = input("Do you want to play again? (y or n): ")
            if str(answer_play).isalpha() and len(answer_play) == 1:
                if answer_play.lower() == 'y':
                    return True
                elif answer_play.lower() == 'n':
                    return False
                else:
                    print("It's not a valid symbol.")

    def tile_choice(self):
        while True:
            print("Current player: " + self._current_player)
            tile_id = input("Please choose an unoccupied tile - from 1 to 9. ")
            num_format = re.compile(r'^[1-9]$')
            if re.match(num_format, tile_id):
                tile_id = int(tile_id) - 1
                if self._board.check_can_place(tile_id):
                    return tile_id
                else:
                    print("This tile is occupied.")
            else:
                print("It's not a valid symbol.")

    def replay(self):
        if self.replay_choice():
            self._board.reset()
        else:
            sys.exit(0)

    def set_player(self):
        self._current_player = self.marker_choice()

    def switch_player(self):
        self._current_player = 'x' if self._current_player == 'o' else 'o'

    def place_marker(self):
        tile_id = self.tile_choice()
        marker = self._current_player
        self._board.place(marker, tile_id)

    def has_ended(self):
        if self._board.check_win():
            self.switch_player()
            print("Congratulations! Player: " + self._current_player + " won!")
            return True
        elif self._board.check_full():
            print("It's a draw!")
            return True
        return False

    def play_game(self):
        print("Welcome to Tick-Tack-Toe!")
        while True:
            self.set_player()
            self._board.draw()
            while not self.has_ended():
                self.place_marker()
                self._board.draw()
                self.switch_player()
            self.replay()

