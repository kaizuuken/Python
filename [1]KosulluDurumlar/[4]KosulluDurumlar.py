# Mantiksal Degerler (Boolean)
"""
Boolean degerler aslinda Pytonda bir veri tipidir ve iki degere sahiplerdir
True , false

"""
a = True
print(type(a))  # <class 'bool'>
b = False
print(type(b))  # <class 'bool'>

"""
Pythonda bir sayı değeri eğer 0'dan farklıysa True, 0 ise False olarak anlam kazanır. 
Bunu bool() fonksiyonuyla dönüştürme yaparak görebiliriz.
"""

print(bool(12.4))  # True
print(bool(0))  # False

print(1 == 1)  # True
print(1 == 2)  # False

# Ayrıca Pythonda eğer bir değişkenin değerini sonradan belirlemek isterseniz geçici
# olarak bu değişken None (atanmamış anlamında) değerine eşitleyebilirsiniz

a = None
print(a)  # None

"""
####  Karsilastirma Operatorleri  ####
== Esit ise True Degil ise False
!= Esit degil ise True esit ise False
> Sol sagdan buyuk ise True
< Sol sagdan Kucuk ise True Buyuk ise False
>= Sol Sagdan Buyuk esit ise True degil Ise false
<= Sol sagdan kucuk esit ise True degil ise False

"""

print("mehmet" == "mehmet")  # True
print("mehmet" != "mehmet")  # False
print("ahmet" < "burak")  # True "Alfabetik olarak bakar )
print(42 <= 42)  # True

##### Mantiksal Baglaclar #####

# and Operatoru

"""Bu mantıksal bağlaç, bütün karşılaştırma işlemlerinin sonucunun True olmasına bakar. 
Bağlanan karşılaştırma işlemlerinin  hepsinin kendi içinde sonucu True ise genel sonuç True ,
diğer durumlarda ise sonuç False çıkar. Kullanımı şu şekildedir.
"""

print("a" == "a" and 4 < 8)  # True
print("Yusuf" != "irem" and 2 == 3)  # false
print("Yusuf" == "yusuf")  # False  (buyuk kucuk harf onemli)

# or Operatoru
"""Bu mantıksal bağlaç, bütün karşılaştırma işlemlerinin sonuçlarından en az birinin True olmasına bakar. 
Bağlanan karşılaştırma işlemlerinin en az birinin True olmasında genel sonuç True , 
diğer durumlarda ise sonuç False çıkar. Kullanımı şu şekildedir."""

print(1 < 2 or 1 == 3)  # True
print(12 == 13 or 13 == 14)  # False

# not Operatoru
"""not operatörü aslında bir mantıksal bağlaç değildir. Bu operatör sadece bir mantıksal değeri veya karşılaştırma 
işlemininin tam tersi sonuca çevirir. Yani, not operatörü True olan bir sonucu False , 
False olan bir sonucu True sonucuna çevirir. Kullanımı şu şekildedir."""

print(not 2 == 2)  # False
print(not 1 == 2)  # True
print(not "Python" == "Php")  # True

# Operatorleri Beraber Kullanma.

print(not 2 == 2) or ("yusuf" == "irem")  # False
print(("Yusuf" == "Yusuf " and "ahmet" > "Yusuf") or 3.12 != 3.13)  # True

#######  Kosullu Blok Durumlari  #######

"""
Python Programlarinin Calisma Mantigi 
Python programlari calistirilmaya basladigi zaman kodlarimiz yukaridan baslayarak teker teker calistirilir 
calistirilacak kod kalmayinca programimiz sona erer.
/ornek olarak"""
a = 2
b = 3
c = 4
print(a + b + c)  # 9 olarak geri doner
"""Ancak Her Program bu kadar basit olmayabilir.
Çoğu zaman Python programlarımız belirli bloklardan oluşur ve bu bloklar her zaman çalışmak zorunda olmaz.
Peki bu bloklar nasıl tanımlanır ? Pythonda bir blok tanımlama işlemi Girintiler sayesinde olmaktadır.
 Örnek olması açısından, Pythonda bloklar şu şekilde oluşabilir"""

a = 2  # Blok 1 'e ait kod

if (a == 2):
    print(a)  # Blok 2'ye ait kod
print("Merhaba")  # Blok 1 ' ait kod   Out: 2;Merhaba

"""Dikkat ederseniz burada daha önce görmediğimiz bir şey yaptık ve if in bulunduğu satırdan sonraki print işlemini 
bir tab kadar girintili yazdık. Burada gördüğümüz gibi, girintiler(tab) Pythonda bir blok oluşturmak için kullanılıyor 
ve her bloğunun çalıştırılması gerekmiyor. Mesela yukarıda gördüğümüz kodda 2 print işlemi de çalıştı. 
Ancak kodumuzu şu şekilde yazsaydık, ilk print işlemi çalışmayacaktı.
"""

a = 2  # Blok 1 'e ait kod
if a == 3:
    print(a)  # Blok 2'ye ait kod
print("merhaba")  # Out: merhaba

