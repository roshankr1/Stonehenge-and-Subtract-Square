"""Solution for stonehenge"""
from typing import Any
from game import Game
from game_state import GameState
from copy import deepcopy


ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def board_generator(side_length: int) -> str:
    """To generate boards."""
    u_count = 1
    s_count = 1
    d_count = 1
    a = 0
    rowed = " - "
    very_first = (4 * ' ') + (2 * side_length * ' ')
    for i in range(2):
        very_first += '3' + str(u_count)
        u_count += 1
        if not i == 1:
            very_first += 3 * ' '
    very_first += ' \n'
    very_second = (3 * ' ') + (2 * side_length * ' ')
    for i in range(2):
        very_second += '/'
        if not i == 1:
            very_second += 3 * ' '
    very_second += ' \n'
    middle = ''
    for i in range(2, side_length + 1):
        each = 2 * ' ' * (side_length + 1 - i)
        each += '5' + str(s_count) + rowed
        s_count += 1
        for j in range(i):
            each += ALPHA[a]
            a += 1
            if not j == i - 1:
                each += rowed
            if j == i - 1:
                each += 3 * " " + '3' + str(u_count)
                u_count += 1
        each += '\n'
        down_each = ''
        if not i == side_length:
            down_each = 2 * ' ' * (side_length + 1 - i) + 3 * ' '
            for j in range(i):
                down_each += '/' + ' '
                if not j == i - 1:
                    down_each += '\\' + ' '
            down_each += '\\' + ' ' + '/'
            down_each += ' \n'
        middle += each + down_each
    major_line = '5' + str(s_count) + rowed
    s_count += 1
    for i in range(side_length + 1):
        major_line += ALPHA[a]
        a += 1
        if not i == side_length:
            major_line += rowed
    major_line += ' \n'
    up_major_line = 5 * ' '
    for i in range(side_length + 1):
        if not i == 0:
            up_major_line += "\\" + " "
        up_major_line += '/' + " "
    up_major_line += ' \n'
    if side_length == 1:
        up_major_line = ''
    down_major_line = 5 * ' '
    for i in range(side_length + 1):
        if not i == 0:
            down_major_line += '/' + ' '
        down_major_line += '\\' + ' '
    down_major_line += ' \n'
    major = up_major_line + major_line + down_major_line
    last_line = 2 * ' ' + '5' + str(s_count) + rowed
    s_count += 1
    for i in range(side_length):
        last_line += ALPHA[a]
        a += 1
        if not i == side_length - 1:
            last_line += rowed
        if i == side_length - 1:
            last_line += 3 * ' ' + '4' + str(d_count)
            d_count += 1
    last_line += ' \n'
    down_last_line = 7 * " "
    for i in range(side_length):
        down_last_line += '\\'
        if not i == side_length - 1:
            down_last_line += 3 * ' '
    down_last_line += ' \n'
    very_last = 8 * ' '
    for i in range(side_length):
        very_last += '4' + str(d_count)
        d_count += 1
        if not i == side_length - 1:
            very_last += 3 * ' '
    major += last_line + down_last_line + very_last
    return very_first + very_second + middle + major + '    '


