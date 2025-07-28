#!/usr/bin/env python3
"""
Tic‑Tac‑Toe: human (X) vs computer (O)
"""
import random
from typing import List

Board = List[str]


def print_board(brd: Board) -> None:
    """Display board nicely."""
    # TODO: implement


def winner(brd: Board) -> str | None:
    """Return 'X', 'O', 'draw', or None."""
    # TODO: implement


def human_turn(brd: Board) -> None:
    """Ask user for move (1‑9)."""
    # TODO: implement


def computer_turn(brd: Board) -> None:
    """Randomly choose an empty cell and mark 'O'."""
    # TODO: implement


def play() -> None:
    board: Board = [" "] * 9
    turn = "X"
    while True:
        print_board(board)
        if turn == "X":
            human_turn(board)
        else:
            computer_turn(board)
        win = winner(board)
        if win:
            print_board(board)
            print("Result:", "Draw" if win == "draw" else f"{win} wins!")
            break
        turn = "O" if turn == "X" else "X"


if __name__ == "__main__":
    play()
