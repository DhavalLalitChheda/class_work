max = None
min = None
while True:
	temp =  input("Please enter a number: ")
	if temp == 'done':
		break
	try:
		num = float(temp)
	except:
		print("Please enter a valid number")
		continue
	if(max is None or num > max):
		max = num
	if(min is None or num < min):
		min = num

print("Max: ", max)
print("Min: ", min)