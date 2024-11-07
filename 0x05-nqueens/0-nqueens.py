#!/usr/bin/python3
import sys

"""
N queens puzzle challenge
"""

def print_board(board):
    """Function to print the solution in the required format."""
    print(board)

def is_valid(board, row, col):
    """Check if placing a queen at (row, col) is valid."""
    for i in range(row):
        if board[i][1] == col or \
           board[i][1] - i == col - row or \
           board[i][1] + i == col + row:
            return False
    return True

def solve_nqueens(N, row, board):
    """Backtracking algorithm to solve N Queens problem."""
    if row == N:
        print_board(board)
        return
    for col in range(N):
        if is_valid(board, row, col):
            board.append([row, col])
            solve_nqueens(N, row + 1, board)
            board.pop()

def main():
    """Main function to handle input and solve the N Queens problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N queens problem starting from row 0
    solve_nqueens(N, 0, [])

if __name__ == "__main__":
    main()
