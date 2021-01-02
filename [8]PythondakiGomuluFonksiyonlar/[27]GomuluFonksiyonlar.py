print("Gomulu Fonksiyonlar ---------------------------")

"""
map() fonksiyonu

                map(fonksiyon,iterasyon yapılabilecek veritipi(liste,demet vb),....)

map() fonksiyonu ilk parametre olarak bir tane fonksiyon objesi alır. (Fonksiyonlar da birer obje olduğu için başka bir 
fonksiyona gönderilebilir.) 2. parametre olarak da bir tane iterasyon yapılacak veritipi alarak , gönderilen fonksiyonu
 her bir eleman üzerinde uygulayarak sonuçları bir map objesi olarak döner. 
"""
def double(x):
    return x*2
print(map(double,[1,2,3,4,5,6])) # out:<map object at 0x7ff0778b2dc0>
print(list(map(double,[1,2,3,4,5,6]))) #out:[2, 4, 6, 8, 10, 12]

# Soyle deneyelim

lst1=[1,2,3,4,6,7,8,9]

print(list(map(double,lst1))) # out:2, 4, 6, 8, 12, 14, 16, 18] Basarili..
print(double(lst1)) # Bu seklilde listeyi 2 ile carpti.. out: [1, 2, 3, 4, 6, 7, 8, 9, 1, 2, 3, 4, 6, 7, 8, 9]

"""Map fonksiyonu birden fazla liste veya demet alabilir."""

lst1=[1,2,3,4,6,7,8,9]
lst2=[2,4,6,8,10,12,14,16]
def multiply(x,y):
    return x * y


print(list(map(multiply,lst1,lst2)))

"""
reduce() fonksiyonu

                reduce(function, iterasyon yapılabilen veritipi(liste vb.))

reduce() fonksiyonu değer olarak aldığı fonksiyonu soldan başlayarak listenin ilk 2 elemanına uygular 
ve daha sonra çıkan sonucu listenin 3. elemanına uygular ve bu şekilde devam ederek liste bitince bir tane değer döner.


"""


from functools import reduce

def summ(x,y):
    return x+y

print(reduce(summ,[12,14,15,13])) # out : 54 Ilk iki elemani topladi sonra 26 sonra 15 ekledi ve 13 ekledi

# Reduce() kumulatif bir fonksiyon yani birike birike calisiyor.

# Faktoriyel bulmak icin kullanalim

def fact(x,y):
    return  x*y

print(reduce(fact,[1,2,3,4,5]))  # 120
# Veya carparak devam edebiliriz
print(reduce(fact,[3,5,10,20])) # 3000

# max fonksiyonu()
print(max([1,2,3,4,5,6]))  # 6

# reduce ile max fonksiyonu
def maximum(x,y):
    if (x > y):
        return x
    else:
        return y

print(reduce(maximum,[-2,1,100,35,32])) # 100

"""
filter() fonsiyonu

             filter(fonksiyon,iterasyon yapılabilen bir veritipi(liste vb.))

filter() fonksiyonu birinci parametre olarak mutlaka mantıksal değer dönen (True , False) bir fonksiyon alır ve liste
 gibi veritiplerinin her bir elemanına bu fonksiyonunu uygular. filter sadece True sonuç çıkaran değerleri alarak 
 bir tane filter objesi döner. 

"""

def odd_nums(x):
    if x % 2 == 0:
        return True
    else:
        return False


print(list(filter(odd_nums,[1,2,3,4,5,6,7,8,9]))) # Out : [2, 4, 6, 8]

def is_it_prime(x):
    i=2
    if x==1:
        return False # Asal degil
    elif x==2:
        return True # Asal
    else:
        while i<x:
            if x % i == 0 :
                return False # Asal degil
            i+=1
        else:
            return True

print(is_it_prime(3))
print(is_it_prime(5))
print(is_it_prime(12))

print(list(filter(is_it_prime,range(1,100)))) # 1 den 100 e kadar olan asal sayilar
                # out:[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

