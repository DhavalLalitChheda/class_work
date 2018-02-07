def chop(list):
    del list[len(list) - 1]
    del list[0]

letters = ['a', 'b', 'c', 'd', 'e','f']
chop(letters)
print(letters)