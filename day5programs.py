'''import random as r
x="i love sweets"
print(r.sample(x,2))'''

'''import random as r
a=[1,2,3,4,5,6]
r.shuffle(a)
print(a)'''

'''import random as r
a=[1,2,3,4,5,6]
print(r.choice(a))'''

'''import random as r
b="welcome back"
print(r.choice(b))'''

'''import random as r
a=[1,2,3,4,5,6]
a=r.random()
print(a)'''

'''import random as r
print(r.randint(20,30))'''

'''import random as r
a=[10,20,30,40,50,60]
print(r.choices(a,k=11))'''

'''import random as r
s="hello good day"
print(r.choices(s,k=3))'''

'''import random as r
print(r.uniform(5,10))'''

'''import random as r
z=dir(r)
print(z)'''

'''import calendar
print("Full calendar")
print(calendar.calendar(2022))
print("Particular Month")
print(calendar.month(2022,12))
print("Set first day of the week")
calendar.setfirstweekday(calendar.FRIDAY)
print(calendar.month(2022,12))'''

'''import datetime
a=datetime.datetime.now()
print(a)
sv=a.strftime("%y")
fv=a.strftime("%Y")
print("Year short version",sv)
print("Year full version",fv)'''

'''def sample():
    print("great day")
    print("happy time")
sample()
print("today")
sample()'''

'''n=int(input("enter the value of n:"))
p=1
i=0
while i<n:
    i=i+1
    p=p*i    
print(p)'''

'''def multi():
    n1=int(input("number:"))
    n2=int(input("number:"))
    n3=int(input("number:"))
    product=n1*n2*n3
    print(product)
multi()'''

'''def multi():
    n1=int(input("number:"))
    n2=int(input("number:"))
    n3=int(input("number:"))
    product=n1*n2*n3
    return product
result=multi()
print(result)'''

'''def multi(n1,n2,n3):
    product=n1*n2*n3
    print(product)
multi(3,4,5)'''

'''def multi(a,b,c):
    product=a*b*c
    print(product)
n1=int(input("enter 1:"))
n2=int(input("enter 2:"))
n3=int(input("enter 3:"))
multi(n1,n2,n3)'''

'''def multi(n1,n2,n3):
    product=n1*n2*n3
    return product
result=multi(3,4,5)
print(result)
def multi(a,b,c):
    product=a*b*c
    return product
n1=int(input("enter 1:"))
n2=int(input("enter 2:"))
n3=int(input("enter 3:"))
result1=multi(n1,n2,n3)
print(result1)'''

'''n=int(input("enter number of lemons in hand:"))
total=21
def excess():
    if n>total:
        a=n-total
        print(a)
excess()
def lower():
    if n<total:
        b=total-n
        print(b)
lower()'''

'''n=int(input("enter a number:"))
def factors():
    for i in range(1,n+1):
        if n%i==0:
            print(i)
factors()'''

'''def multi_table(n):
    for i in range(1,11):
        print(i,"x",n,"=",i*n)
n=int(input("which table:"))
multi_table(n)'''

'''def digits(n):
    sum=0
    while n!=0:
        rem=n%10
        sum=sum+rem
        n=n//10
    return sum
n=int(input("enter a number:"))
res=digits(n)
print(res)'''

'''def display():
    n=int(input("enter a number:"))
    if n==1:
        display()
    else:
        print("over")
display()'''

'''def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result=fact(4)
print(result)'''

'''n=int(input("enter a number:"))
a=0
b=1
sum=0
count=1
while(count<=n):
    print(sum,end=" ")
    count=count+1
    a=b
    b=sum
    sum=a+b'''

'''def add_sub(x,y):
    sub=x-y
    add=x+y
    return sub,add
res1,res2=add_sub(20,10)
print(res1)
print(res2)'''

'''def sum(*a):
    c=0
    for i in a:
        c=c+i
    print(c)
sum(10,2,3,1,2)'''
        


    
    
    










    




