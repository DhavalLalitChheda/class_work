count = 0
total = 0
while True:
    temp = input("Please enter a number: ")
    if temp == "done" : 
        break
    try:
        num = float(temp)
    except:
        print("Invalid input, please enter a valid number or done to finish")
        continue
    count = count + 1
    total = total + num
print("")
print(total, count, total/count)