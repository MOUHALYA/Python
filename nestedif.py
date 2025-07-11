#1.Write a program to use a nested `if` statement to check if a user-entered integer is less than 100 but greater than or equal to 50. If the condition is met, print "Condition met"; otherwise, print "Condition not met." 

integer=int(input("enter integer values"))
if integer<100:
	if integer>=50:
		print("Condition met")
	else:
		print("Condition not met")
else:
	print("Condition not met")



#2.Write a C program that checks if a user-entered integer is positive or negative. If the integer is negative, it then checks whether it's even or odd using nested if statements.

num=int(input("Enter an integer"))
if num<0:
	if num%2==0:
		print("integer is negative and even")
	else:
		print("integer is negative and odd")
else:
	print("integer is positive")
