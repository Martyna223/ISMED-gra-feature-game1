class Board:
    def __init__(self):
        self._state = self._init_state()
        self._drawn_board = self._init_drawn_board()

    def _init_state(self):
        return ['#'] * 9

    def _init_drawn_board(self):
        return """
    ___________________
    |     |     |     |
    |  1  |  2  |  3  |
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  4  |  5  |  6  |
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  7  |  8  |  9  |
    |     |     |     |
    |-----------------|
    """

    def reset(self):
        self._state = self._init_state()
        self._drawn_board = self._init_drawn_board()

    def draw(self):
        print(self._drawn_board)

    def place(self, marker, tile_id):
        if self.check_can_place(tile_id):
            self._state[tile_id] = marker
            self._drawn_board = self._drawn_board.replace(str(tile_id+1), marker)
            return True, "Marker is placed."
        else:
            return False, "Cannot place marker."

    def check_can_place(self, tile_id):
        return self._state[tile_id] == '#'

    def check_full(self):
        return not any([tile == '#' for tile in self._state])

    def check_win(self):
        # horizontal check
        for i in range(0, 7, 3):
            if self._state[i] == self._state[i+1] == self._state[i+2] and self._state[i] != '#':
                return True
        # vertical check
        for i in range(0, 3, 1):
            if self._state[i] == self._state[i+3] == self._state[i+6] and self._state[i] != '#':
                return True
        # diagonal check
        if self._state[0] == self._state[4] == self._state[8] and self._state[0] != '#':
            return True
        if self._state[2] == self._state[4] == self._state[6] and self._state[2] != '#':
            return True
        return False
