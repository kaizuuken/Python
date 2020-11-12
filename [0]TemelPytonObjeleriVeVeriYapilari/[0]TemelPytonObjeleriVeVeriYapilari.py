# Tam sayilar INTEGER
# Ondalik sayilar FLOAT
# Toplama + , Cikartma - , Carpma * , Bolme /
from typing import Set

print(13 * 3)  # 39
print(13 / 3)  # 4.333333333
i = 10
print(i + i)  # 20

# 1. Değişken isimleri bir sayı ile başlayamaz.
# 2. Değişken ismi kelimelerden oluşuyorsa aralarında boşluk olamaz.
# #3. :'",<>/?|\()!@#$%^&*~-+ Buradaki semboller değişken ismi içinde kullanılamaz.(Sadece _ sembolü kullanılabilir)
# 4. Pythonda tanımlı anahtar kelimeler değişken ismi olarak kullanılamaz.(while, not vs. )


# iki degiskenin degeri bibiri ile degistirmek icin pratik bir yontem var:
a = 4
b = 3
a, b = b, a
print(a)  # 3
print(b)  # 4

a += 1
print(a)  # 4 a=a+1 ile ayni sey!
b = b - 1
print(b)  # 3 Oldu.
b -= 1
print(b)  # 2oldu:)

"""
buralar yorum satiri olarak degerlerdiriliyor Python buralari okuyup yorum yapmiyor

"""

# Tamsayi bolemesi icin //
# Bolumden Kalanini bulma (mod) %
# Ust alma  **

