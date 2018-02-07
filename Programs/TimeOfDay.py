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
			d1,d2,d3 = words[5].split(':')
			if d1 not in temp:
				temp[d1] = 1 
			else:
				temp[d1] += 1
	
	lst = list()
	for key, value in temp.items():
		lst.append((key, value))
	
	lst.sort()
	for key, value in lst :
		print(key, value)
		
except:
	print('File contains no data')
	exit()