class StonehengeGame(Game):
    """Abstract class of a game to be played with two players called
    Stonehenge"""
    def __init__(self, p1_starts):
        """
        Initialize this Game, using p1_starts to find who the first player is.
        """
        side_length = int(input("Enter the side length of the board: "))
        start_board = board_generator(side_length)
        cell_list = []
        for letter in start_board:
            if letter.isalpha():
                cell_list.append(letter)
        rows = []
        start = 0
        count = 2
        while count <= side_length + 1:
            rows.append(cell_list[start:start + count])
            start = start + count
            count = count + 1
        rows.append(cell_list[len(cell_list) - side_length:])
        row_ley_lines = {}
        up_ley_lines = {}
        down_ley_lines = {}
        if side_length == 1:
            row_ley_lines = [[51, ['A', 'B']], [52, ['C']]]
            up_ley_lines = [[31, ['A']], [32, ['B', 'C']]]
            down_ley_lines = [[41, ['B']], [42, ['A', 'C']]]
        if side_length == 2:
            row_ley_lines = [[51, ['A', 'B']], [52, ['C', 'D', 'E']],
                             [53, ['F', 'G']]]
            up_ley_lines = [[31, ['A', 'C']], [32, ['B', 'D', 'F']],
                            [33, ['E', 'G']]]
            down_ley_lines = [[41, ['B', 'E']], [43, ['A', 'D', 'G']],
                              [42, ['C', 'F']]]
        if side_length == 3:
            row_ley_lines = [[51, ['A', 'B']], [52, ['C', 'D', 'E']],
                             [53, ['F', 'G', 'H', 'I']], [54, ['J', 'K', 'L']]]
            up_ley_lines = [[31, ['A', 'C', 'F']], [32, ['B', 'D', 'G', 'J']],
                            [33, ['E', 'H', 'K']], [34, ['I', 'L']]]
            down_ley_lines = [[41, ['B', 'E', 'I']], [43, ['C', 'G', 'K']],
                              [42, ['J', 'F']], [44, ['A', 'D', 'H', 'L']]]
        if side_length == 4:
            row_ley_lines = [[51, ['A', 'B']], [52, ['C', 'D', 'E']],
                             [53, ['F', 'G', 'H', 'I']],
                             [54, ['J', 'K', 'L', 'M', 'N']],
                             [55, ['O', 'P', 'Q', 'R']]]
            up_ley_lines = [[31, ['A', 'C', 'F', 'J']],
                            [32, ['B', 'D', 'G', 'K', 'O']],
                            [33, ['E', 'H', 'L', 'P']], [34, ['I', 'M', 'Q']],
                            [35, ['N', 'R']]]
            down_ley_lines = [[41, ['B', 'E', 'I', 'N']], [43, ['F', 'P', 'K']],
                              [42, ['J', 'O']], [44, ['C', 'G', 'Q', 'L']],
                              [45, ['A', 'D', 'H', 'M', 'R']]]
        if side_length == 5:
            row_ley_lines = [[51, ['A', 'B']], [52, ['C', 'D', 'E']],
                             [53, ['F', 'G', 'H', 'I']],
                             [54, ['J', 'K', 'L', 'M', 'N']],
                             [55, ['O', 'P', 'Q', 'R', 'S', 'T']],
                             [56, ['U', 'V', 'W', 'X', 'Y']]]
            up_ley_lines = [[31, ['A', 'C', 'F', 'J', 'O']],
                            [32, ['B', 'D', 'G', 'K', 'P', 'U']],
                            [33, ['E', 'H', 'L', 'Q', 'V']],
                            [34, ['I', 'M', 'R', 'W']],
                            [35, ['N', 'S', 'X']], [36, ['T', 'Y']]]
            down_ley_lines = [[41, ['B', 'E', 'I', 'N', 'T']],
                              [43, ['J', 'P', 'V']],
                              [42, ['U', 'O']], [44, ['F', 'K', 'Q', 'W']],
                              [45, ['C', 'G', 'L', 'X', 'R']],
                              [46, ['A', 'D', 'H', 'M', 'S', 'Y']]]
        ley_lines = [row_ley_lines, up_ley_lines, down_ley_lines]

        self.current_state = StonehengeState(p1_starts, side_length,
                                             start_board, ley_lines)


    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.
        """
        instructions = "Players take turns to occupy available positions " \
                       "on the " \
                       "board. Once half or more of a ley-line has been " \
                       "occupied" \
                       "one player, that ley-line is entirely captured by " \
                       "said player. The winner is the person who captures " \
                       "half" \
                       "or more of the ley-lines first."
        return instructions

    def is_over(self, state) -> bool:
        """
        Return whether the game is over.
        """

        p1_count = 0
        p2_count = 0
        ley_line_total = (state.side_length + 1) * 3
        for itype in state.current_ley_lines:
            for line in itype:
                if line[0] == '1':
                    p1_count += 1
                if line[0] == '2':
                    p2_count += 1

        if p1_count >= ley_line_total/2 or p2_count >= ley_line_total/2:
            return True
        return False





    def is_winner(self, player) -> bool:
        """
        Return whether player is the winner of the game.
        """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string):
        """
        Return the move that string represents. If string is not a move,
        return an invalid move.
        """
        if not string.strip().isalpha():
            return -1
        return string.strip()

class StonehengeState(GameState):
    """
    The state of a game at a certain point in time.
    """
    def __init__(self, is_p1_turn: bool, side_length: int, current_board: str,
                 current_ley_lines: list):
        """
        Initialize this GameState, using is_p1_turn to find who the
        current player is.
        """
        super().__init__(is_p1_turn)
        self.current_board = current_board
        self.current_ley_lines = current_ley_lines
        self.side_length = side_length


    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        not_actual = self.current_board
        representation = self.current_board

        for index in range(len(not_actual)):
            if not_actual[index: index + 2] in ['31', '32', '33', '34', '36',
                                                '37', '38']:
                representation = representation.replace(
                    not_actual[index: index + 2], '@')
            if not_actual[index: index + 2] in ['41', '42', '43', '44', '45',
                                                '46', '47', '48']:
                representation = representation.replace(
                    not_actual[index: index + 2], '@')
            if not_actual[index: index + 2] in ['51', '52', '53', '54', '55',
                                                '56', '57', '58']:
                representation = representation.replace(
                    not_actual[index: index + 2], '@')
        return representation



    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        """
        p1_count = 0
        p2_count = 0
        ley_line_total = (self.side_length + 1) * 3
        for itype in self.current_ley_lines:
            for line in itype:
                if line[0] == '1':
                    p1_count += 1
                if line[0] == '2':
                    p2_count += 1
        if p1_count >= ley_line_total / 2 or p2_count >= ley_line_total / 2:
            return []
        moves = []
        for letter in self.current_board:
            if letter.isalpha():
                moves.append(letter)
        return moves

    def make_move(self, move: Any) -> "StonehengeState":
        """
        Return the GameState that results from applying move to this GameState.
        """
        new_board = deepcopy(self.current_board)
        for index in range(len(self.current_board)):
            if self.current_board[index] == move:
                if self.p1_turn:
                    new_board = new_board.replace(
                        self.current_board[index], '1')
                else:
                    new_board = new_board.replace(
                        self.current_board[index], '2')
        new_ley_lines = deepcopy(self.current_ley_lines)
        for item in new_ley_lines:
            for key in item:
                for index in range(len(key[1])):
                    if key[1][index] == move:
                        if self.p1_turn:
                            key[1][index] = '1'
                        else:
                            key[1][index] = '2'
        change_dict = {}
        for item in new_ley_lines:
            for key in item:
                p1_count = 0
                p2_count = 0
                for string in key[1]:
                    if string == '1':
                        p1_count += 1
                    if string == '2':
                        p2_count += 1


                if p1_count >= len(key[1])/2 and p1_count > p2_count:

                    change_dict[key[0]] = '1'
                if p2_count >= len(key[1])/2 and p2_count > p1_count:

                    change_dict[key[0]] = '2'
        for key in change_dict:
            if not (key == '1' or key == '2'):
                if str(key) in new_board:
                    new_board = new_board.replace(str(key), change_dict[key])
                for item in new_ley_lines:
                    for key1 in item:
                        if key == key1[0]:
                            key1[0] = change_dict[key]

        new_state = StonehengeState(not self.p1_turn, self.side_length,
                                    new_board, new_ley_lines)
        return new_state

    def __repr__(self) -> str:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        return "P1's Turn: {} - Board: {}".format(self.p1_turn,
                                                  self.current_board)
    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        if is_win(self):
            return 1
        elif is_lose(self):
            return -1
        return 0


    def finished(self) -> bool:
        """
        To check is game is over.
        """
        p1_count = 0
        p2_count = 0
        ley_line_total = (self.side_length + 1) * 3
        for itype in self.current_ley_lines:
            for line in itype:
                if line[0] == '1':
                    p1_count += 1
                if line[0] == '2':
                    p2_count += 1
        return p1_count >= ley_line_total / 2 or p2_count >= ley_line_total / 2

def is_win(state: StonehengeState) -> bool:
    """
    To check if it is a win.
    """
    moves = []
    for move in state.get_possible_moves():
        new_state = deepcopy(state.make_move(move))
        moves.append(new_state.finished())
    return any(moves)

def is_lose(state: StonehengeState) -> bool:
    """
    To check is it is a loss.
    """
    moves = []
    for move in state.get_possible_moves():
        next_state = state.make_move(move)
        moves.append(next_state.finished())
    return any(moves)







if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="/Users/roshankr/Documents/csc148/a2/a2_pyta")
