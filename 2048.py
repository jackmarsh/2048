import random

def create_board(board):
	while True:
		x1 = random.randint(0,3)
		y1 = random.randint(0,3)
		x2 = random.randint(0,3)
		y2 = random.randint(0,3)   
		if [x1, y1] != [x2, y2]:
			board[x1][y1] = 2
			board[x2][y2] = 2
			return board

def display(board):
	for row in board:
		print row

def find(board):
	# find values and return list of where they are
	a_s = []
	for x in range(len(board)):
		for y in range(len(board[x])):
			if board[x][y] > 0:
				a_s.append([x,y,board[x][y]])
	return a_s

def new(board):
	while True:
		outside = [0,3]
		x = random.randint(0,3)
		y = random.randint(0,3)
		if x == 0 or x == 3 or y == 0 or y == 3:
			if board[x][y] == 0:
				board[x][y] = 2
				return board

def move(board):
	# check move is valid
	while True:
		move = str(raw_input("move: "))
		if move in ["w","a","s","d"]:
			break

	# move on board
	a_s = find(board)
	if move == "w":
		for i in a_s:
			while i[0] > 0:
				if board[i[0]-1][i[1]] == 0:
					board[i[0]-1][i[1]] = i[2]
					board[i[0]][i[1]] = 0
					i[0] -= 1
				elif board[i[0]-1][i[1]] == i[2]:
					board[i[0]-1][i[1]] = i[2]*2
					board[i[0]][i[1]] = 0
					i[0] -= 1
				else:
					break
	elif move == "a":
		for i in a_s:
			while i[1] > 0:
				if board[i[0]][i[1]-1] == 0:
					board[i[0]][i[1]-1] = i[2]
					board[i[0]][i[1]] = 0
					i[1] -= 1
				elif board[i[0]][i[1]-1] == i[2]:
					board[i[0]][i[1]-1] = i[2]*2
					board[i[0]][i[1]] = 0
					i[1] -= 1
				else:
					break
	elif move == "s":
		for i in a_s:
			while i[0] < 3:
				if board[i[0]+1][i[1]] == 0:
					board[i[0]+1][i[1]] = i[2]
					board[i[0]][i[1]] = 0
					i[0] += 1
				elif board[i[0]+1][i[1]] == i[2]:
					board[i[0]+1][i[1]] = i[2]*2
					board[i[0]][i[1]] = 0
					i[0] += 1
				else:
					break
	elif move == "d":
		for i in a_s:
			while i[1] < 3:
				if board[i[0]][i[1]+1] == 0:
					board[i[0]][i[1]+1] = i[2]
					board[i[0]][i[1]] = 0
					i[1] += 1
				elif board[i[0]][i[1]+1] == i[2]:
					board[i[0]][i[1]+1] = i[2]*2
					board[i[0]][i[1]] = 0
					i[1] += 1
				else:
					break
	new(board)
	return board


def update_board(board):
	display(board)
	for row in board:
		if 2048 in row:
			return 1
	update_board(move(board))



board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
board = create_board(board)
display(board)
update_board(move(board))
