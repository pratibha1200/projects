game = [[1,1,4],
		[1,1,0],
		[0,1,2],]
for col in range(len(game)):
	check= []
	for row in game:
		check.append(row[col])

	if check.count(check[0]) == len(check):
		print("winner")
