# Methods - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""Metodlar bir obje üzerinde belli işlemleri gerçekleştiren objelere özgü fonksiyonlardır ve
objelerin üzerinde metodlar şu şekilde kullanılır."""

liste = [1, 2, 3, 4, 5]
liste.insert(1, 'Yusuf')
print(liste)  # [1, 'Yusuf', 2, 3, 4, 5] Vurgulden sonraki elemanin pesine girdigimiz degeri ekledi.
liste.pop()
print(liste)  # [1, 'Yusuf', 2, 3, 4] son elemani cikartti

liste.append("Python")
print(liste)  # [1, 'Yusuf', 2, 3, 4, 'Python']

"""fonksiyonlar programlamada belli işlevleri olan ve tekrar tekrar kullandığımız yapılardır. Örneğin kursumuzun 
başlarından beri kullandığımız print() fonksiyonunun görevi içine gönderdiğimiz değerleri ekrana yazdırdırmaktır. 
Bu fonksiyon Python geliştiricileri tarafından bir defa yazılmış ve biz de bu fonksiyonu programlarımızın değişik 
yerlerinde tekrar tekrar kullanıyoruz. İşte fonksiyonların kullanım amacı tam olarak budur. Fonksiyonlar bir defa 
tanımlanır ve programlarda ihtiyacımız olduğu zaman kullanırız. Ayrıca fonksiyonlar kod tekrarını engeller ve kodlarımız
daha derli toplu durur.

İsterseniz şimdi de fonksiyonların ne olduğunu gerçek hayattan benzetme yaparak anlamaya çalışalım. 
Örneğin evimize bir adet katı meyve sıkacağı alıyoruz ve canımız ne zaman meyve suyu isterse bu aleti kullanıyoruz. 
Yani aslında bu aletin görevi ve fonksiyonu meyve suyu hazırlamaktır.

Python geliştiricilerin yazdığı fonksiyonlara yani bizim hazır kullandığımız fonksiyonlara(print(),type() vs.) gömülü 
fonksiyonlar(built-in function) denilmektedir.Ancak bunlardan hariç olarak biz kendi özel fonksiyonlarımızı
(user-defined functions) da tanımlayabiliriz."""

# Fonksiyonların Tanımlanması

"""Fonksiyon tanımlamanın yapısı şu şekildedir;

        def fonksiyon_adı(parametre1,parametre2..... (opsiyonel)):
            # Fonksiyon bloğu
            Yapılacak işlemler
            # dönüş değeri - Opsiyonel
