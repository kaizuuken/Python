# # # # # # # Dongu Yapilarini Kullanma # # # # # # # #
"""Şimdiye kadar yazdığımız programlarda yazdığımız programlar bir defa çalışıyor ve sona eriyordu. Ancak biz çoğu zaman
 programlarımızın belli koşullarda çalışmasını sürekli devam ettirmesini ve işlemlerini tekrar etmesini isteriz. İşte
  bunları yapmamızı sağlayan yapılara döngü diyoruz.

Döngüler bütün programlama dillerinde bulunan ve belli koşullarda işlemlerini sürekli tekrar eden yapılardır.
İsterseniz gerçek hayattaki programlara bakarak döngü mantığını anlamaya çalışalım.

Örneğin , siz ATM makinesine gidip kartınızı yerleştiriyorsunuz ve program başlıyor. Para Çekme, Para Yatırma ,
Vergileri Ödeme gibi işlemleri tekrar tekrar gerçekleştiriyorsunuz. Programın sona ermesi ise Kart İade seçeneği ile
gerçekleşiyor. Yani siz Kart İade tuşuna basmadığınız sürece ATM makinesi çalışmaya devam ediyor. Buna bakarak ,
aslında ATM makinesi döngü yapılarını kullanıyor diyebiliriz.

Başka bir örnek düşünelim. Örneğin siz bir siteye login olma işlemi gerçekleştiriyorsunuz. Biz kullanıcı adı ve
parolayı yanlış girdiğimiz sürece program sürekli bize kullanıcı adı ve parola soruyor. Programın sona ermesi ise biz
kullanıcı adı ve parolayı doğru girdiğimizde gerçekleşiyor. Yine burada da siz döngü yapılarının kullanıldığını
düşünebilirsiniz.

Biz de artık bu bölümle birlikte Pythondaki while ve for döngülerini kullanarak programlarımızı
daha efektif bir şekilde yazabileceğiz."""

# ------For Donguleri------#

# in Operatöru

# Pythondaki in operatörü , bir elemanın başka bir listede,demette veya stringte (karakter dizileri)
# bulunup bulunmadığını kontrol eder. Kullanımı şu şekildedir;

print("a" in "Merhaba")  # True
print("mer" in "merhaba")  # True
print("t" in "merhaba")  # False
print(4 in [1, 2, 3, 4])  # True
print(not 4 in [1, 2, 3, 4])  # false

# for Döngüsü

"""for Döngüsü , listelerin ,demetlerin, stringlerin ve hatta sözlüklerin 
üzerinde dolaşmamızı sağlayan bir döngü türüdür. Yapısı şu şekildedir.

 for eleman in veri_yapısı(liste,demet vs):
            Yapılacak İşlemler
Bu yapı bize şunu söyler;

        eleman değişkeni her döngünün başında listenin,demetin vs. her bir elemanına eşit olacak ve her döngüde 
        bu elemanla işlem yapılacak.
for döngüsünü daha iyi anlamak için örneklerimize bakalım.
"""
# Listeler Uzerinde Gezinmek

liste = [1, 2, 3, 4, 5, 6, 7]

for eleman in liste:
    print(eleman)  # 1;2;3;4;5;6;7

# Liste Elemanlarini Toplamak

toplam = 0
liste = [1, 2, 3, 4, 5, 6, 7]
for eleman in liste:
    toplam = toplam + eleman
    print("toplam", toplam)  # toplam 28

toplam = 0
liste = [1, 2, 3, 4, 5]

for eleman in liste:
    toplam = toplam + eleman
    print("Toplam: {} , Eleman: {} ".format(toplam, eleman))
"""Out:
Toplam: 1 , Eleman: 1 
Toplam: 3 , Eleman: 2 
Toplam: 6 , Eleman: 3 
Toplam: 10 , Eleman: 4 
Toplam: 15 , Eleman: 5 
"""

# Cift Sayilari Bastirma

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lst:
    if i % 2 == 0:
        print(i)  # Out:2;4;6;8;10
# ---------------------------------------------
s = "Python".upper()

for i in s:
    print(i)  # P;Y;T;H;O;N
# ---------------------------------------------

for i in s:
    print(i * 3)  # Out: PPP;YYY;TTT;HHHH;OOO;NNN

