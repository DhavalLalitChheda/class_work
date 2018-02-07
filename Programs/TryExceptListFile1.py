file = input('Please enter valid file: ')

try:
	fHandle = open(file)
except:
	print('File does not exist')
	exit()

try:	
	for line in fHandle:
		words = line.split()
		if len(words) != 0 and words[0] == 'From':
			print(words[2])
except:
	print('File contains no data')
	exit()