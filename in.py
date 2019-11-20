class Players():
	def players(self,name,match,run,odi):
		cdict = {}
		cdict['name']= name
		cdict['match'] = match
		cdict['run'] = run
		cdict['odi'] = odi

		return cdict

N = int(input('Enter players: '))
list1 = []
if N != 0:
	name = input('Enter player name: ')
	match = int(input('Enter No. of Matches: '))
	run = int(input('Enter no. of Runs: '))
	odi = int(input('Enter no. of Odi: '))

	obj1 = Players()
	cdict = obj1.players(name,match,run,odi)
	list1.append(cdict)
	N -=1

print(list1)	