# - - - - - - - - - - - - - - - - - - - - - - - - - -
demet = (1, 2, 3, 4, 5, 6)

for i in demet:
    print(i)  # 1 ; 2 ; 3 ; 4 ; 5 ; 6

# - - - - - - - - - - - - - - - - - - - - - - - - -
# Demetler Uzerinde Uygulanabilen For Dongusunde Cok Pratik Bir Yontem Bulunuyor.
liste = [(1, 2), (3, 4), (5, 6)]

for i in liste:
    print(i)
"""  
    Out: (1, 2)
         (3, 4)
         (5, 6) 
"""

# Demet içindeki herbir elemanı almak için pratik yöntem
liste = [(1, 2), (3, 4), (5, 6), (7, 8)]

for (i, j) in liste:
    print(i, j)  # out : 1 2 ; 3 4 ; 5 6 ; 7 8

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
liste = [(1, 2), (3, 4), (5, 6), (7, 8)]

for i, j in liste:
    print("i: {} , j: {}".format(i, j))

"""Out: 
i: 1 , j: 2
i: 3 , j: 4
i: 5 , j: 6
i: 7 , j: 8
"""

# Demet içindeki elemanları yazdiralim
liste = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]

for i, j, k in liste:
    print(i, j, k)  # Out: 1 2 3 ; 4 5 6 ; 7 8 9 ; 10 11 12

# Demet Icindeki elemanlari Carptirma
liste = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
for i, j, k in liste:
    print(i * j * k)  # Out: 6 ; 120 ; 504 ; 1320

# Sozlukler Uzerinde Gezinmek

sozluk = {"bir": 1, "iki": 2, "üç": 3, "dört": 4}
print(sozluk.keys())  # dict_keys(['bir', 'iki', 'üç', 'dört'])
print(sozluk.values())  # dict_values([1, 2, 3, 4])
print(sozluk.items())  # dict_items([('bir', 1), ('iki', 2), ('üç', 3), ('dört', 4)])

# Metodları kullanmadan sözlük üzerinde gezinmek - Sadece anahtarları alabiliyoruz.
sozluk = {"bir": 1, "iki": 2, "üç": 3, "dört": 4}

for i in sozluk:
    print(i)  # bir ; iki ; uc ; dort

sozluk = {"bir": 1, "iki": 2, "üç": 3, "dört": 4}

for i in sozluk.keys():
    print(i)  # # bir ; iki ; uc ; dort

sozluk = {"bir": 1, "iki": 2, "üç": 3, "dört": 4}

for i in sozluk.values():
    print(i)  # 1 ;2 ;3; 4

sozluk = {"bir": 1, "iki": 2, "üç": 3, "dört": 4}

for i, j in sozluk.items():
    print("Anahtar :", i, "Deger", j)
"""" Out:
Anahtar : bir Deger 1
Anahtar : iki Deger 2
Anahtar : üç Deger 3
Anahtar : dört Deger 4"""

# Programın ciktisi nedir?


liste = [2, 1, 10, 2, 23, 1, 56, 3]

total = 0
for i in liste:
    if (not (i % 2 == 0)):
        total += i

print(total)

# While Donguleri

"""Bu bölümde while döngülerinin yapısını ve nasıl kullanılacağını öğrenmeye çalışacağız.

while döngüleri belli bir koşul sağlandığı sürece bloğundaki işlemleri gerçekleştirmeye devam eder. 
while döngülerinin sona ermesi için koşul durumunun bir süre sonra False olması gereklidir.Yapısı şu şekildedir;
while (koşul):
                                İşlem1
                                İşlem2
                                İşlem3
                                  //
                                  //
"""
# Döngüde i değerlerini ekrana yazdırma

i = 0
while i < 10:
    print("i'nin degeri:", i)
    i += 1  # i nin degeri:0i nin degeri:1;i nin degeri:2;i nin degeri:3;4i nin degeri:;i nin deger:5;i nin degeri:6
    # ;i nin degeri:i nin degeri:7;i nin degeri:8;i nin degeri:9

# i degerlerini yazdirma

i = 0
while i < 20:
    print(i)
    i = i + 2  # 0;2;4;6;8;10;12;14;16;18