"""
zip() fonksiyonu 

Burada zip fonksiyonunun kullanımını görüyoruz. zip fonksiyonu listelerin elemanları sırasıyla demet şeklinde 
gruplayarak bir tane liste oluşturuyor.

"""
liste1=[1,2,3,4,5]
liste2=[6,7,8,9,10]

#  Sonucu [(1,6),(2,7),(3,8),(4,9),(5,10)] yapmaya çalışalım

i=0
sonuc=list()
while i<len(liste1) and i<len(liste2):
    sonuc.append((liste1[i],liste2[i]))
    i+=1
print(sonuc)

# Peki böyle uzun bir işlemi zip fonksiyonuyla nasıl yaparız ?

print(list(zip(liste1,liste2))) # out: [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = ["Python","Php","Java","Javascript","C"]

print(list(zip(liste1,liste2,liste3)))

# Ayni anda iki liste uzerinde gezinmek

liste1 = [1,2,3,4]
liste3 = ["Python","Php","Java","Javascript","C"]

for i,j in zip(liste1,liste3):
    print("i:",i,"j:",j)
    # i: 1 j: Python
    # i: 2 j: Php
    # i: 3 j: Java
    # i: 4 j: Javascript

# Sözlükleri zipleyelim.
sözlük1 = {"Elma":1,"Armut":2,"Kiraz":3}
sözlük2 = {"Sıfır":0,"Bir":1,"İki":2}

print(list(zip(sözlük1,sözlük2))) # Anahtarlar eşleşti.

"""
enumerate() fonksiyonu
enumerate, for döngülerinde çoğu zaman işlerimizi oldukça kolaylaştırmaktadır. Bu fonksiyonlar aklınızda bulunsun.
 Bir gün elbet ihtiyacınız olacak :)

"""
liste = ["Elma","Armut","Muz","Kiraz"]

# sonucu [(0,'Elma'),(1,'Armut'),(2,'Muz'),(3,'Kiraz')] yapmak istiyoruz.

sonuc = list()
step=0
for i in liste:
    sonuc.append((step,i))
    step+= 1
print(sonuc)

# Enumerate ile nasil yaparz?

print(list(enumerate(liste))) # Basarili

# Örneğin bir listenin çift indekslerini(0,2,4) enumerate kullanarak nasıl yazdırabiliriz ?

liste = ["a","b","c","d","e","f","g"]

for index,eleman in enumerate(liste):
    if index % 2 ==0 :
        print("eleman:",eleman)

"""
all() ve any() fonksiyonlari

all() fonksiyonu bütün değerler True ise True, en az bir değer False ise False sonuç döndürür.
any() fonksiyonu bütün değerler False ise False, en az bir değer True ise True sonuç döndürür.

"""
# En az 1 tanesi false olsa bile false dondurelim

def hepsi(liste):
    for i in liste:
        if not i:  # i false ise
            return False
    return True

liste = [True,False,True,False,True]

print(hepsi(liste)) # False , Cunku en az birisi false

liste = [1,2,3,4,5]
print(hepsi(liste)) # True , cunku 0 haric butun sayilar True temsil eder.

def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False
#  Herhangi bir değer True ise True, Hepsi False ise False döndürmek istiyoruz.
liste = [True,False,True,False,True]
print(herhangi(liste)) # True

liste = [0,0,0,0,0,0,0] # Bütün değerler False , 0 = False
print(herhangi(liste)) # False

"""
Aslında bu işlemleri all() ve any() fonksiyonları yapmaktadır. İsterseniz bunların örneklerine bakalım.
all() fonksiyonu bütün değerler True ise True, en az bir değer False ise False sonuç döndürür.
any() fonksiyonu bütün değerler False ise False, en az bir değer True ise True sonuç döndürür.
"""

liste = [True,False,True,False,True]
print(all(liste)) # False
print(any(liste)) # True

liste = [1,2,3,4,5]
print(all(liste)) # True
print(any(liste)) # True
