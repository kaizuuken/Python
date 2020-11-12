"""Problem 1
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak,
 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)"""

print("Welcome! to Perfect Number Finder Program.")
print("******************************************")

Num = int(input("Num:"))

i=1
total=0

while i < Num:
    if Num % i == 0:
        total+=i
    i+=1

if Num == total:
        print(Num,"is an Perfect Number.!")
else:
        print(Num,"is just a number :(")


"""Problem 2
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı
( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4"""


print("***********************************************")
print("Finding Amstrong Number")
print("***********************************************")

num=input("B:")
digit=len(num)
num=int(num)
total=0
digitcalculation=0

temporary_num = num


while temporary_num>0:
    digitcalculation=temporary_num%10
    total+=digitcalculation ** digit
    temporary_num=temporary_num//10

if total==num:
    print(num,"is an Amstrong number!")
else:
    print(num,"isnt an Amstrong Number.")

"""Problem 3
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.
"""
print("******************************************")
print("The Multiplication Table")
print("******************************************")

for i in range(1,11):
    print("******************************************")
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,i*j))

"""Problem 4
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene 
ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın."""

total=0

while True:
    num=input("Sayi:")
    if num=="q":
        print("the program is terminating..")
        break

    num=int(num)
    total+=num
print("total:",total)

"""Problem 5
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.
"""
Numbersdividedby_3=[]
for i in range(101):
    if i%3 == 0:
        Numbersdividedby_3.append(i)
print(Numbersdividedby_3)

# Continue kullanarakda deneyelim

sayilar=[]

for i in range(0,101):
    if i%3 !=0:
        continue
    else:
        sayilar.append(i)
print(sayilar)
