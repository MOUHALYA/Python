s=input()
r=input()
c=['this','is','an']
l=int(input())
s=s.split()
sl=s
def processData():
    for i in range(len(s)):#['this','is','python']
        if s[i] in c and len(s[i])<l:
             sl[i]=r
        else:
            sl[i]=s[i]
    return " ".join(sl)
r=processData()
print(r)
