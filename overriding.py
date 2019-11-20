class first():
	def m(self):
		print('m1 is called')
class second(first):
	def m(self):
		print("m2 is called")

secondobj = second()
secondobj.m()
secondobj = first()
secondobj.m()



