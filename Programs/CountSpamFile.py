inputFile = input('Please enter a valid filename: ')
count = 0
c = 0
try:
	
	fhandle = open(inputFile)
except:
	print('Invalid file')
	exit()
for line in fhandle:
	if line.startswith('X-DSPAM-Confidence'):
		c = c + 1
		a,b = line.split(':')
		count = count + float(b)

print(count/c)