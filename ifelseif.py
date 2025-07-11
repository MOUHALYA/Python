#1.Write a program to use `if-else if` conditions to determine whether a student's exam score falls into one of the following categories: "Excellent" (score >= 90), "Good" (score >= 75), "Pass" (score >= 60), or "Fail" (score < 60). 

stu_score=int(input("Enter student score"))
if stu_score>=90:
	print("Excellent")
elif stu_score>=75:
	print("Good")
elif stu_score>=60:
	print("Pass")
elif stu_score<60:
	print("Fail")


#2.Write a program that uses `if-else if` conditions to classify a user-provided number as "Positive" (greater than 0), "Negative" (less than 0), or "Zero" (equal to 0). 

num=int(input("Enter the number:"))
if num>0:
	print("Positive")
elif num<0:
	print("Negative")
elif num==0:
	print("Zero")


#3.Develop a program that uses `if-else if` conditions to categorize a user's age into different groups, such as "Child" (0-12 years), "Teenager" (13-19 years), "Adult" (20-59 years), and "Senior" (60+ years). 

user_age=int(input("Enter users age:"))
if user_age<0 and user_age<=12:
	print("Child")
elif user_age>=13 and user_age<=19:
	print("Teenager")
elif user_age>=20 and user_age<=59:
	print("Adult")
elif user_age>=60:
	print("Senior")
