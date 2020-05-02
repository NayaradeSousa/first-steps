"""
It is a game of only two players where:
The board is an array of three rows by three columns.
     |   |
 ---+---+---
    |   |
 ---+---+---
    |   |
Two players choose a mark each, usually a circle (O) and a cross (X).
Players play alternately, one check at a time, in a gap that is empty.
The aim is to get three circles or three crosses in a row, either horizontally, vertically or diagonally,
and at the same time, when possible, prevent the opponent from winning on the next move.
When a player achieves the goal, it is customary to cross out the three symbols.
"""
# O tabuleiro
velha = """               Positions
   |   |      7 | 8 | 9
---+---+---  ---+---+---
   |   |      4 | 5 | 6
---+---+---  ---+---+---
   |   |      1 | 2 | 3
"""

positions = [
    None,  # Add to facilitate indexes
    (5, 1),
    (5, 5),
    (5, 9),
    (3, 1),
    (3, 5),
    (3, 9),
    (1, 1),
    (1, 5),
    (1, 9),
]

win = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
    [7, 5, 3],
    [1, 5, 9]
]

board = []
for line in velha.splitlines():
    board.append(list(line))

player = "X"
playing = True
moves = 0
while True:
    for t in board:
        print("".join(t))
    if not playing:
        break
    if moves == 9:
        print("Nobody won.")
        break
    move = int(input("Enter 1-9 position to play (player %s):" % player))
    if move < 1 or move > 9:
        print("Invalid position.")
        continue
    # Checks whether the position is free
    if board[positions[move][0]][positions[move][1]] != " ":
        print("Occupied position.")
        continue
    # Marks the move for the player
    board[positions[move][0]][positions[move][1]] = player
    # Check if there was won
    for p in win:
        for x in p:
            if board[positions[x][0]][positions[x][1]] != player:
                break
        else:
            print("Player %s won (%s): " % (player, p))
            playing = False
            break
    player = "X" if player == "O" else "O"
    moves += 1
