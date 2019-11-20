def calculation():
	print("=================CALCULATOR=================")
	x = int(input('Enter first value: '))
	y = int(input('Enter second value: '))
	print('Press 1 for Addition(+)\n Press 2 for Subtrction(-)\n Press 3 for multiplication(*)\n Press 4 for Division(/)')
	option = int(input("==> "))
	def add():
		res = x+y
		print(res)

	def sub():
		res = x-y	
		print(res)

	def mul():
		res = x*y
		print(res)

	def dev():
		res = x/y
		print(res)

	
	if(option == 1):
		add()
	elif(option == 2):
		sub()
	elif(option == 3):
		mul()
	elif(option == 4):
		dev()
calculation()			


