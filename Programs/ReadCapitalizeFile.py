inputFile = input('Please enter a valid filename: ')
try:
	
	fhandle = open(inputFile)
except:
	print('Invalid file')
	exit()
for line in fhandle:
	line = line.upper()
	print(line)