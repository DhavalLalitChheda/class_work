temp = input("Please enter the sample string: ")

pos = temp.find(":")
num = float(temp[pos + 1 : ])
print(num)
print(type(num))