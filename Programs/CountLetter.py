def count(word, letter):
	c = 0
	for x in word:
		if x == letter:
			c = c + 1
	return c

temp = input("Please input a valid string: ")
l = input("Please input letter to be counted: ")
print("Letter ", l ," is repeated ", count(temp, l) , " times")