"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any, Union
from copy import deepcopy


# TODO: Adjust the type annotation as needed.
def interactive_strategy(game: "Game") -> Union[int, str]:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: "Game") -> Union[int, str]:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


def recursive_minimax_strategy(game: "Game") -> Union[int, str]:
    """
    Return a move for... COMPLETE THIS
    """
    best_move = None
    best_outcome = -2
    old_state = deepcopy(game.current_state)
    moves = old_state.get_possible_moves()
    for move in moves:
        new_state = deepcopy(old_state.make_move(move))
        guessed_score = -1 * recursive_helper(game, new_state)
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move
    game.current_state = old_state
    return best_move

def recursive_helper(game: "Game", game_state: "GameState") -> int:
    """
    Does the recursive work for recursive_minimax_strategy
    """
    if game.is_over(game_state):
        return game_state.rough_outcome()


    return max([recursive_helper(game, game_state.make_move(move)) * -1
                for move in game_state.get_possible_moves()])


def iterative_minimax_strategy(game: "Game") -> Union[int, str]:
    """Strategy"""
    best_move = None
    best_outcome = -2
    old_state = game.current_state
    moves = old_state.get_possible_moves()
    for move in moves:
        guessed_score = -1 * \
                        iterative_helper(game.current_state.make_move(move))
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move
    game.current_state = old_state
    return best_move


def iterative_helper(game_state: "GameState") -> int:
    """Helper for iterative strategy."""
    stack = Stack()
    first_node = Node()
    first_node.id = 0
    index = 0
    first_node.state = game_state
    first_node.children = []
    first_node.score = None
    stack.add(first_node)
    place = []
    place_last_index = -1
    while not stack.is_empty():
        current_item = stack.remove()
        if current_item.state.get_possible_moves() == []:
            current_item.score = -1
            place.append(current_item)
            place_last_index += 1
        else:
            if current_item.children == []:
                states_list = []
                nodes_list = []
                for move in current_item.state.get_possible_moves():
                    states_list.append(current_item.state.make_move(move))
                for state in states_list:
                    node = Node()
                    node.id = index + 1
                    index += 1
                    node.state = state
                    node.children = []
                    node.score = None
                    nodes_list.append(node)
                for node_index in nodes_list:
                    current_item.children.append(node_index.id)
                stack.add(current_item)
                for node_index in nodes_list:
                    stack.add(node_index)
            else:
                scores_list = []
                for item in place:
                    if item.id in current_item.children:
                        scores_list.append(-1 * item.score)
                current_item.score = max(scores_list)
                place.append(current_item)
                place_last_index += 1
    return place[place_last_index].score


class Node:
    """A class to wrap the state. """
    def __init__(self):
        self.id: int
        self.state: Any
        self.children: list
        self.score: int

class Stack:
    """ Last-in, first-out (LIFO) stack.

    TAKEN FROM CLASS.
    """

    def __init__(self) -> None:
        """ Create a new, empty Stack self.

        >>> s = Stack()
        """
        self._contains = []

    def add(self, obj: object) -> None:
        """ Add object obj to top of Stack self.

        >>> s = Stack()
        >>> s.add(5)
        """
        self._contains.append(obj)

    def remove(self) -> object:
        """
        Remove and return top element of Stack self.

        Assume Stack self is not emp.

        >>> s = Stack()
        >>> s.add(5)
        >>> s.add(7)
        >>> s.remove()
        7
        """
        return self._contains.pop()

    def is_empty(self) -> bool:
        """
        Return whether Stack self is empty.

        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.add(5)
        >>> s.is_empty()
        False
        """
        return len(self._contains) == 0
if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="/Users/roshankr/Documents/csc148/a2/a2_pyta")
