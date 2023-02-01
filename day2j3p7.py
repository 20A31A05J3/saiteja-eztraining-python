import random
n=random.randrange(1,50)
guess=int(input("enter a value:"))
while n!=guess:
    if guess<n:
        print("too low")
        guess=int(input("enter the value again:"))
    elif guess>n:
        print("too high")
        guess=int(input("enter the value again:"))
    else:
        break
print("your guess is right")
    
        
