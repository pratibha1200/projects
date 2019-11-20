n = 3
d = dict(input().split() for i in range(n))
print (d)

d1 = dict(input().split() for i in range(n))
print(d1)

d2 = dict(input().split() for i in range(n))
print(d2)

list1 = [v for v in d.values()] 
print(list1)

list2 = [v for v in d1.values()]
print(list2)

list3 = [v for v in d2.values()]
print(list3)	

# list4 = list1 + list2 + list3 
from tabulate import tabulate
print(tabulate([list1,list2,list3], headers=['Name', 'Match','Run']))