"""


# Bir selamlama Fonksiyonu tanimlayalim

def selamla():
    print("Selamin Aleykum")
    print("Naptin?")


print(type(selamla))  # <class 'function'>

print(selamla())  # Selamin Aleykum
                  # Naptin?

# Parametreler ve Argümanlar

"""Biliyorsunuz biz selamla fonksiyonunun içine herhangi bir değer göndermiyorduk ve fonksiyonumuz hep aynı işi
yapıyordu. Ancak çoğu zaman fonksiyonlarımız içine gönderdiğimiz değerlerle farklı işlemler yaparlar. Örneğin katı 
meyve sıkacağına eğer "Elma" verirsek elma suyu, "Nar" verirsek nar suyu hazırlayacaktır. Fonksiyonlarda da 
Parametreleri bu şekilde düşünebilirsiniz. İsterseniz şimdi selamlama fonksiyonumuzu bir tane parametre alacak şekilde 
tanımlayalım."""

def selamla(isim):
    print("Merhaba,",isim)

selamla("Yusuf")  #Merhaba, Yusuf

"""Bizim fonksiyon tanımlarken tanımladığımız herbir değişken birer Parametre , fonksiyon çağrısı yaptığımız zaman içine 
gönderdiğimiz değerler ise Argüman olmaktadır. Burada fonksiyonu çağırırken gönderdiğimiz "Kemal" değeri "isim" isimli 
parametreye eşit oluyor ve fonksiyonumuz bu değere göre işlem yapıyor. "Ayşe" değerini gönderdiğimizde ise fonksiyonumuz
bu değere göre işlem yaparak ekrana farklı bir değer yazdırıyor. Şimdi isterseniz farklı bir fonksiyon tanımlayalım ve 
3 tane parametre alsın.
"""
# Toplama Fonksiyonu

def toplama(a,b,c):
    print("toplamlari:",a+b+c)

toplama(2,3,4) # 9

# Faktoriyel Hesaplama Fonksiyonu

def faktoriyel(sayi):
    faktoriyel=1
    if sayi == 1 or sayi == 0:
        print("esittir:",faktoriyel)
    else:
        while sayi>=1:
            faktoriyel*=sayi
            sayi-=1
        print("Faktoriyel = {}.".format(faktoriyel))


faktoriyel(4)  # 40320

# Fonksiyonlarda Return. #---------------------------------------------

"""Önceki bölümde yazdığımız fonksiyonları hatırlayacak olursak, bu fonksiyonlar sadece ekrana print ile değer 
yazdırıyordu. Ancak bu fonksiyonlar yaptıklar işlemler bize herhangi bir değer vermiyorlardı. Ancak biz programlarımızda
 bir fonksiyon sonucunda elde edilen değerleri alıp programlarımızın bambaşka yerlerinde kullanmak isteyebiliriz. Bu 
 derste bunu nasıl yapacağımızı öğrenmeye çalışacağız.

return ifadesi fonksiyonun işlemi bittikten sonra çağrıldığı yere değer döndürmesi anlamı taşır. 
Böylelikle, fonksiyonda aldığımız değeri bir değişkende depolayabilir ve değeri programın başka yerlerinde
 kullanabiliriz. Şimdi iki tane çok basit fonksiyon yazalım ve return neden gereklidir anlamaya çalışalım."""

"""
def toplam(a,b,c):
    print("Toplamlari:",a+b+c)
def ikiylecarp(a):
    print("Ikiyle Carpilmis Halleri:",a*2)

toplam = toplam(2,3,4)
ikiylecarp(toplam)

TypeError                                 Traceback (most recent call last)
<ipython-input-11-da4bfe0bd65f> in <module>()
      1 toplam = toplama(3,4,5)
      2 
----> 3 ikiyleçarp(toplam)

<ipython-input-10-5128afde7d6b> in ikiyleçarp(a)
      3 
      4 def ikiyleçarp(a): # İkinci fonksiyon
----> 5     print("2 ile çarpılmış hali", a * 2)
      6 

TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
Burada hata almamızın sebebi fonksiyonları herhangi bir değer döndürmemesi yani return kullanmamasıdır. 
İsterseniz toplam değişkeninin tipine bakalim
"""
# print(type(toplam))  # NoneType

def toplama(a,b,c):
    return a+b+c
def ikiylecarp(a):
    return a*2
toplam=toplama(2,3,4)
print(ikiylecarp(toplam)) # 18

# ------------------------------------------------------------------

def kareal(a):
    print("1. Fonksiyon Calisti.")
    return a**2
def ikiylecarp(a):
    print("2. Fonksiyon Calisti.")
    return a*2
def dordebol(a):
    print("3. Fonksiyon Calisti.")
    return a/4

#Ucunu birlikte Calistiralim

print(dordebol(ikiylecarp(kareal(2))))

"""
Out: 
1. Fonksiyon Calisti.
2. Fonksiyon Calisti.
3. Fonksiyon Calisti.
2.0
"""

# return ifadesinden sonra fonksiyonumuz tamamıyla sona erer. Yani, return ifadesinden sonra yapılan herhangi
# bir işlem çalıştırılmaz.

# Parametrelerin Varsayilan Degerleri

def selamla(isim):
    print("Merhaba",isim)

selamla("Yusuf") # Merbaba Yusuf

# selamla() Bu kullanim hata Veriyor. Ancak biz eğer bir parametrenin değerini varsayılan olarak belirlemek istersek,
# bunu varsayılan değerler ile yapabiliriz. Varsayılan değerleri anlamak için selamla fonksiyonunu ,
# varsayılan parametre değeri ile yazalım.

def selamla(isim="Isimsiz"):
    print("Merhaba",isim)
selamla() # Merhaba Isimsiz
selamla("Yusuf") # Merhaba Yusuf

# Peki birçok parametreye sahip olursak ne olacak ?

def ogrenci_bilgileri(ad="Bilgi yok",soyad="Bilgi Yok",numara="Bilgi Yok"):
    print("Ad:",ad,"soyad:",soyad,"Numara",numara)

ogrenci_bilgileri() #Ad: Bilgi yok soyad: Bilgi Yok Numara Bilgi Yok
ogrenci_bilgileri("yusuf","erdem") # Ad: yusuf soyad: erdem Numara Bilgi Yok
# Fakat bunlar sirali olarak yazdigimiz icin calisti fakat sadece numarayi vermek istersek?
ogrenci_bilgileri(numara="5539665664") # Ad: Bilgi yok soyad: Bilgi Yok Numara 5539665664

print("Yusuf","Erdem") # Yusuf Erdem # Varsayilan olarak bosluk birakti
print("yusuf","erdem",sep="/") # yusuf/erdem

# Esnek Sayida Degerler

# Simdilik Fonksiyon yazildiginda ozel olarak kac tane parametresi olacagini onceden belirtmemiz gerekiyor
"""Ornegin
def toplama(a,b,c):
    print(a,b,c)

toplama(2,3,4,5) # 4 deger giremeyiz

"""

#Peki ben bir fonksiyonu esnek sayıda argümanla kullanmak istersem ne yapacağım ? Bunun için de Yıldızlı Parametre
# kullanmam gerekiyor. Kullanımı şu şekildedir;

def toplama(*parametreler):
    print(parametreler)

toplama(2,3,4,5,6,7) # (2, 3, 4, 5, 6, 7) bana tuple olarak dondurdu. o Zaman bunlari for donguleri ile toplayabiliriz

# --------------------------------------------------------------------------------------------------------------------
def toplama(*parametreler):
    toplam=0
    for i in parametreler:
        toplam+=i
    print(toplam)
toplama(2,3,4,5,6,7,8) # 35

# print fonksiyonunu tekrar hatırlayacak olursak aslında print fonksiyonu bu şekilde tanımlanmış bir fonksiyondur.
# Çünkü biz print fonksiyonuna istediğimiz sayıda argüman gönderebiliyorduk.

print(3,4,5,6,7) # 3 4 5 6 7


# Global Ve Local Degiskenler

"""Pythonda fonksiyonlarda tanımlanan değişkenler Python tarafından Yerel (Local) değişkenler olarak tanımlanırlar.Yani 
bir fonksiyon bloğunda oluşturulan değişkenler fonksiyona özgüdür ve fonksiyon çalışmasını bitirdikten sonra bu değişken
ler bellekten silinir ve yok olur. Böylelikle , fonksiyon içinde tanımlanmış bir değişkene başka bir yerden erişilemez.

Pythonda en genel kapsama sahip değişkenler ise Global değişkenler olarak tanımlanırlar ve global değişkenlere
 tanımlandığı andan itibaren programın her yerinden ulaşabiliriz.

