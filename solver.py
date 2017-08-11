# Assignment 2 - Puzzle Game
#
# CSC148 Summer 2017, University of Toronto
# ---------------------------------------------
"""This module contains functions responsible for solving a puzzle.

This module can be used to take a puzzle and generate one or all
possible solutions. It can also generate hints for a puzzle (see Part 4).
"""
from puzzle import Puzzle


def solve(puzzle, verbose=False):
    """Return a solution of the puzzle.

    Even if there is only one possible solution, just return one of them.
    If there are no possible solutions, return None.

    In 'verbose' mode, print out every state explored in addition to
    the final solution. By default 'verbose' mode is disabled.

    Uses a recursive algorithm to exhaustively try all possible
    sequences of moves (using the 'extensions' method of the Puzzle
    interface) until it finds a solution.

    @type puzzle: Puzzle
    @type verbose: bool
    @rtype: Puzzle | None
    """
    all_states = []
    next_moves = puzzle.extensions()
    final = None
    for state in next_moves:
        if final:
            return final
        all_states.append(state)
        if state.is_solved():
            if verbose:
                final = all_states
                return final
            final = all_states[-1]
            return final
        else:
            final = solve(state, verbose)
    if verbose:
        for i in all_states:
            print(i)
    return final


def solve_complete(puzzle, verbose=False):

    """Return all solutions of the puzzle.

    Return an empty list if there are no possible solutions.

    In 'verbose' mode, print out every state explored in addition to
    the final solution. By default 'verbose' mode is disabled.

    Uses a recursive algorithm to exhaustively try all possible
    sequences of moves (using the 'extensions' method of the Puzzle
    interface) until it finds all solutions.

    @type puzzle: Puzzle
    @type verbose: bool
    @rtype: list[Puzzle]
    """
    solutions = []
    states = []
    puzzle_states = puzzle.extensions()
    for state in puzzle_states:
        states.append(state)
        if state.is_solved():
            solutions.append(state)
        else:
            solutions.append(solve(state, verbose))
    return solutions



if __name__ == '__main__':
    from sudoku_puzzle import SudokuPuzzle
    s = SudokuPuzzle([['', '', '', ''],
                      ['', '', '', ''],
                      ['C', 'D', 'A', 'B'],
                      ['A', 'B', 'C', 'D']])

    solution = solve(s)
    print(solution)
