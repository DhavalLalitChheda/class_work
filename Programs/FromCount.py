file = input('Please enter valid file: ')

try:
	fHandle = open(file)
except:
	print('File does not exist')
	exit()

try:
	count = 0
	for line in fHandle:
		words = line.split()
		if len(words) > 0 and words[0].startswith('From'):
			count = count + 1
			print(words[1])
	print('There are ',count,' lines that start with From')
		
except:
	print('File contains no data')
	exit()