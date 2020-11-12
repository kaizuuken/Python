# For Dongusu Ile Faktoriyel Bulalim.
""""************************
Factorial finder program
************************

Press to 'q' for Quit.
"""

while True:
    Num=input("Num:")
    if Num == "q":
        print("The program is terminating...")
        break
    else:
        Num=int(Num)
        factorial=1

        for i in range(2,Num+1):
            factorial =factorial*i
        print("{} Factorial is = {} ".format(Num,factorial))
