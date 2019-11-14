import itertools	
# game = [[1,5,1],
# 		[1,0,0],
# 		[1,0,2],]
def win(current_game):

	def all_same(l):
		if l.count(l[0]) == len(l) and l[0] != 0:
			return True 
		else:
			return False


	# Horizontal
	for row in game:
		print(row)
		if all_same(row):
			print(f"Player {row[0]} is the winner horizontally")
			return True 

	# Diagonal 		
	diags = []
	for ix in range(len(game)):
		diags.append(game[ix][ix])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner diagonally (\\)")
		return True 

	diags = []
	for row,col in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner diagonally (/)")	
		return True 

	# Vertical	
	for col in range(len(game)):
		check= []
		for row in game:
			check.append(row[col])

		if all_same(check):
			print(f"Player {check[0]} is the winner Vertically ")	
			return True 
	return False		


def game_board(game_map,player = 0,row = 0	,column=0, just_display = False):
	try:
		if game_map[row][column] != 0:
			print("this position is occupied choose another")
			return game_map,False
		# print("   0, 1, 2")
		print("   "+"  ".join([str(i) for i in range(len(game_map))]))
		if not just_display:
			game_map[row][column] = player
		for count,row in enumerate(game_map):
			print(count,row)
		return game_map	, True 
	except IndexError as e :
		print("Error: make sure you are using  or 2 as col/row ",e)
		return game_map,False	
	except Exception as e:
		print("Something went wrong ",e)
		return game_map,False

play = True 
players = [1,2]
while play:	
	# game = [[0,0,0],
	# 		[0,0,0],
	# 		[0,0,0],]	
	game_size = int(input("what size game of tic tac toe? "))
	game = [[0 for i in range (game_size)] for i in range (game_size)]
	game_won = False
	game , _ = game_board(game,just_display = True)
	player_choice = itertools.cycle([1,2])	
	while not game_won:
		current_player = next(player_choice)
		print(f"current player:{ current_player}")
		played = False 

		while not played:
			column_choice = int(input("what column do u want to play? (0, 1, 2)"))
			row_choice = int(input("what row do u want to play? (0, 1, 2)"))
			game,played  = game_board(game,current_player,row_choice,column_choice)	

		if win(game):
			game_won = True
			again= input("the game is over, do you want to play again? (y/n) ")
			if again.lower() == "y":
				print("restarting")
			elif again.lower() == "n":
				print("Byeeeeeee")
				play = False		
			else: 
				print("not a valid answer,")
				play = False	

# game_board(game,just_display = True)			
# game_board(game_board,player = 1, row = 3,column= 1)			
win(game)

