game = [[1,1,1],
		[2,1,0],
		[2,2,2],
		[5,6,8],]
def win(current_game):
	for row in game:
		print(row)

		# solution 3
		if row.count(row[0]) == len(row):
			print("Winner")

		# Solution 2

		# all_match = True
		# for item in row:
		# 	if item != row[0]:
		# 		all_match = False 
		# if all_match:
		# 	print("winner")		

		# solution 1 
		# col1 = row[0]
		# col2 = row[1]
		# col3 = row[2]

		# if col1 == col2 == col3:
		# 	print("winner")



win(game)			