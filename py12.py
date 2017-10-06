big_giants={
	'google': 500,
	'facebook' : 450,
	'amazon' : 400,
	'microsoft' : 470,
	'cisco' : 350,
	'uber' : 370,
}
print (min(zip(big_giants.values(),big_giants.keys())))
print (max(zip(big_giants.values(), big_giants.keys())))
print (min(zip(big_giants.keys(), big_giants.values())))
print (max(zip(big_giants.keys(), big_giants.values())))
print (sorted(zip(big_giants.values(), big_giants.keys())))
print (sorted(zip(big_giants.keys(), big_giants.values())))



