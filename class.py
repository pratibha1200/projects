class Employee:

	num_of_emps = 0
	raise_amt = 1.10

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@gmail.com'

		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first,self.last)	

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
	def __init__(self,first,last,pay,prog_lang):
		super().__init__(first,last,pay)
		# Employee.__init__(self,first,last,pay)	
		self.prog_lang = prog_lang		



class Manager(Employee):
	def __init__(self,first,last,pay,employees=None):
		super().__init__(first,last,pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees	

	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)


	def print_emp(self):
		for emp in self.employees:
			print('-->',emp.fullname())								


dev_1 = Developer('mahesh','verma',50000,"python")
dev_2 = Developer('suresh','sharma',100000,"java")

mgr_1 = Manager('sue','Smith',96000,[dev_1])


print(dev_1.prog_lang)

# print(help(Developer))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

mgr_1.print_emp()
mgr_1.add_emp(dev_2)
mgr_1.print_emp()


mgr_1.remove_emp(dev_1)
mgr_1.print_emp()






	# @classmethod
	# def set_raise_amt(cls,amount):
	# 	cls.raise_amt = amount	


	# @classmethod 
	# def from_string(cls,emp_str):
	# 	first,last,pay = emp_str.split('-')	
	# 	return cls(first,last,pay)	


	# @staticmethod
	# def is_workday(day):
	# 	if day.weekday() == 5 or day.weekday() == 6:
	# 		return False
	# 	return True	

	


# emp_1 = Employee('mahesh','Kumar',80000)
# emp_2 = Employee('suresh','sharma',100000)



# emp_str_1 = 'john-die-52000'
# emp_str_2 = 'prayaik-chlo-62000'



# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.__dict__)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
# x = emp_1.fullname()
# print(x )
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_1.__dict__)

# print(Employee.num_of_emps)


# import datetime
# my_date = datetime.date(2019,11,14)

# print(Employee.is_workday(my_date))