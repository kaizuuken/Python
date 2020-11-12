"""Asal Sayilar 1 ve Kendisinden Baska Bir Sayiya Bolunmeyen Sayilardir."""

def is_it_prime(num):
    if num == 1:
        return False
    elif num==2:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
        else:
            return True

while True:
    try:
        num=input("Number:")

        if num =="q":
            break
        else:
            num=int(num)

        is_it_prime(num)

        if is_it_prime(num)==False:
            print(num,"Isnt a Prime Number!!")
        else:
            print(num,"Is a Prime number")
    except ValueError:
        print("Please Enter a Number!")

""" HATA BLOGU Sonradan eklendi."""


