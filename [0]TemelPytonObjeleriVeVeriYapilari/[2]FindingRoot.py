"""
Oncelikle Notlar alalim.

denklem : ax^2 bx + c
delta hesabi : b^2-4*a*c

1st root: (-b - delta ** 0.5)/(2*a)
2nd root:  (-b + delta ** 0.5)/(2*a)


"""


a=float(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))

delta=b**2-4*a*c
x1=(-b-delta**0.5)/(2*a)
x2=(-b+delta**0.5)/(2*a)

print("1st root:{}\n2nd root:{}".format(x1,x2))



