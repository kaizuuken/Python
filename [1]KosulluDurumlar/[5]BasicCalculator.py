print("""
***************************************
Calculator Program

1. Plus

2. Minus

3. Multiply

4. Divided 

***************************************


""")

a=int(input("1st Number: "))
b=int(input("2sn Number: "))

operation=input("enter operation:")

if operation=="1":
    print("{} + {}  {} .".format(a,b,a+b))
elif operation=="2":
    print("{} - {}  {} . ".format(a,b,a-b))
elif operation=="3":
    print("{} * {}  {} .".format(a,b,a*b))
elif operation=="4":
    print("{} / {}  {} .".format(a,b,a / b))
else:
    print("Invalid Operation")