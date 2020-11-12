"""
Fibonacci Serisi yeni bir sayiyi onceki iki sayinin toplami seklinde olusturur.
1,1,2,3,5,8,13,21,34.......

"""

a=1 # 1. Fibonacci
b=1 # 2. Fibonacci

fibonacci=[a,b]

for i in range(20):

    a,b =b,a+b
    fibonacci.append(b)

print(fibonacci)
