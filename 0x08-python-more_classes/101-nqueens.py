#!/usr/bin/python3


def print_NQueen(square_y, N):
    """Create a the format and print the result
    result = possible variant of the queen position
    in the chess game"""
    result = []
    i = 0
    for a in square_y:
        new = []
        new.append(i)
        new.append(a)
        result.append(new)
        i = i + 1
    print(result)


def check_move(pos_x, square_y):
    """Check if the square it is available to move or not
        we check the position between one queen and the
        posible position of the new queen"""
    for i in range(pos_x):
        if square_y[i] == square_y[pos_x]:
            return False
        if pos_x - i == abs(square_y[pos_x] - square_y[i]):
            return False
    return True


def solve_NQueen(N, pos_x, square_y):
    """Backtracking function:
    - N: Size of chessboard
    - pos_x: actual position
    - square_x: list of solutions to move the queen"""
    if (pos_x == N):
        print_NQueen(square_y, N)
    else:
        for i in range(N):
            square_y.append(i)
            if (check_move(pos_x, square_y)):
                solve_NQueen(N, pos_x + 1, square_y)
            square_y.pop(-1)

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]

    try:
        N = int(N)
    except:
        print("N must be a number")
        exit(1)

    if (N < 4):
        print("N must be at least 4")
        sys.exit(1)

    # initialize chess game
    square_y = []
    pos_x = 0
    solve_NQueen(N, pos_x, square_y)
