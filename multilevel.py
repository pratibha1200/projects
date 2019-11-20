class first():
	def m1(self,a,b):
		c = a+b
		return c
class second(first):
	def m2(self):
		print("m2 method is passed")

class third(second):
	def m3(self):
		print('m3 method is called ')

obj1 = third()
print(obj1.m1(5,2))				