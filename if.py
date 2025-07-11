#1.Write a program that uses an `if` statement to check if a user-entered integer is less than 100. If the condition is met, print "Approved."

n=int(input("Enter Your Number"))
if n<100:
	print("Approved")



#2.Create a program that uses an `if` statement to determine whether a user-inputted temperature is above freezing (greater than 0 degrees Celsius). If it is, display "No frost." 

temp=int(input("Enter temperature"))
if temp>0:
	print("No Frost")


#3. Write a program that utilizes an `if` statement to check if a student's exam score is equal to or higher than 60. If the condition holds, print "Passed." 

score=int(input("Enter score"))
if score>=60:
	print("Passed")
