#1. Write a program that evaluates if a user's age is less than 18. If it is, print "Underage." Otherwise, print "Adult."

age=int(input("Enter your age"))
if age<18:
	print("Underage")
else:
	print("Adult")



#2. Develop a program that checks if a person's temperature in Celsius is above 37 degrees. If it is, print "Fever detected." Otherwise, print "Normal temperature."

per_temp=int(input("Enter persons temperature"))
if per_temp>37:
	print("Fever Detected")
else:
	print("Normal Temperature")


#3. Develop a program that checks if a person's age is exactly 50. If it is, print "You're 50 years old." Otherwise, print "Your age is not 50."

per_age=int(input("Enter persons age"))
if per_age==50:
	print("You're 50 years old")
else:
	print("Your age is not 50")
