list = []
while True:
	temp = input('Enter a number: ')
	if temp == 'done':
		break;
	try:
		num = float(temp)
	except:
		print('Invalid num')
		continue
	list.append(num)

print(max(list))
print(min(list))