# Ekrana 40 defa "Python Öğreniyorum" yazdıralım.
i = 0

while i < 40:
    print("Python Ogreniyorum.")
    i += 1  # Out:Python Ogreniyorum. x 40 (alt alta)

# Liste üzerinde indeks ile gezinme
# Once For dongusu ile gezinelim
liste = [1, 2, 3, 4, 5]
for i in liste:
    print(i)  # 1;2;3;4;5
# While Dongusu ile gezinelim

liste = [1, 2, 3, 4, 5]
indeks = 0
while indeks < len(liste):  # KOUSULUMUZ INDEX 5 DEN KUCUK OLDUGU SURECE
    print("indeks:", indeks, "eleman:", liste[indeks])
    indeks += 1
    """
indeks: 0 eleman: 1
indeks: 1 eleman: 2
indeks: 2 eleman: 3
indeks: 3 eleman: 4
indeks: 4 eleman: 5"""

# range() Fonksiyonu:

"""Pythondaki bu hazır fonksiyon bizim verdiğimiz değerlere göre range isimli bir yapı oluşturur ve bu yapı listelere
oldukça benzer. Bu yapı başlangıç, bitiş ve opsiyonel olarak artırma değeri alarak listelere benzeyen bir sayı dizisi 
oluşturur. Kullanımlarını öğrenmeye başlayalım."""

range(0, 20)  # 0'dan 20' a kadar (dahil değil) sayı dizisi oluşturur.
print(range(0, 20))  # range(0,20)
print(*range(0, 20))  # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 Basina * koyarsak calisir.

liste = list(range(0, 20))  # list komutu ile listeye donusturulebilir

print(liste)  # Out:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print(*range(5, 10))  # 5 6 7 8 9
print(*range(15))  # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 Baslangic degeri Vermessek 0 dan baslar.

# 2 ser atlayarak yazmasini istiyoruz?
print(*range(0, 10, 2))  # 0 2 4 6 8

print(*range(5, 100, 5))  # 5'ten 100'e kadar olan ve 5 ile bölünebilen sayılar
# out:5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95

print(*range(20, 0))  # 20'den geri gelen sayıları oluşturmaz.
print(*range(20, 0, -1))  # 20'den geri gelen sayıları oluşturur. Out:20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2
""" ilk girilen sayi dahil ikinci degil gibi anlasiliyor.!"""

# Şimdi de, range fonksiyonu ile oluşturduğumuz yapının üzerinde for döngüsü ile gezinelim.

for i in range(0, 5):
    print(i)  # 0 ; 1 ; 2 ; 3 ; 4

for sayi in range(10):
    print(sayi)  # 0;1;2;3;4;5;6;7;8;9

for i in range(1, 20):  # yildizi bir string olarak alip once 1 ile 2 ile 19 a kadar sira ile carpiyor.
    print("*" * i)
""""
*
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * * 
* * * * * * * * * * * * 
* * * * * * * * * * * * * 
* * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * """

# break ifadesi

"""break ifadesi döngülerde programcılar tarafından en çok kullanılan ifadedir. Anlamı şu şekildedir;

        Döngü herhangi bir yerde ve herhangi bir zamanda break ifadesiyle karşılaştığı zaman
        çalışmasını bir anda durdurur. Böylelikle döngü hiçbir koşula bağlı kalmadan sonlanmış olur."""

# break ifadesi sadece ve sadece içindeki bulunduğu döngüyü sonlandırır. Eğer iç içe döngüler bulunuyorsa ve en içteki
# döngüde break kullanılmışsa sadece içteki döngü sona erer. Örneklerle break ifadesini anlamaya çalışalım.

i = 0  # Bu donguyu biliyoruz.
while i < 20:
    print(i)
    i += 1
# ----------------------------------------------------------------------------------
i = 0
while i < 20:
    print(i)
    if i == 10:
        break  # i'nin değeri 10 olunca bu koşul sağlanıyor ve  break ifadesiyle karşılaşıldığı için döngü anında
        # sona eriyor.
    i += 1
    # Out: 1;2;3;4;5;6;7;8;9;10
# ---------------------------------------------------------------------------------

# For dongusu ile break kullanalim

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lst:
    if i == 5:
        break
    print("i:", i)  # i:1; i:2; i:3; i:4

