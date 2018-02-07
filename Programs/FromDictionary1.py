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
			if words[1] not in temp:
				temp[words[1]] = 1 
			else:
				temp[words[1]] += 1
	
	for key in temp:
		if temp[key] == max(temp.values()):
			print(key, temp[key])
		
except:
	print('File contains no data')
	exit()