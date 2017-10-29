# inheritance : class Parent is being inherited by class Child
class Parent():
	def print_lastname(self):
		print ("agrawal")

class Child(Parent):
	def print_firstname(self):
		print("charul")
class Uncle(Parent):
	def print_lastname(self):
		print("sharma")
object=Child()
object.print_firstname()
object.print_lastname()
object2=Uncle()
object2.print_lastname()

