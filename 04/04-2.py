def check_win(board):
    # Check vert wins
    for row_id in range(0, len(board)):
        if board[row_id] == ['x', 'x', 'x', 'x', 'x']:
            return True
    # Check horiz wins
    for column in range(0, len(board[0])):
        if board[0][column] == 'x' and board[1][column] == 'x' and board[2][column] == 'x' and board[3][column] == 'x' and board[4][column] == 'x':
            return True
    return False

import sys

with open('04-callouts', 'r') as f: callouts = f.read().split(',')
with open('04-boards', 'r') as f: raw_boards = f.read().splitlines()
#print(callouts)
#print(raw_boards)

# Import boards
boards = []
for i in range((len(raw_boards) + 1) // 6):
    board = []
    for j in range(0, 5): board.append(raw_boards[(i * 6) + j].split())
    boards.append(board)

while True:
    # For each callout in the bingo numbers...
    for callout in callouts:
        print(f"\n{len(boards)=}")
        if callout == callouts[-1]:
            print(f"{boards=}")
            sys.exit(1)
        print(f"{callout=}")
        for board_id in range(0, len(boards)):
            for row_id in range(0, len(boards[board_id])):
                for column_id in range(0, len(boards[board_id][row_id])):
                    if boards[board_id][row_id][column_id] == callout:
                        boards[board_id][row_id][column_id] = 'x'
    
        check_board, orig_board = 0, 0
        while check_board < len(boards):
            if check_win(boards[check_board]):
                print(f"*** Board {orig_board+1} won! {len(boards)-1} remain{'s' if len(boards) == 2 else ''}.")
                print(f"Final state of board: {boards[check_board]}")
                del(boards[check_board])
                check_board -= 1
                
            check_board += 1
            orig_board += 1