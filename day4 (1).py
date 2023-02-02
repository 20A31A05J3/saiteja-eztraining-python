'''d={n:n*n for n in range(1,6)}
print(d)




#calculating product for 5 units
old={'rice':60 , 'dhaal':50 , 'oil':170}
new={product:price*5 for (product,price) in old.items()}
print(new)




#with checks
real={'chaiteja':81 , 'david':21 , 'frem':34}
now={name:age for (name,age) in real.items() if age>30}
print(now)



##create a list with 8 customer names display a dictionary which has customer
#names along with discounts for them from a particular shop.....randrange




import random
l=["tyrian","jamie","eddard","jonsnow","danaerys","greyworm","jorah","drogo"]
dis={name:random.randint(1,100) for name in l}
print(dis)


l1=['a','b','c']
l2=[1,2,3]
d={l1:l2 for (l1,l2) in zip(l1,l2)}
print(d)



##create 2 lists 1st list shouls have 5 names and 2nd have marks(1,500) names as keys
##percentage of marks as values


s=['david','saiteja','prem','umesh','vardhan']
m=[450,499,470,456,501]
d1={s:m for (s,m) in zip(s,m)}
print(d1)
d2={s:(m*100)/500 for (s,m) in d1.items()}
print(d2)



s="David raju"
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.replace('u','a'))
print(s.strip())
print(s.split())
print(s.split(','))
print(s.split('.'))
print(s.count('a'))



s="hellothere"
if 'x'in s:
    print(s)
else:
    print("there is no such character")


v=input("enter a string:")
if v[0:]==v[::-1]:
    print("it is palindrome")
else:
    print("no")



l=["a","e","i","o","u"]
s=input("Enter a string:")
count=0
for i in s:
    
    if i in l:
        count=count+1
print(count)'''


import math
print("CEIL 12.5:", math.ceil(12.5))
print("FLOOR 12.5:",math.floor(12.5))
print("SQRT 345",math.sqrt(345))
print("Factorial 3:",math.factorial(3))
print("Power 2,3",math.pow(2,3))
print("Remainder 10,3",math.fmod(10,3))
a,b=divmod(10,3)
print(a,b)







































































































