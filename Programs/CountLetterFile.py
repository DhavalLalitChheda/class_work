file = input('Please enter valid file: ')

try:
	fHandle = open(file)
except:
	print('File does not exist')
	exit()

try:
	temp = dict()
	for line in fHandle:
		line = line.lower()
		for x in line:
			if x not in 'abcdefghijklmnopqrstuvwxyz':
				continue
			if x not in temp:
				temp[x] = 1 
			else:
				temp[x] += 1
	
	lst = list()
	for key, val in temp.items():
		lst.append( (val, key) )
	lst.sort(reverse = True)

	for key, val in lst :
		print(key, val)
		
except:
	print('File contains no data')
	exit()