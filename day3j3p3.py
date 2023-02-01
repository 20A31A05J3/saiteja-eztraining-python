size=int(input("enter the size of list:"))
L=[]
for i in range(size):
    element=int(input("enter an element:"))
    L.append(element)
print(L)
for j in L:
    if j%2==0:
        print(j)
