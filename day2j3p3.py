t=int(input("enter the value of temperature:"))
if t>45:
    print("hottest")
elif t>=40 and t<=45:
    print("hot")
elif t>=25 and t<40:
    print("moderate")
elif t>=10 and t<25:
    print("cold")
else:
    print("chill")
