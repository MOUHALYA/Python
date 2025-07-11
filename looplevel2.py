"""1)Write a program that takes an integer N as input and prints numbers from 1 to N, but:
If the number is a multiple of 3, add 5 to it before printing.
If the number is a multiple of 5, subtract 3 before printing.
If a number is both a multiple of 3 and 5, print it as 0."""
N = int(input("Enter an Number:"))
for i in range(1,N):
    if i % 3 == 0  and i % 5 == 0:
        print("0")
    elif i % 3 == 0:
        print(i+5)
    elif i % 5 == 0:
        print(i-3)



"""2)Write a program that takes an integer N and computes the below opertions numbers from 1 to N,
    1. Odd numbers are added as is.
    2. Even numbers are subtracted."""
N = int(input("Enter an number:"))
odd = 0
even = 0
for i in range(1,N+1):
    if i % 2 != 0:
        odd = odd + i
        print("Odd:",odd)
    else:
        even = even - i
        print("Even:",even)



"""3)Write a program that takes an integer N and a single-digit number D,
and counts how many times D appears in N."""
N = int(input("Enter a Number:"))
D = int(input("Enter a single-digit number:"))
N_str = str(N)
D_str = str(D)
count = 0
for digit in N_str:
    if digit == D_str:
        count += 1
print(count)




"""4)Write a program that takes an integer N and prints its digits in reverse order
without converting it to a string."""
N = int(input("Enter an Number:"))
for i in range(N,0,-1):
    print(i,end = " ")





"""5)Write a program that takes an integer N and finds its largest digit
without using strings or arrays.
"""
N = int(input("Enter an Number:"))
lar = 0
while N > 0:
    digit = N % 10 # Extract the last digit-last digit teesukuntundi
    if digit > lar:
        lar = digit
    N = N // 10  # Remove the last digit
print(lar)





"""6)Write a program that takes an integer N and finds the sum of its even digits only."""
N = int(input("Enter an Number:"))
N_str = str(N)
sum = 0
for digit in N_str:
    if int(digit) % 2 == 0:
        sum = sum + int(digit)
print("Sum of Even Digits:",sum)


"""7)Write a program that takes an integer N and multiplies all of its non-zero digits together.
"""




"""8)Write a program that takes an integer N and prints numbers from 1 to N,
but modifies them based on these rules:
If a number is divisible by 2, multiply it by 3.
If a number is divisible by 3, divide it by 2.
"""
N = int(input("Enter an Number: "))
for i in range(1,N+1):
    if i % 2 == 0:
        print(i*3)
    if i % 3 == 0:
        print(i/2)



"""9)Write a program that takes a string S and a character C,
and counts how many times C appears in S."""
S = input("Enter an string:")
C = input("Enter an character:")
count = 0
for l in S:
    if C in l:
        count = count+1
print(count)


"""10)Write a program that takes a string S and checks its password strength based on these rules:
If S has both uppercase and lowercase letters, print "Strong".
If S has only uppercase or only lowercase, print "Weak".
If S contains only numbers, print "Very Weak".
"""
def password(p):
    upper = False
    lower = False
    digit = False
    for i in p:
        if i.isupper():
            upper = True
        elif i.islower():
            lower = True
        elif i.isdigit():
            digit = True
    if upper and lower and digit:
        return "Strong" 
    elif upper or lower:
        return "Weak"
    elif digit:
        return "very weak" 
s = input("Enter your password:")
print(password(s))   


"""without def"""
s = input("Enter your password:")
isupper = False
islower = False
isdigit = False
for i in s:
    if i.isupper():
        isupper = True
    elif i.islower():
        islower = True
    elif i.isdigit():
        isdigit = True
if isupper and islower and isdigit:
    print("Given password is strong")
elif s.isupper() or s.islower():
    print("Given password is weak")
elif s.isdigit:
    print("Given password is very weak")
else:
    print("Given password is invalid")
