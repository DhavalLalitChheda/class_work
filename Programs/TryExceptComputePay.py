def computePay(hours, rate):
	if(hours <= 40):
		return hours * rate
	else:
		return hours * rate + ((hours - 40) * rate * 0.5)
try:		
	hours = float(input("Please enter number of hours: "))
	rate = float(input("Please enter hourly rate: "))
except:
	print("Error, please enter numeric input")
	quit()

print("Pay: $", computePay(hours, rate))