# ---------------------------------------------------------------------------------

while True:
    isim = input("Isminizi Giriniz(CikmakIcin 'q' ya basiniz):")
    if isim == "q":
        print("Programdan Cikiliyor.")
        break
    print("Isminiz", isim)  # in;Yusuf out:isminiz Yusuf  , in: Yusuf Erdem out:isminiz Yusuf Erdem
    # in:q out: Programdan Cikiliyor...

# continue ifadesi

"""continue ifadesi
continue ifadesi break'e göre biraz daha az kullanılan bir ifadedir. Anlamı şu şekildedir;

    Döngü herhangi bir yerde ve herhangi bir zamanda continue ifadesiyle karşılaştığı zaman geri kalan işlemlerini
    yapmadan direk bloğunun başına döner.
"""

liste = list(range(11))
print(liste)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in liste:
    print("i:", i)
# -----------------------------------------------------------------
liste = list(range(11))
print(liste)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in liste:
    if i == 3 or i == 5:
        continue
    print("i:", i)  # out : i: 3 ve i:5  BASTIRILMADI

# ---------------------------------------------------------------

"""i=0
while i < 10:
    if i == 2:
        continue
    print(i)
    i+=1"""  # bu kodu calistirdigimiz zaman 0 i almaya basliyor 2 de islemleri atlayip tekrar artirma islemini
# yapamadigindan sonsuz donguye giriyor o yuzden arttirma islemini continue den once yapmaliyiz.

i = 0  # Kodun sorunsuz hali

while i < 10:

    if i == 2:
        i += 1  # Artırma işlemi
        continue

    print("i:", i)
    i += 1
"""out:
i: 0
i: 1
i: 3
i: 4
i: 5
i: 6
i: 7
i: 8
i: 9"""

# List Comprehension #

# Listelerdeki append metodunu hatırlayalım.
liste=[1, 2, 3, 4]
liste.append(5)  # [1, 2, 3, 4, 5]

# liste1'den liste2'yi oluşturalım.

liste1 = [1, 2, 3, 4, 5]
liste2=list() # veya list=[] ikiside bos liste olusturur.

for i in liste1:
    liste2.append(i)  # liste2 'ye liste1 in elemanları for döngüsü yardımıyla atıyoruz
print(liste2)  # [1, 2, 3, 4, 5]

# Acaba bu kodumuzu list comprehension ile daha kısa yazabilir miyiz ?

liste3=[1,2,3,4,5,6,7,8,9]

liste4=[i for i in liste3]
print(liste4)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ------------------------
liste =[3,4,5]  # her elemani 2 ile carpip yeni bir liste olusturmak istiyorum.
liste1=[i*2 for i in liste]
print(liste1)  # [6, 8, 10]
# ----------------------------

liste=[(1,2),(3,4),(5,6)]

liste1=[i*j for i,j in liste]
print(liste1)  # [2, 12, 30]

# ----------------------------
s="python"
liste1=[i for i in s]
print(liste1)  # ['p', 'y', 't', 'h', 'o', 'n']

# ------------------------------------------------------
lst=[]
a="Yusuf"
for i in a:
    lst.append(i*3)
print(lst)  # ['YYY', 'uuu', 'sss', 'uuu', 'fff'] bu sekildede bir denedim


# ----------- soylede yapabiliriz.

liste42=list()
isim="Yusuf"
liste42=[i*3 for i in isim]
print(liste42)  # ['YYY', 'uuu', 'sss', 'uuu', 'fff'] Yani bilmiyorum cok kisaldimi ama ilerde farkli islerde,
# ise yarayabilir (Ins..)


# Peki iç içe listeleri tek bir liste haline list comprehension ile nasıl getirebiliriz?
# İlk önce normal yolumuzu görelim

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
# yeni_liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
yeni_liste=[]
for i in liste:
    yeni_liste.append(i)
print(yeni_liste)  # [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15]] olabildi
# -------------------------------------------------------------------------------------------

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste2 = list()
for i in liste:
    for x in i:
        print("x:",x)
        liste2.append(x)
print(liste2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# List Comprehention ile:
liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste2=[x for i in liste for x in i]
print(liste2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

""" Yorum.Bence ilk yontem daha temiz."""



