import time
import random
import threading

def print_board(board):
    for row in board:
        print(' '.join(row))
    print('\n' + '='*20 + '\n')

def next_generation(board):
    new_board = [row[:] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            total = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    if 0 <= i + x < len(board) and 0 <= j + y < len(board[i]):
                        total += board[i + x][j + y] == '#'
            if board[i][j] == '#':
                if total < 2 or total > 3:
                    new_board[i][j] = ' '
            elif board[i][j] == ' ':
                if total == 3:
                    new_board[i][j] = '#'
    return new_board

def main():
    board_size = 10
    board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
    for i in range(board_size):
        for j in range(board_size):
            board[i][j] = '#' if random.random() > 0.7 else ' '

    def change_board_size():
        nonlocal board_size, board
        while True:
            try:
                new_size = int(input("Enter new board size (or 0 to exit): "))
                if new_size == 0:
                    print("Exiting...")
                    return
                board_size = new_size
                board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
                for i in range(board_size):
                    for j in range(board_size):
                        board[i][j] = '#' if random.random() > 0.7 else ' '
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    size_change_thread = threading.Thread(target=change_board_size, daemon=True)
    size_change_thread.start()

    while size_change_thread.is_alive():
        print_board(board)
        board = next_generation(board)
        time.sleep(1)

if __name__ == "__main__":
    main()


#Fix Bugs