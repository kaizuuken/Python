"""Programlama Ödevi - Modüller
Proje 1
Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirmeye çalışın.

"""

import math
help(math)

print("""
********************************************************
Casio Classwiz fx-82EX
********************************************************
^Press "q" For the Quit^

^Press 1 for trigonometric operations.^
^Press 2 for Mod^
^Press 3 For Factorial^
^Press 4 - + / x^
^Press 5 for logarithmic operations^
^Press 6 exponentiate or Root^

DATA e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

""")
while True:
    operation=input("Bir Islem Giriniz:")

    if operation == "q":
        print("The Program is terminating")
        break
    elif operation == "4":

        fouroperation=input("Plus -1,Minus-2,Multiplication-3,Divide-4:")
        a = int(input("1.Sayi:"))
        b = int(input("2.Sayi:"))

        if fouroperation == "1":
            print("{} + {} = {}".format(a,b,a+b))
        elif fouroperation == "2":
            print("{} - {} = {}".format(a, b, a - b))
        elif fouroperation == "3":
            print("{} x {} = {}".format(a,b,a*b))
        else:
            print("{} / {} = {}".format(a, b, a / b))

    elif operation=="1":
        print("""
        For the cosine of an angle '1'
        For the sine of an angle '2'
        For the Tangent of an angle '3'
        
        
        """)
        triginometric=input("Enter a Operation:")

        if triginometric =="1":
            angle=int(input("The Angle You Want to Take Cosine:"))
            angle2=float(angle*3.141592653589793/180)
            angle3=math.cos(angle2)
            print(angle,"Cosune of the angle:",angle3,"dir.")
        elif triginometric == "2":
            angle = int(input("The Angle you want to take sine:"))
            angle2 = float(angle * 3.141592653589793 / 180)
            angle = math.sin(angle2)
            print(angle, "Sine of the angle:", angle3, "dir.")
        elif triginometric=="3":
            angle = int(input("The angle you want to take tangent:"))
            angle2 = float(angle * 3.141592653589793 / 180)
            angle3 = math.tan(angle2)
            print(angle, "Tangent if the angle,",angle3,"dir.")
    elif operation == "2":

        mod1=int(input("The Num you want to take mod:"))
        mod2=int(input("Divider Num:"))
        print("{} % {} = {}".format(mod1,mod2,math.fmod(mod1,mod2)))

    elif operation == "3":
        fac=int(input("The Num you want to take Factrial:"))
        print(fac,"Factorial=",math.factorial(fac))

    elif operation  == "5":
        log=int(input("Base number:"))
        log1=int(input("Power:"))

        print("log{}^{} = {}".format(log,log1,math.log(log,log1)))
    elif operation == "6":
        print("""
         For the exponantiate --------press 'p' 
         For the SquareRoot --------press 'r' 
         
         """)
        sqrt=input("Enter Operation 'p' or 'r':")
        if sqrt == "r":
            num=int(input("Num:"))
            print("the squareroot of the {} is {}".format(num,math.sqrt(num)))
        if sqrt == "p":
            num2=int(input("Num:"))
            num3=int(input("Power:"))
            num4=num2**num3
            print(num4)