# # # # # # # # Kosullu Durumlar # # # # # # # # # #

"""Koşullu durumlar aslında günlük yaşamda sürekli karşılaştığımız durumlardır.
Örneğin havanın yağmurlu olma koşuluna göre şemsiyemizi alırız veya uykumuzun gelme koşuluna göre uyuruz. 
Aslında programlamada da birçok koşullu durumla karşılaşırız. Örneğin , belli koşullara göre belli işlemleri yaparız ,
belli koşullara göre yapmayız. İşte bunlar koşullu durumların temeli oluşturur. 
İsterseniz koşullu durumları yazmaya if blokları ile başlayalım."""

# if Blogu

# if bloğu programımızın içinde herhangi bir yerde belli bir koşulu kontrol edecek isek kullanılan bloklardır.
# Yazımı şu şekildedir;
#
#        if (koşul):
#            # if bloğu - Koşul sağlanınca (True) çalışır. Bu hizadaki her işlem bu if bloğuna ait.
#            # if bloğu - Girintiyle oluşturulur.
#            Yapılacak İşlemler

# 18 Yas Kontrolu

yas = int(input("Yasinizi Giriniz:"))

if yas < 18:
    print("Mekana Giremezsiniz")  # In:17 Out:Mekana Giremezsiniz

# Negatif Mi degil mi ?

sayi = int(input("Sayi Giriniz:"))
if sayi < 0:
    print("Negatif Sayi")  # In : -3 Out : Negatif Sayi

# Ancak Burda bir sorun var Yasi 22 girersek Bir cikti Vermiyor veya sayiyi 3 girersek Bu durumda:

# else Blogu

"""else blokları if koşulu sağlanmadığı zaman (False) çalışan bloklardır. Kullanımı şu şekildedir;

       # else:
           # else bloğu - Yukarısındaki herhangi bir if bloğu (veya ilerde göreceğimiz elif bloğu) çalışmadığı
           # zaman çalışır.
           # else bloğu - Girintiyle oluşturulur.
               #Yapılacak İşlemler"""

# 18 Yas Kontrolu

yasi = int(input("Yasinizi Girisiniz:"))

if yasi < 18:
    print("Mekana Giremezsiniz :/")
else:
    print("Mekana Hosgeldiniz!")  # In : 21 Out:Mekana Hosgeldiniz! In : 17 Out: Mekana Giremezsiniz

#--------------

"""else:
    print("Merhaba")
  File "<ipython-input-15-9fdf2315e01a>", line 1
    else:
       ^
#SyntaxError: invalid syntax
#Buradaki kod hata verdi çünkü bir else bloğu kendinden önce herhangi bir koşul bloğu yok ise çalışamaz 
ve Pythonda hataya yol açar."""

# # # # # if-elif-else Blokları # # # # # #

""" 
if koşul: 
               Yapılacak İşlemler
           elif başka bir koşul:
               Yapılacak İşlemler
           elif başka bir koşul:
               Yapılacak İşlemler

                //
                //
           else:
               Yapılacak İşlemler 
               
Programlarımızda, Kaç tane koşulumuz var ise o kadar elif bloğu oluşturabiliriz. Ayrıca else in yazılması zorunlu
değildir. if - elif - else kalıplarında, hangi koşul sağlanırsa program o bloğu çalıştırır ve if-elif-blokları
sona erer. Şimdi isterseniz kullanıcıya işlem seçtirdiğimiz bir programla , bu kalıbı öğrenmeye başlayalım.
"""

islem=int(input("Islem Seciniz:")) # 3 tane Islemimiz olsun
if islem==1:
    print("1. Islem Secildi.")
elif islem ==2:
    print("2. Islemi Secildi.")
elif islem ==3:
    print("3. Islem Secildi.")
else:
    print("Gecersiz Islem.")  # In: 4 Out : Gecersiz Islem

# # # if-if-if Bloklari # # #

# Bu blokları öğrenmeden önce isterseniz öğrendiğimiz bilgilerle, bir harf notu hesaplama sistemi yapalım.
# Daha sonra bu kalıpları anlamaya çalışalım.
note = float(input("Notunuzu giriniz:"))

if note >= 90:
    print("AA")
elif note >= 85:
    print("BA")
elif note >= 90:
    print("BA")
elif note >= 80:
    print("BB")
elif note >= 75:
    print("CB")
elif note >= 70:
    print("CC")
elif note >= 65:
    print("DC")
elif note >= 60:
    print("DD")
else:
    print("Dersten Kaldınız")


# --------------------------------------------------
note = float(input("Notunuzu giriniz:"))

if note >= 90:
    print("AA")
if note >= 85:
    print("BA")
if note >= 90:
    print("BA")
if note >= 80:
    print("BB")
if note >= 75:
    print("CB")
if note >= 70:
    print("CC")
if note >= 65:
    print("DC")
if note >= 60:
    print("DD")
else:
    print("Dersten Kaldınız") # In : 80 Out : BB ;CB; CC; DC; DD;  Hepsini Calistirmis oldu.
                              # Sira ile Bu Yuzden elif kullaniyoruz.




