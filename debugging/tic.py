#!/usr/bin/python3
def print_board(board):
	print('  ' + ' '.join(f'{i:3}' for i in range(3)))
	for y in range(3):
		print(f'{y:3}' + ' | '.join(f'{board[y][x]:3}' for x in range(3)))
		if y < 2:
			print('    ' + ' '.join('___' for _ in range(3)))

def check_winner(board):
	for row in board:
		if row.count(row[0]) == len(row) and row[0] != " ":
			return True
	for col in range(len(board[0])):
		if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
			return True
	if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
		return True
	if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
		return True
	return False

def tic_tac_toe():
	board = [[" "]*3 for _ in range(3)]
	player = "X"
	moves = 0
	max_moves = 9

	while not check_winner(board) and moves < max_moves:
		print_board(board)
		try:
			row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
			col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

			if row not in range(3) or col not in range(3):
				print("Invalid input. Please enter row and column between 0 and 2.")
				continue

			if board[row][col] == " ":
				board[row][col] = player
				moves += 1
				if check_winner(board):
					print_board(board)
					print(f"Player {player} wins!")
					return
				player = "O" if player == "X" else "X"
			else:
				print("That spot is already taken! Try again.")
		except ValueError:
			print("Invalid input. Please enter numbers only.")

	print_board(board)
	print("It's a draw!")

if __name__ == "__main__":
	tic_tac_toe()
