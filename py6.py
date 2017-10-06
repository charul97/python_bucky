while True:
	try:
		num=int(input("enter a number\n"))
		print(10//num)
		break
	except NameError:
		print("enter a valid no")
	except ZeroDivisionError:
		print("dont enter zero")
	except:
		break
	finally:
		print("exited from the loop")
