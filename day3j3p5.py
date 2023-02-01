size=int(input("enter the size of list:"))
L=[]
p=1
s=0
for i in range(size):
    element=int(input("enter an element:"))
    L.append(element)
print(L)
for i in L:
    p=p*i
    s=s+i
print(p)
print(s)
if p<750:
    print(p)
else:
    print(s)
