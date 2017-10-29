# __init__ function   : whenever this function is present in any class, then the# object of that class first looks for this function and executes it and then go# es to other functions of the class 

class abc:
	def f1(self):
		print('this is function 1')
	def __init__(self):
		print('hi guys')

obj= abc()
obj.f1()
