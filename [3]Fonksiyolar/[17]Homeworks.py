"""1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup
olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır
 (1 + 2 + 3 = 6)."""

def perfectnum(num):
    disivors=0
    for i in range(1,num):
        if num % i == 0:
            disivors+=i
    return disivors



num=int(input("Number:"))
if perfectnum(num) == num:
    print(num,"Is a Perfect Num!")
else:
    print(num,"Is Just a nubmer :(")

"""Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;"""

#LCD : largest common dividers asdjaskdasd
def lcd(num1, num2):
    i = 1
    lcd = 1
    while (i <= num1 and i <= num2):

        if (not (num1 % i) and not (num2 % i)):
            lcd = i
        i += 1
    return lcd


num1 = int(input("Number-1:"))
num2 = int(input("Number-2:"))

print("Ebob:", lcd(num1, num2))

"""Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi"""

birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunus(sayi):
    birinci=sayi%10
    ikinci=sayi//10

    return onlar[ikinci] +" "+birler[birinci]
sayi=int(input("Sayi----------->"))
print(okunus(sayi))


"""1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)"""

def pisagor():
    lst=[]
    for i in range(1,101):
        for j in range(1,101):
            operation=(i**2 + j**2) **0.5
            if operation==int(operation):
                lst.append((i,j,int(operation)))
    return lst
for i in pisagor():
    print(i)


















