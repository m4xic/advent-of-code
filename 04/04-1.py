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
        if callout == callouts[-1]:
            print(f"{boards=}")
            sys.exit(1)
        print(f"{callout=}")
        for board_id in range(0, len(boards)):
            for row_id in range(0, len(boards[board_id])):
                for column_id in range(0, len(boards[board_id][row_id])):
                    if boards[board_id][row_id][column_id] == callout:
                        boards[board_id][row_id][column_id] = 'x'
    
        # Check for a win after every callout
        for board_id in range(0, len(boards)):
            # Check for row wins
            for row_id in range(0, len(boards[board_id])):
                if boards[board_id][row_id] == ['x', 'x', 'x', 'x', 'x']:
                    print(f"ROW WINNER!! {board_id=} {callout=} {boards[board_id]=}")
                    #sys.exit(1)
            # Check horiz wins
            for column in range(0, len(boards[board_id][0])):
                if boards[board_id][0][column] == 'x' and boards[board_id][1][column] == 'x' and boards[board_id][2][column] == 'x' and boards[board_id][3][column] == 'x' and boards[board_id][4][column] == 'x':
                    print(f"COL WINNER!! {board_id=} {callout=} {boards[board_id]=}")
                    #sys.exit(1)
    print(f"{boards}")
    break