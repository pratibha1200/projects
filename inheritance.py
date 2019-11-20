class person:
	def __init__(self,name):
		self.name = name

	def getdetails(self):
		return(self.name)

class student(person):
	def __init__(self,name,branch,address):
		person.__init__(self,name)
		self.branch = branch
		self.address = address

	def getdetails(self):
		print(self.name)
		print(self.branch)
		print(self.address)

class teacher(person):
	def __init__(self,name,fathername,add):
		person.__init__(self,name)
		self.fathername = fathername
		self.add = add

	def getdetails(self):
		print(self.name)
		print(self.fathername)
		print(self.add)


objperson = person("pratibha")
print(objperson.getdetails())
objstudent = student("divya", 'cse', 'palwal')
print(objstudent.getdetails())	
objteacher = teacher("pratibha","pramod","delhi")
print(objteacher.getdetails())
