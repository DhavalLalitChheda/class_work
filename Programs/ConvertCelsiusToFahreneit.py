def convertToFahreneit(temp_Celsius):
	return temp_Celsius * 9 / 5 + 32

temp_Celsius = float(input("Please enter temp in celsius: "))
print("The temperature in Fahreneit is: ", convertToFahreneit(temp_Celsius))