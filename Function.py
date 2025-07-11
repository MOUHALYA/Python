def greet():
    print("Hello")
a=['Hi']
def wish():
    a[0]+="Hello"
def getData():
    return a[0]+ 'hi...'
print(r)
x=getData()
print(x)
greet()
print("Before Wish",a)
wish()
print("After Wish",a)
getData()
r=getData()
print(r)
