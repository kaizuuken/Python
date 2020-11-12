import time

"""Nesne Tabanlı Programlama Mantığı

konuşacağız. Nesne Tabanlı Programlama veya ingilizce ismiyle Object Oriented Programming en basit anlamıyla gerçek
hayatı programlamaya uyarlamak olarak düşünülebilir. Örneğin bir tane öğrenci otomasyon sistemi yazmak istiyoruz.
Bunun için öğretmenleri , öğrencileri ve kursları aslında birer nesne olarak oluşturmamız gerekiyor. Böyle bir sistemi
 programlamayla gerçekleştirmek için aslında her bir nesnenin yapısını tanımlayıp, daha sonra bu yapılardan nesneler
 üretmemiz gerekiyor. """

# Obje nedir ?

# Etrafımıza baktığımızda aslında her bir eşyanın bir obje olduğunu görüyoruz. Örneğin bir tane televizyon kumandasını
# düşünelim. Bu kumandanın kendi içinde değişik özellikleri (attribute) ve fonksiyonları(metod) bulunuyor. Örneğin,
# kumandanın markası, tuşları aslında bu kumandanın özellikleridir(attribute). Kumandanın kırmızı tuşuna bastığımızda
# televizyonun kapanması ve sesi kapatma tuşuna bastığımızda televizyonun sesinin kapanması bu kumandanın metodlarıdır.
# Bunun gibi Pythondaki aslında her şey bir objedir. Örneğin, listelere bakacak olursak bu liste objelerinin aslında
# birçok metodu ve özelliği bulunur.

liste = [1, 2, 3, 4, 5]  # Liste objesi oluşturmak
liste.append(6)  # Append metodu
print(liste)

type(liste)  # liste objesi

sözlük = dict()
type(sözlük)  # dictionary objesi

type((1, 2, 3, 4))  # tuple objesi


def toplama(a, b):
    return a + b


type(toplama)  # Fonksiyon objesi

# # # # # # # # # # # # # # # # CLASSES # # # # # # # # # # # # # # # #

"""Bu konuda artık kendi veri tiplerimizi ve objelerimizi üretmeye başlayacağız.

Kendi veri tiplerimizi oluşturmak ve bu veri tiplerinden objeler üretmemiz için öncelikle objeleri üreteceğimiz yapıyı 
tanımlamamız gerekiyor. Bunu tasarladığımız yapıya da sınıf veya ingilizce ismiyle class diyoruz. Şimdi class yapılarını
öğrenerek konumuza başlayalım."""


# Class Anahtar Kelimesi
# Sınıflar veya Classlar objelerimizi oluştururken objelerin özelliklerini ve metodlarını tanımladığımız bir yapıdır ve
# biz herbir objeyi bu yapıya göre üretiriz. İsterseniz bir Araba classı tanımlayarak yapımızı kurmaya başlayalım.

# Yeni Bir Araba Veri Tipi Olusturalim.

class araba():
    model = 'Honda Civic'
    renk = "Gumus Gri"
    beygir_gucu = 106  # Sınıfımızın özellikleri (attributes)
    silindir = 4


# Sınıfımızı Pythonda tanımladık. Peki bu sınıftan obje nasıl oluşturacağız ? Bunu da şu şekilde yapabiliyoruz.

# obje_ismi = Sınıf_İsmi(parametreler(opsiyonel))

araba1 = araba()  # # araba veri tipinden bir "araba1" isminde bir obje oluşturduk.

print(type(araba1))  # <class '__main__.araba'> objemizin veri tipi araba

# araba1 objesi artık sınıfta tanımladığımız bütün özelliklere (attributes) sahip olmuş oldu. İşte sınıf ve obje üretmek
# bu şekilde olmaktadır. Peki bu araba objesinin özelliklerinin nasıl görebiliriz ?

araba1.model
print(araba1.model)  # Honda Civic
print(araba1.renk)  # Gumus Gri