Yerel değişkenleri anlamak için bir tane fonksiyon tanımlayalım."""

def fonsiyon():
    a=10
    print(a)

fonsiyon()  # 10
# print(a) # a degiskeni yok oldu. NameError: name 'a' is not defined

# Burada fonksiyon içinde tanımlanan a değişkeni fonksiyon çağrıldığında bellekte oluşur ve fonksiyon bloğunu çalıştırdı
# -ktan sonra yok olur. Yani, a değişkeni burada bir yerel değişkendir.

# Peki Global Degiskenler?

a=5
def fonsiyon():
    print(a)

fonsiyon() # 5
print(a)   # 5

# ----------------------------------
c = 10 # Globalde tanımlanmış bir değişken
def fonksiyon():
    c = 2 # Yerelde tanımlanmış bir değişken
    print(c)  # Yerel değişken kullanılıyor.

fonksiyon() # 2
print(c)    #10

"""Kodumuz çalıştığında ilk olarak c isimli global değişken oluşuyor. fonksiyon çağrıldığında ise c isimli başka bir 
yerel değişken oluşuyor gibi düşünebilirsiniz. Böyle bir durumda elimizden iki tane c değişkeni var. Python bu durumda 
global c değişkeni yerine kendi yerel c değişkenini kullanıyor."""

# Peki globaldakini nasil kullaniriz?
d = 10


def fonksiyon():
    global d

    d = 4
    print(d)

fonksiyon()  # 4
print(d)     # 4

# Peki bir if veya while bloğunda yerel bir değişken tanımlanır mı hemen bakalım.

if True:
    t=10
    print(t) # 10

print(t)  # 10 Globade tanimladi

while True:
    deger=10
    print(deger)
    break    # 10

print(deger)  # 10 Burada gördüğümüz gibi, if ve while bloklarında tanımlanan değişkenler yerel bir değişken yerine
# global bir değişken olmaktadır.

# Lambda Ifadeleri ( EXPRESSTION )

"""mbda ifadeleri fonksiyonlarımızı oluşturmak için Pythonda bulunan pratik bir yöntemdir ve gerektiği yerlerde bu 
ifadeleri kullanabiliriz. Biliyorsunuz listelerimizi oluşturmak için List Comprehension yöntemini kullanabiliyorduk. 
List Comprehension yöntemini hatırlayalım."""

liste1=[1,2,3,4,5]
liste2=[]
for i in liste1:
    liste2.append(i*2)
print(liste2) # [2,4,6,8,10]

# List Comprehension ile...

liste3=[2,3,4,5,6]
liste4=[i * 2 for i in liste3]
print(liste4)  # [4, 6, 8, 10, 12]

"""Aynı buradaki gibi bir fonksiyonu da tek satır halinde lambda ifadeleriyle oluşturabiliriz. 
İlk önce yapısına bakalım sonra örneklerimize geçelim.

                etiket = lambda parametre1,parametre2.... :  İşlem"""

def ikiylecarp(x):
    return x*2
print(ikiylecarp(2)) # 4

#Lambda Ile?

ikiylecarp1= lambda x :x*2 # # x parametre x* 2 return ifadesi ve ikiyleçarp değeri de bir etikettir(değişken gibi)
print(ikiylecarp1(3)) # 6

# ------------------------------------------------------------------------------------------------------------------

def toplama(a,b,c):
    return a+b+c

print(toplama(1,2,3)) # 6

# Lambda ile

toplama1=lambda a,b,c: a+b+c
print(toplama1(1,2,3)) # 6

# Stringi ters çevirme

def terscevir(s):
    return s[::-1]
print(terscevir("Python Programlama Dili")) # iliD amalmargorP nohtyP

# Lambda ile

ters=lambda s :s[::-1]
print(ters("Yusuf Erdem")) # medrE fusuY

s="Python"
print(ters(s))  # nohtyP

# --------------------------------------------------------------------------------------

def cifmi(x):
    return (x%2 == 0)
print(cifmi(7))  # False
print(cifmi(8))  # True

# Lambda ile :

cifttek=lambda x : x%2 == 0

print(cifttek(13)) # False


#İşte lambda ifadesini bu şekilde küçük fonksiyonlar için kullanabiliriz. lambda ifadelerini özellikle kısa bir
# fonksiyonu def ifadesiyle yazmanın zahmetli olduğu zamanlarda kullanılabilir.





