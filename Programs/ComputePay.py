def computePay(hours, rate):
	if(hours <= 40):
		return hours * rate
	else:
		return hours * rate + ((hours - 40) * rate * 0.5)
		
hours = float(input("Please enter number of hours: "))
rate = float(input("Please enter hourly rate: "))
print("Pay: $", computePay(hours, rate))