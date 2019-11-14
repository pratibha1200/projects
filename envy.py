# def check_letter(input_string):
#     list = {}
#     for c in input_string:
#     	list[c] = input_string.count(c)
#     return list
   
def check_without(input_string):
	dicts = {}
	for word in input_string:
		if word in dicts:
			dicts[word] += 1
		else:
			dicts[word] = 1	
	return dicts




a = input("enter string: ")
print(check_without(a))