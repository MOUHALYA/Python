"""1)Write a program that takes three integers as input and returns the largest of these three numbers. 
"""
def largest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
            return b
    else:
        return c
a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
c = int(input("Enter c value:"))
result = largest(a,b,c)
print(result)


"""2)Given a number N, write a program that calculates and outputs the sum of the first N natural numbers starting from 1."""
n = int(input("Enter n value:"))
sum = 0
for i in range(1,n+1):
    sum += i
print("Sum:",sum)


"""3)Given a number X, write a program that prints the multiplication table of X from 1 to 10.
"""
X = int(input("Enter X value:"))
for i in range(1,11):
    print(X,"*",i,"=",X*i)
    

"""4)Write a program that takes a year Y and checks whether it is a leap year or not.?
"""
year = int(input("Enter a Year:"))
if (year % 4 == 0 and year % 100 != 0 )or year % 400 == 0:
    print("Leap Year")
else:
    print("Non-Leap Year")


"""5)Given a number N, write a program that counts the number of digits in N.
"""
N = int(input("Enter N value:"))
count = 0
for i in range(1,N):
    count = count + i
print(i)



"""6) How would you print the first N natural numbers using both a while and a for loop?
"""
N = int(input("Enter N number:"))
for i in range(1,N):
    print(i)

# Using While Loop
W = int(input("Enter W number:"))
i = 1
while i < W :
    print(i)
    i = i+1


"""7)Write a program that takes a number X as input and prints all the divisors of X. 
"""
X = int(input("Enter X value:"))
for i in range(1,X):
    if X % i == 0:
        print(i)


"""8)Write a program that takes an integer N as input and reverses its digits using a loop. 
"""
"""N = int(input("Enter N value:"))
rev = " "
for i in range(N,0,-1):
    print(i)"""
n = int(input("Enter n value:"))
rev = " "
for i in range(1,n):
    rev = str(i) +" "+ rev 
print(rev)


"""9Write a program that takes a string as input and prints only the vowels (a, e, i, o, u) present in the string."""
name = input("Enter an string:")
vowels = 'aeiouAEIOU'
result = ""
for char in name:
    if char in vowels:
        result += char
print(result)


"""10)Using a loop, write a program that prints all the lowercase alphabets from a to z. What is the most efficient way to loop through all the alphabet characters?"""
a = input("Enter an alphabet:")
z = input("Enter an alphabet:")
for i in range(ord(a),ord(z)+1):
    print(chr(i),end=" ")
