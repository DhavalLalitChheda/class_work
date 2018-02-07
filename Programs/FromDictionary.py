file = input('Please enter valid file: ')

try:
	fHandle = open(file)
except:
	print('File does not exist')
	exit()

try:
	temp = dict()
	for line in fHandle:
		words = line.split()
		if len(words) > 0 and words[0] == 'From':
			if words[2] not in temp:
				temp[words[2]] = 1 
			else:
				temp[words[2]] += 1
	print(temp)
		
except:
	print('File contains no data')
	exit()