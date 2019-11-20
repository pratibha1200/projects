class first():
	def sum1(self,a,b):
		c = a+b
		return c
class second():
	def sub(self,x,y):
		z = x-y
		return z
class third(first,second):
	pass

obj1 = third()
print(obj1.sum1(5,6))
print(obj1.sub(89,25))
