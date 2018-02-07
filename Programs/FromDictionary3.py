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
			temp1 = words[1].split('@')
			if temp1[1] not in temp:
				temp[temp1[1]] = 1 
			else:
				temp[temp1[1]] += 1
	
	lst = list()
	for key, value in temp.items():
		lst.append((value, key))
	
	lst.sort(reverse = True)
	print(lst[:1])
		
except:
	print('File contains no data')
	exit()