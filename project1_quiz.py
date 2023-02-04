q1="""who is the greatest of all time(GOAT) in football history?
a.diego maradona
b.pele
c.christiano ronaldo
d.leonel messi"""

q2="""who scored most number of runs in test cricket?
a.ricky ponting
b.kumar sangakkara
c.brian lara
d.sachin tendulkar"""

q3="""what is the name of actor who played the role of ironman?
a.chris evans
b.chris pratt
c.chris hemsworth
d.robert downey jr"""

q4="""who is the director of the film (rrr)?
a.k raghavendra rao
b.b gopal
c.b sukumar
d.ss rajamouli"""

q5="""what is the name of the character played by kit harington in game of thrones?
a.ned stark
b.tyrion lannister
c.jamie lannister
d.jon snow"""


questions={q1:"d",q2:"d",q3:"d",q4:"d",q5:"d"}

name=input("hi what is your name")
print("hello",name,"welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("do you want to skip this question?(yes/no):")
    if flag1=="yes":
        continue
    answer=input("enter your answer:")
    if answer==questions[i]:
        print("wow! you got one point")
        score=score+1
        print("your current score is:",score)
    else:
        print("wrong answer,you lost one point")
        score=score-1
        print("your current score is:",score)
    flag2=input("do you want to quit?(yes/no):")
    if flag2=='yes':
        break
print("your total score is:",score)
    
    
