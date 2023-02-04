'''a=100
b=0
try:
    print(a/b)
except Exception as a:
    print("please note,number cannot be divided by zero",a)
print("bye")'''

'''filename=input("enter the name of file:")
a="."
i=filename.index(a)
l=len(filename)
if a in filename:
    print(filename[i+1:l+1])'''

'''a=10
b=0
try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("do not give second number as zero",e)
finally:
    print("resource closed")'''

'''a=10
try:
    b=int(input("enter the number:"))
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print("please note,number cannot be divided with zero",e)
except ValueError as e:
    print("invalid input",e)
except Exception as e:
    print("other error",e)
finally:
    print("resource closed")'''

'''x=9
if x%2!=0:
    raise Exception("x should be even number")
else:
    print("x is an even number,correct")'''

'''its an efficienr concept used in all programming languages like java and python.
for multiple reasons we use oops concept. for example, code reusability,data
security,hiding data
class:
its a blue printexample:birds,laptops
object:
its a thing created based on class
note:
one class can have multiple objects
class:laptop objects:lenovo,hp,dell'''

'''class computer:
    def config(self):
        print("yes")
lenovo=computer()
lenovo.config()
dell=computer()
dell.config()'''

'''class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print("ID:%d \nName: %s" % (self.id,self.name))
emp1=Employee("john",101)
emp2=Employee("david",102)
emp1.display()
emp2.display()'''

class computer():
    a=10
    b=20
    print("class variable inside class",a)
    def config(self):
        c=100
        print("yes")
        print("instance access",self.b)
lenovo=computer()
print(lenovo.a)
print(lenovo.a+lenovo.b)
dell=computer()
print("dell",dell.a)
lenovo.config()




