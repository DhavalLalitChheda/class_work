file = input('Please enter valid file: ')

try:
	fHandle = open(file)
except:
	print('File does not exist')
	exit()

try:
	list = []
	for line in fHandle:
		words = line.split()
		for i in words:
			if i in list:
				continue;
			list.append(i)
	
	list.sort()
	print(list)
		
except:
	print('File contains no data')
	exit()