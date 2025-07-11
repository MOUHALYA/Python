"""#code1 "Write a program that takes a list of integers as input, separated by spaces. The program should then identify and print the first element that appears only once in the list. After printing that unique element, the program should terminate."
a=[2,3,5,3,2]
list_a = list(map(int,input().split()))
for i in list_a:
    value = list_a.count(i)
    if value == 1:
        print(i)
    break


#code2 Write a program that takes two integer inputs, m and n, and calculates the sum of all integers between m (inclusive) and n (exclusive). Then, print the calculated sum."
m=int(input("Enter m value:"))
n=int(input("Enter n value:"))
sum = 0
for i in range(m,n):
    sum = sum + i
print(sum)"""


#code3
word = "c0d1n3"
l = []
c = ""
for i in word:
    if i.isdigit():
        l.append(i)
    elif i.isalpha():
        c.append(i)  
print(min(1))
print(max(1))
print(sum(1))