araba2 = araba()
print(araba2.silindir)  # 4
print(araba2.model)  # Honda Civic

# Burda gördüğümüz gibi oluşturduğumuz objelerin buradaki model,renk vs. gibi özelliklerinin değeri aynıdır. Çünkü
# aslında burada tanımladığımız özellikler birer sınıf özelliğidir. Yani biz bir obje oluşturduğumuzda bu özelliklerin
# değerleri varsayılan olarak gelir. Bu özelliklerin değerlerine , herhangi bir obje oluşturmadan da erişebiliriz.
# Bunu da şu şekilde yapabiliriz.

print(araba.renk)  # Gumus Gri
print(araba.model)  # Honda Civic

# Bizim her bir objeyi başlangıçta farklı değerlerle oluşturmamız için her bir objeyi oluştururken objelerin değerlerini
# göndermemiz gerekiyor. Bunun için de özel bir metodu kullanmamız gerekmektedir.
#                   __init__()
# Peki bu metod ne anlama geliyor ? Ilk olarak dir() fonksiyonu yardımıyla araba1 objemizde neler var bakalım.

print(dir(araba1))

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# '__weakref__', 'beygir_gucu', 'model', 'renk', 'silindir']

"""Burada objemizin tüm özelliklerini ve metodlarını görüyoruz. Ancak biz herhangi bir metod tanımlamamıştır. Buradaki 
metodlar Python tarafından bir obje oluşturulduğunda özel olarak tanımlanan metodlardır ve biz eğer özel olarak bunları 
tanımlamazsak Python kendisi bunları varsayılan tanımlıyor. Burada aynı zamanda init metodunu da görüyoruz. Eğer biz bu 
metodu kendimiz tanımlarsak objelerimizi farklı değerlerle başlatabiliriz.

Aslında init metodu Pythonda yapıcı(constructor) fonksiyon olarak tanımlanmaktadır. Bu metod objelerimiz oluşturulurken
otomatik olarak ilk çağrılan fonksiyondur. Bu metodu özel olarak tanımlayarak objelerimizi farklı değerlerle 
oluşturabiliriz.

Peki bu metodu nasıl tanımlayacağız ? Direk örnek üzerinden görmeye çalışalım."""


# araba Veri tipi

class araba():
    model = 'Honda Civic'
    renk = 'Gumus Gri'
    silindir = 4
    beygir_gucu = 110

    # Simdilik Class ozelliklerine Ihtiyacimiz yok.
    def __init__(self):
        print('Init Fonksiyonu Cagirildi.')


araba1 = araba()  # Init Fonksiyonu Cagirildi.

"""Peki burada self ne anlama geliyor ? self anahtar kelimesi objeyi oluşturduğumuz zaman o objeyi gösteren bir 
referanstır ve metodlarımızda en başta bulunması gereken bir parametredir. Yani biz bir objenin bütün özelliklerini ve 
metodlarını bu referans üzerinden kullanabiliriz.

Objeler oluşturulurken, Python bu referansı metodlara otomatik olarak kendisi gönderir. Özel olarak self referansını 
göndermemize gerek yoktur.

init metodunu ve self'i iyi anlamak için objelerimize özellikler ekleyelim."""


class araba():
    def __init__(self, model, renk, beygir_gucu, silindir):
        print('Init Fonksiyonu Cagirildi.')
        self.model = model
        self.renk = renk
        self.beygir_gucu = beygir_gucu
        self.silindir = silindir


araba1 = araba("Honda Civic", "Gumus Gri", 110, 4)
araba2 = araba("Bmw M5", "Austun Yellow", 600, 8)

print(araba1.model)  # Honda Civic
print(araba2.model)  # Bmw M5


# Veya bunu Bilgi Yok veya Varsayilan Degerler ile tanimlayabiliriz

class araba():
    def __init__(self, model='Bilgi Yok', renk='Bilgi Yok', beygir_gucu=70, silindir=4):
        self.model = model
        self.renk = renk
        self.beygir_gucu = beygir_gucu
        self.silindir = silindir


