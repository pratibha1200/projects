n = int(input("start: "))
m = int(input("end: "))
even = []
odd = []
for num in range(n,m+1):
	if num % 2 == 0:
		even.append(num)
	else:
		odd.append(num)
output = {"even": even,"odd": odd}
print(output)