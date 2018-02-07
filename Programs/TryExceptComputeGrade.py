def computeGrade(score):
	result = ''
	if(score < 0.0 or score > 1.0):
		result = 'Bad Score'
	elif(score > 0.9):
		result = 'A'
	elif(score > 0.8):
		result = 'B'
	elif(score > 0.7):
		result = 'C'
	elif(score > 0.6):
		result = 'D'
	else:
		result = 'F'
	return result
try:	
	score = float(input("Please enter a valid score from 0 to 1.0: "))
	print(computeGrade(score))
except:
	print("Bad Score")
	quit()
	