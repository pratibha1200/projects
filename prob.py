# def missing(A):
# 	n = len(A)
# 	total = (n+1)*(n+2)/2
# 	sum_A = sum(A)
# 	return total-sum_A

# A = [1,2,4,5,6]
# print(missing(A))
# 	
# def rotate(arr,n):
# 	x = arr[n-1]
# 	for i in range(n-1,0,-1):
# 		arr[i] = arr[i-1]

# 	arr[0] = x
		
# arr = [1,2,4,5,6]
# n = len(arr)
# rotate(arr,n)
# for i in range(0,n):
# 	print(arr[i],end = " ")
# print()	

import datetime
print (datetime.date.today().strftime("%a %d %b %Y"))
