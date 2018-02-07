file = input('Please enter valid file: ')

try:
	fHandle = open(file)
except:
	print('File does not exist')
	exit()

try:
	dictionary = {}
	for line in fHandle:
		words = line.split()
		for word in words:
			if word not in dictionary:
				dictionary[word] = 1
			else:
				dictionary[word] += 1
	print(dictionary)
		
except:
	print('File contains no data')
	exit()