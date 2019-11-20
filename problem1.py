from tabulate import tabulate
dictlist = []
n = int(input('Enter no. of Columns: '))
x = int(input('Enter no. of Players: '))

for d in range(x):
	d = dict(input().split() for i in range(n))
	print(d)
	dictlist.append(d)

dataset = dictlist
header = dataset[0].keys()
rows =  [x.values() for x in dataset]
print (tabulate(rows, header))







