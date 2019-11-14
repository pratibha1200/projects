game = [[1,1,1],
		[1,1,0],
		[1,1,0],]
# Manually 

# if game[0][0] == game[1][1] == game[2][2]:
# 	print("Winner")
# if game[2][0] == game[1][1] == game[0][2]:
# 	print("Winner")			


diags = []
for ix in range(len(game)):
	diags.append(game[ix][ix])

diags = []
for row,col in enumerate(reversed(range(len(game)))):
	diags.append(game[row][col])