print(12 // 5)  # 2
print(12 % 5)  # 2
print(12 / 5)  # 2.4
print(12 ** 5)  # 248832

# STRING
print("yusuf erdem")  # yusuf erdem
print("""yusuf erdem""")  # yusuf erdem
print('yusuf erdem')  # yusuf erdem
naber = "naber iyi misin?"
print(naber)  # naber iyi misin?

# String indexleme ve Parcalama
x = "irem"
print(x[1])  # r
print(x[0])  # i
y = "iremi cok seviyorum"
print(len(y))  # 19
print(y[0:5])  # iremi
print(y[3:19])  # mi cok seviyorum
print(y[::3])  # imc vom Bastan 3 er atlaya atlaya stringi al
print(y[0:19:2])  # ieicksvyrm 0 dan 19 a 2 ser atlayarak stringi al

a = "iremi"
b = "cok"
c = "seviyorum"
print(a + b + c)  # iremicokseviyorum ?? ayrilmadi
print(c * 3)  # seviyorumseviyorumseviyorum
print(a, b, c)  # iremi cok seviyorum
print("iremi", "cok", "seviyorum")  # iremi cok seviyorum

# Data Type Transformations

a = 42
a = float(a)
print(a)  # 42.0
float(-1)
c = 42.3
c = int(c)  # Float'i integer'a
print(c)  # 42
d = 345
d = str(d)  # Int'i String'e
print(d)  # 345
print(len(d))  # 3
a = str(3.14)
print(len(a))  # 4 icindeki nokta bile string e dondu

# Stringi integer'a

a = "3144234"
b = int(a)
print(b)  # 3144234
a = "3.142324"
"""
c=int(a) # invalid literal for int() with base 10: '3.142324'
"""
c = float(a)
print(c)  # 3.142324

##################################################################

"""
Print icinde 
\n kullanirsak alt satirdan isleme devam eder 
\t kullanilirsa bir tab bosluk birakarak devam eder
"""
print("yakisiyomu\nlan\ntop")  # Yakisiyomu;lan;top
print("yakisiyomu\tlan\ttop")  # yakisiyomu	lan	top
print("yakisiyomu\t\t\t\t\t\tlan")  # yakisiyomu						lan

"""
type() fonksiyonu  icine gonderilen verinin hangi veri tipinde oldugunu soyle 
"""
# Integer (Tamsayı) türü
a = 65
print(type(a))

# Float (Ondalıklı Sayı) türü
a = 5.87
print(type(a))

# String (Karakter Dizisi) türü
a = "Murat"
print(type(a))

"""
print() fonksiyonunda kullanılabilen sep parametresi yazdırdığımız 
değerlerin arasına istediğimiz karakterlerin 
yerleştirilmesini sağlar. Eğer bu parametreyi kullanmazsak değerlerin arasına varsayılan 
olarak boşluk yerleştirildiğini biliyoruz

"""
print(12, 9, 1998)  # 12 9 1998
print(12, 9, 1998, sep="/")  # 12/9/1998
print(12, 9, 1998, sep="\n")  # 12 ; 9 ; 1998

# * li parametlereler
print("T", "B", "M", "M")
print(*"TBMM")  # T B M M
print(*"TMBB", sep=".")  # T.B.M.M

#######     STRINGLERDE FORMATLAMA     ######
# format() fonksiyonu
a = 3
b = 4
print("{} + {}'nin toplami {}'dir.".format(a, b, a + b))

# arabanin plakasini yazdiralim
print("{2} {0} {1}".format("BAE", 227, "06"))  # 06 BAE 227
# yani suslu parantezin icindeki sayi formatta indexlerden secim yapiyor
# 0 1 2 indexleri icinde mesela 1 icin 227 0 icin BAE

#######             LISTS             ########################

# Liste olusturma
liste = [3, 4, 5, 6, "Yusuf", 3.14, 5, 232]
print(liste)  # [3, 4, 5, 6, 'Yusuf', 3.14, 5, 232]
bos_liste = []
# bos liste
bos_liste = list()
print(bos_liste)  # []

s = "merhaba"
lst = list(s)
print(lst)  # ['m', 'e', 'r', 'h', 'a', 'b', 'a'] liste bu sekildede olusturulabilir

# Listeleri indexleme'
a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(a))  # 9
print(a[3])  # 5
print(a[-1])  # 10
print(a[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2]

# Temel liste metotlari ve islemleri
liste1 = [1, 2, 3, 4, 5]
liste2 = [6, 7, 8, 9, 10]
print(liste1 + liste2)  # [1,2,3,4,5,6,7,8,9,10]
name = ["irem"]
print(liste1 + name)  # [1,2,3,4,5 , 'irem']

print(liste1 + ["Yusuf"])  # [1, 2, 3, 4, 5, 'Yusuf']

#######################################################
lst = [1, 2, 3, 4, 5]
lst[0] = 12
print(lst)  # [12,2,3,4,5] gibi istedigimiz index i degistirebiliyoruz

print(lst * 3)  # [12, 2, 3, 4, 5, 12, 2, 3, 4, 5, 12, 2, 3, 4, 5]

# append() metodu
# bu sekilde yazdigimiz halde son indexin pesine ekleme yapar
liste22 = [1, 2, 3]
liste22.append("Yusuf")
print(liste22)  # [1, 2, 3, 'Yusuf']

# pop() metodu
liste = [1, 2, 3]
liste.pop(0)
print((liste))  # [ 2 ,3 ]

# sort() Metodu
lst23 = [23, 42, 51, 2, 3, 44]
lst23.sort()
print(lst23)  # [2, 3, 23,42,44,51] kucukten buyuge siraladik

lst24 = ["ahmet", 'ceylan', 'yusuf', 'deniz']
lst24.sort()
print(lst24)  # ['ahmet', 'ceylan', 'deniz', 'yusuf'] alfabetik olarak siraladi
lst24 = ["ahmet", 'ceylan', 'yusuf', 'deniz']
lst24.sort(reverse=True)
print(lst24)  # ['yusuf', 'deniz', 'ceylan', 'ahmet'] terse cevirdik

# liste ekleme
lst1 = [1, 2, 3, 4]
lst2 = [4, 5, 6, 7]
lst3 = [8, 9, 10, 11]
yeni_liste = [lst1 + lst2 + lst3]
print(yeni_liste)  # [[1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11]]
#  LISTE ICINDE LISTELER

lst4 = [[2, 4], [1, 3], [6, 5]]  # 3e ulasmak istiyoruz
print(lst4[1])  # [1 3]
print(lst4[1][1])  # 3

###########   Tuples   ##############
# listlere oldukça benzer ancak farkları tuple larin değiştirilemez oluşudur.

demet = (1, 2, 3, 4, 5)
print(demet)  # (1, 2, 3, 4, 5)
print(demet[1])  # 2
print(type(demet))  # <class 'tuple'>

tuple = (1, 2, 3, 4, 2, 1, 2, 2, 2, "yusuf", "erdem")
print(tuple.index("yusuf"))  # 9
# tuple.remove("erdem")  AttributeError: 'tuple' object has no attribute 'remove'
print(tuple.count(2))  # 5
print(tuple.count("yusuf"))  # 1

##############   DICTIONARYS    ###############


sozluk1 = {"bir": 1, "iki": 2, "Dort": 4}
sozluk2 = {}  # bos sozluk olusturduk , veya
sozluk3 = dict()
print(sozluk3)  # {}
print(sozluk1)  # {'bir': 1, 'iki': 2, 'Dort': 4}
print(sozluk1["bir"])  # 1
"""
print(sozluk1["bes"]) # Key Error
"""
sozluk1["bes"] = 5
print(sozluk1)  # {'bir': 1, 'iki': 2, 'Dort': 4, 'bes': 5}

liste4 = {"bir": [1, 2, 3, 4], "iki": [[1, 2], [3, 4], [5, 6]], "uc": 15}
print(liste4["iki"])  # [[1, 2], [3, 4], [5, 6]]
# yukaradaki iki numarali sozlukten [3,4] un icindeki 4 e erismek istiyoruz
print(liste4["iki"][1])  # [3 ,4]
print(liste4["iki"][1][1])  # 4
sozluk5 = {"bir": 1, "iki": 2, "uc": 3}
sozluk5["uc"] = 10
print(sozluk5)  # {'bir': 1, 'iki': 2, 'uc': 10}  istedigimiz degeri degistirebiliyoruz
sozluk5["uc"] += 1
print(sozluk5["uc"])  # 11

# Ic Ice Sozlukler

a = {"sayilar": {"bir": 1, "iki": 2, "üç": 3}, "meyveler": {"kiraz": "yaz", "portakal": "kış", "erik": "yaz"}}
print(a["sayilar"])  # {'bir': 1, 'iki': 2, 'üç': 3}
print(a["sayilar"]["iki"])  # 2
print(a["meyveler"]["kiraz"])  # yaz

# keys()
print(sozluk1.keys())  # dict_keys(['bir', 'iki', 'Dort', 'bes'])

# values()
print(sozluk1.values())  # dict_values([1, 2, 4, 5])

# items()
print(sozluk1.items())  # dict_items([('bir', 1), ('iki', 2), ('Dort', 4), ('bes', 5)]) Tupple olarak verdi

# ilerdeki bir ornek icin deneme

for k, v in sozluk1.items():
    print(k, v)  # bir 1 ; iki ;2 ;Dort 4 ;bes 5

############## Kullanıcıdan Girdi Alma - input() Fonksiyonu #############


input("lutfen bir sayi giriniz:")  # In: 42 out:'42'
# iyide biz bu input fonksiyonundan gelen degeri nasil yakaliycaz yani kullanicidan gelen degeri?
# bir degiskene atayabiliriz

a =input("lutfen sayi gir ")

print("girdiginiz sayi:", a)
# in:22 out:Girdiginiz Sayi 22

b=input("Bir sayi giriniz")
print(b*3)  # in:22 out:222222
#cunku
print(type(b))  # <class 'str'>

#Peki Bunu Nasil Integer a ceviricez?

b=int(input("lutfen bir sayi giriniz"))
print(b*3)  # in:22 out :66


#Kullanicidan 3 tane sayi alalim bunlari toplayan bir program yazalim.
x=int(input("1.sayi"))  # 10
y=int(input("2.sayi"))  # 20
z=int(input("3.sayi"))  # 30
print(x+y+z)  # 60

# Peki Kullanici biz int istedik yanlis bir input girdi ?
a=int(input("a"))  # in:42sads out: ValueError: invalid literal for int() with base 10: '31sdsd'

# o halde

try:
    a=int(input("a:"))
    print(a)
except ValueError:
    print("Lutfen dogru bir Input giriniz.")

    # in:2323123sadsad out:Lutfen dogru bir Unput giriniz.

# Ismimizi yazdiralim.

isim=input("isminizi giriniz:")
print("isminiz",isim,"!")  # in:yusuf out:isminiz yusuf # !






