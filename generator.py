# def updown(N):
# 	for x in range(1,N):
# 		yield x
# 	for x in range(N,0,-1):
# 		yield x	
# for i in updown(3):
# 	print(i)

# def cube(y): 
#     return y*y*y; 
  
# g = lambda x: x*x*x 
# print(g(7)) 
  
# print(cube(5)) 

class MyClass:
    i = 12345

    def f(self):
        return 'hello world'

print(MyClass.f)      