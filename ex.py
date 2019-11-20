class NewStack():
	def __init__(self):
		self.stack = []

	def Empty(self):
		return self.stack == []

	def push(self,item):
		return self.stack.append(item)	

	def pop(self):
		return self.stack.pop()

	def display(self):
		return self.stack	

	def length(self):
		return len(self.stack)	

	

s = NewStack()
print(s.Empty())
print(s.display())
s.push('hello')
s.push('world')
s.push('96')
s.push('52')
print(s.display())
print(s.pop())	
print(s.display())		
print(s.length())	