arabax = araba(beygir_gucu=110, renk="Turuncu")
print(arabax.beygir_gucu)  # 110
print(arabax.silindir)  # 4
print(arabax.model)  # Bilgi Yok
print(arabax.renk)  # Turuncu

arabax = araba(model='Bmw M5')
print(arabax.model)  # Bmw M5
print(arabax.beygir_gucu)  # 70 Cunku sadece Modelini tanimladik


# # # # # # # # # # # # # # # Methods # # # # # # # # # # # # # # #

# Bir Sinif Icerisinde Metotlarimizi Nasil Tanimlayacagiz? Bunun Icin Bir Yazilimici Sinifi Tanimlayalim.

class Yazilimci():
    def __init__(self, isim, soyisim, sirket, maas, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.sirket = sirket
        self.maas = maas
        self.diller = diller


# yazilimci1 Objesi
yazilimci1 = Yazilimci("Yusuf", 'ERDEM', "Boston Dynamics", 12000, ["Python", "C", "Java"])
yazilimci2 = Yazilimci("Yigit", "Erdem", "GitHub", 11999, ["Python", "R", "SmallTalk"])

print(yazilimci1.diller)  # ['Python', 'C', 'Java']
print(yazilimci2.sirket)  # GitHub


# Simdi Biz Buna Bilgileri Goster Adli Bir Metod yazarak ,
# her bir özelliğimizin değeri ekrana derli toplu bir şekilde yazdıralim

class Yazilimci():
    def __init__(self, isim, soyisim, sirket, maas, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.sirket = sirket
        self.maas = maas
        self.diller = diller

    def bilgileri_goster(self):
        print("""
        Calisan Bilgisi:
        
        Isim: {}
        
        Soyisim: {}
        
        Sirket: {}
        
        Maas: {}
        
        Diller: {}
        
        """.format(self.isim, self.soyisim, self.sirket, self.maas, self.diller))


yazilimci1 = Yazilimci("Yusuf", "Erdem", "Boston Dynamics", 12000, ["python", "Java", "C"])

yazilimci1.bilgileri_goster()

""" 

    Output :
Calisan Bilgisi:
        
        Isim: Yusuf
        
        Soyisim: Erdem
        
        Sirket: Boston Dynamics
        
        Maas: 12000
        
        Diller: ['python', 'Java', 'C']

"""


# Burada bilgilerigöster isimli metod tanımlayarak her bir özelliğimizin değeri ekrana derli toplu bir şekilde yazdırmış
# olduk. Metodlarımızı yazarken dikkat etmemiz gerek nokta, her metodun birinci parametresinin self referansı olması
# gerektiğidir. Ayrıca objelerimizin özelliklerine mutlaka self referansıyla erişmemiz gerekiyor.
# Yazilimci class`ina 2 tane daha metod yazalım.

class Yazilimci():
    def __init__(self, isim, soyisim, sirket, maas, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.sirket = sirket
        self.maas = maas
        self.diller = diller

    def bilgileri_goster(self):
        print("""
        Calisan Bilgisi:

        Isim: {}

        Soyisim: {}

        Sirket: {}

        Maas: {}

        Diller: {}

        """.format(self.isim, self.soyisim, self.sirket, self.maas, self.diller))

    def dil_ekle(self, yeni_dil):
        print("Dil Ekleniyor..")
        time.sleep(1)
        self.diller.append(yeni_dil)

    def maas_yukselt(self, zam_miktari):
        print("Zam Yapiliyor..")
        time.sleep(1)
        self.maas += zam_miktari


yazilimci1 = Yazilimci("Yusuf", "Erdem", "Boston Dynamics", 12000, ["C", "Java", "Python"])

yazilimci1.bilgileri_goster()
yazilimci1.maas_yukselt(500)
yazilimci1.bilgileri_goster()
yazilimci1.dil_ekle("GoLang")
yazilimci1.bilgileri_goster()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ INTHERITANCE(KALITIM) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""Bu konuda Nesne Tabanlı Programlamadaki inheritance(kalıtım veya miras alma) konseptini öğrenmeye çalışacağız. 
Inheritance veya kalıtım bir sınıfın başka bir sınıftan özelliklerini(attribute ) ve metodlarını miras almasıdır.

Bu konsepti aslında bizim kendi anne babamızdan değişik özellikleri ve davranışları miras almamıza benzetebiliriz.
(Hani derler ya ! Babasına çekmiş :) )

Peki inheritance nerede işimize yarar ? Örneğin, bir şirketin çalışanlarını tasarlamak için sınıflar oluşturuyoruz. 
Bunun için Yönetici, Proje Direktörü, İşçi gibi sınıflar oluşturmamız gerekiyor. Aslında baktığımız zaman bu sınıfların 
hepsinin belli ortak metodları ve özellikleri bulunuyor. O zaman bu ortak özellikleri ve metodları tekrar tekrar bu 
sınıfların içinde tanımlamak yerine, bir tane ana class tanımlayıp bu classların bu classın özelliklerini ve metodlarını
 almalarını sağlayabiliriz. Inheritance'ın veya Kalıtım'ın temel mantığı budur.

"""


# Bir Calisan sinifi olusturalim

class Calisan():
    def __init__(self, isim, maas, departman):
        print("Calisan Sinifinin Init Fonksiyonu.")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print("Calisan Sinifinin Bilgileri ...")
        print("Isim: {} \n Maas: {} \nDepartman: {}\n".format(self.isim, self.maas, self.departman))

    def departman_degis(self, yeni_departman_ismi):
        self.departman = yeni_departman_ismi


class Yonetici(Calisan):
    pass


yonetici = Yonetici("Yusuf Erdem", 12000, "IT")

yonetici.bilgileri_goster()  # Calisan sinifinin Init Fonk.
""" 
Isim: Yusuf Erdem 
Maas: 12000 
Departman: IT 
"""
yonetici.departman_degis("Insan Kaynaklari")
yonetici.bilgileri_goster()

"""
Isim: Yusuf Erdem 
 Maas: 12000 
Departman:Insan Kaynaklari
"""
print(dir(yonetici))


class Yonetici(Calisan):
    def zam_yap(self, zam_yap):
        self.maas += zam_yap


yonetici1 = Yonetici("Irem Yalcin", 4500, "Insan Kaynaklari")
yonetici1.zam_yap(500)
yonetici1.bilgileri_goster()
"""Calisan Sinifinin Bilgileri ...
   Isim: Irem Yalcin 
   Maas: 5000 
   Departman: Insan Kaynaklari"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Ovverriding (Iptal Etme) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""Overriding (Iptal Etmek)
Eğer biz miras aldığımız metodları aynı isimle kendi sınıfımızda tekrar tanımlarsak , artık metodu çağırdığımız zaman 
miras aldığımız değil kendi metodumuz çalışacaktır. Buna Nesne Tabanlı Programlamada bir metodu override etmek denmektedir.


Örneğin artık Çalışan sınıfının init metodunu kullanmak yerine Yönetici sınıfında init metodunu override edebiliriz. 
Böylelikle Yönetici sınıfına ekstra özellikler(attribute) ekleyebiliriz."""


class Calisan():
    def __init__(self, isim, maas, departman):
        print("Calisan Sinifinin Init Fonksiyonu.")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print("Calisan Sinifinin Bilgileri ...")
        print("Isim: {} \n Maas: {} \nDepartman: {}\n".format(self.isim, self.maas, self.departman))

    def departman_degis(self, yeni_departman_ismi):
        self.departman = yeni_departman_ismi


class Yonetici(Calisan):
    def __init__(self, isim, maas, departman, kisi_sayisi):  # kisi Sayisi = Sorumlu Oldugu Kisi sayisi
        self.isim = isim
        self.maas = maas
        self.departman = departman
        self.kisi_sayisi = kisi_sayisi  # yeni eklenen ozellik.

    def zam_yap(self, zam_miktari):
        self.maas += zam_miktari


# Artik iki init fonk . oldugundan yonetici objesi olusturudugumuzda Yoneticideki init calisacak
yonetici21 = Yonetici('Yusuf', 12000, "IT", 12)
yonetici21.bilgileri_goster()


# Isim Maas Departman geldi fakat sorumlu oldugu kisi sayisi gelmedi bunun icin asagida tekrar bilgileri gosteri override
# etmemiz gerekicek

class Calisan():
    def __init__(self, isim, maas, departman):
        print("Calisan Sinifinin Init Fonksiyonu.")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print("Calisan Sinifinin Bilgileri ...")
        print("Isim: {} \n Maas: {} \nDepartman: {}\n".format(self.isim, self.maas, self.departman))

    def departman_degis(self, yeni_departman_ismi):
        self.departman = yeni_departman_ismi


class Yonetici(Calisan):
    def __init__(self, isim, maas, departman, kisi_sayisi):  # kisi Sayisi = Sorumlu Oldugu Kisi sayisi
        self.isim = isim
        self.maas = maas
        self.departman = departman
        self.kisi_sayisi = kisi_sayisi  # yeni eklenen ozellik.

    def zam_yap(self, zam_miktari):
        self.maas += zam_miktari

    def bilgileri_goster(self):
        print("Yonetici Sinifi Bilgileri...")
        print("Isim: {} \n Maas: {} \nDepartman: {}\nSorumlu Oludu Kisi Sayisi:{}".format(self.isim, self.maas,
                                                                                          self.departman,
                                                                                          self.kisi_sayisi))


yonetici21 = Yonetici('Yusuf', 12000, "IT", 12)
yonetici21.bilgileri_goster()

"""Out:
Yonetici Sinifi Bilgileri...
Isim: Yusuf 
Maas: 12000 x  
Departman: IT
Sorumlu Oludu Kisi Sayisi:12

"""

#  ~~~~~~~~~~~~~~~~~~~~~~ Super Anahtar Kelimesi ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
super anahtar kelimesi özellikle override ettiğimiz bir metodun içinde aynı zamanda miras aldığımız bir metodu kullanmak istersek kullanılabilir. 
Yani super en genel anlamıyla miras aldığımız sınıfın metodlarını alt sınıflardan kullanmamızı sağlar. Hemen örnek üzerinden anlamaya çalışalım.

"""


class Calisan():
    def __init__(self, isim, maas, departman):
        print("Calisan Sinifinin Init Fonksiyonu.")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print("Calisan Sinifinin Bilgileri ...")
        print("Isim: {} \n Maas: {} \nDepartman: {}\n".format(self.isim, self.maas, self.departman))

    def departman_degis(self, yeni_departman_ismi):
        self.departman = yeni_departman_ismi


class Yonetici(Calisan):
    def __init__(self, isim, maas, departman, kisi_sayisi):  # kisi Sayisi = Sorumlu Oldugu Kisi sayisi
        super().__init__(isim, maas,
                         departman)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          # Bu Satir Beni self.isim=isim self.maas=maas vs yazmaktan kurtardi sadece ekstra olarak kisi sayisi ekledim
        self.kisi_sayisi = kisi_sayisi  # yeni eklenen ozellik.

    def zam_yap(self, zam_miktari):
        self.maas += zam_miktari

    def bilgileri_goster(self):
        print("Yonetici Sinifi Bilgileri...")
        print("Isim: {} \n Maas: {} \nDepartman: {}\nSorumlu Oludu Kisi Sayisi:{}".format(self.isim, self.maas,self.departman,self.kisi_sayisi))


yonetici12 = Yonetici('Yusuf', 12000, "IT", 13)
yonetici12.bilgileri_goster()

# ~~~~~~~~~~~~~~~~~~~~~~~~ SPECIAL METHODS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""Nesne tabanlı programlamada son olarak sınıfların özel metodlarını nasıl kendimiz yazarız öğrenmeye çalışalım. Özel metodlar, daha önceden de 
bahsettiğimiz gibi bizim özel olarak çağırmadığımız ancak her classa ait metodlardır. Bunların çoğu biz tanımlamasak bile Python tarafından varsayılan 
olarak tanımlanır. Ancak bu metodların bazılarını da özel olarak bizim tanımlamamız gerekmektedir. Daha önceden gördüğümüz init metodu bu metodlara
 bir örnektir. Bu konuda bu metodlarını nasıl tanımlayacağımızı öğrenmeye çalışacağız."""


class Kitap():
    pass


kitap1 = Kitap()  # __init__ methodu

print(kitap1)  # <__main__.Kitap object at 0x7f862119d040> __str__ metodu

# len(kitap1) yazarsak

"""TypeError                                 Traceback (most recent call last)
<ipython-input-66-5f5391921a08> in <module>()
----> 1 len(kitap1) # __len__ metodu çağrılacak ancak tanımlı değil. Bunu özellikle bizim tanımlamamız gerekiyor.

TypeError: object of type 'Kitap' has no len() """

# del kitap1  # __del__ metodu

# print(kitap1)  # del anahtar kelimesi bir objeyi siler ve __del__ metodu çağrılır.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  __init__ metodu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Kitap():
    def __init__(self, isim, yazar, sayfa_sayisi, tur):
        print("Kitap Objesi Olusturuluyor...")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur


kitap1 = Kitap("Homo Saphiens", "Yuval Noah HARARI", 412, "Populer Bilim")  # Kendi Metodumuz

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  __str__ Metodu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# normalde print(kitap1) yazarsak
print(kitap1)  # <__main__.Kitap object at 0x7fe1259a00a0>  eger str fonksiyonunu kendimiz tanimlarsak kendimiz icine yazi yazabiliriz.


class Kitap():
    def __init__(self, isim, yazar, sayfa_sayisi, tur):
        print("Kitap Objesi Olusturuluyor...")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur

    def __str__(self):
        # return kullanmamiz gerekli
        return "Isim:{}\nYazar:{}\nSayfa_Sayisi:{}\nTur{}".format(self.isim, self.yazar,self.sayfa_sayisi,self.tur)

kitap2= Kitap("Homo Saphiens", "Yuval Noah HARARI", 412, "Populer Bilim")  # Kendi Metodumuz
print(kitap2)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  __len__ Metodu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Kitap():
    def __init__(self, isim, yazar, sayfa_sayisi, tur):
        print("Kitap Objesi Olusturuluyor...")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur

    def __str__(self):
        # return kullanmamiz gerekli
        return "Isim:{}\nYazar:{}\nSayfa_Sayisi:{}\nTur{}".format(self.isim, self.yazar,self.sayfa_sayisi,self.tur)
    def __len__(self):
        return self.sayfa_sayisi

kitap3= Kitap("Homo Saphiens", "Yuval Noah HARARI", 412, "Populer Bilim")  # Kendi Metodumuz
print(len(kitap3))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  __del__ Metodu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Kitap():
    def __init__(self, isim, yazar, sayfa_sayisi, tur):
        print("Kitap Objesi Olusturuluyor...")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur

    def __str__(self):
        # return kullanmamiz gerekli
        return "Isim:{}\nYazar:{}\nSayfa_Sayisi:{}\nTur{}".format(self.isim, self.yazar,self.sayfa_sayisi,self.tur)
    def __len__(self):
        return self.sayfa_sayisi
    def __del__(self):
        print("Kitap Objesi Siliniyor.")

kitap4= Kitap("Homo Saphiens", "Yuval Noah HARARI", 412, "Populer Bilim")

del kitap4




