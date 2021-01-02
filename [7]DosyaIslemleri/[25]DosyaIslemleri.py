print("Dosya Islemeleri")

"""Bir dosyayı açmak için open() fonksiyonunu kullanıyoruz. Yapısı şu şekildedir;

           #    open(dosya_adı,dosya_erişme_kipi)
           # Dosya adını istediğimiz isimde verebiliriz. Dosya erişme kipi ise bizim dosya üzerindeki işlemlerimizi   belirler



              # "w" dosya kipi"""

# Dosyalarımızı açmak ve dosyalarımıza yazmak için "write" anlamına gelen "w" kipini kullanıyoruz. "w" kipi eğer
# oluşturmak istediğimiz dizinde öyle bir dosya yoksa dosyayı oluşturuyor , eğer öyle bir dosya varsa dosyayı silip
# tekrar oluşturuyor. Yani, eğer açmak istediğimiz dosyadan zaten varsa ve dosyanın içi doluysa "w" kipi dosyadaki
# bilgileri silip tekrar oluşturacaktır. (Biraz Tehlikeli)


open("bilgiler.txt","w")  #  Dosyayı bulunduğumuz dizinde açıyor.

file=open("/Users/Macintosh/Desktop/Bilgiler.txt","w")
file.close() # Kapatmak icin

file=open("/Users/Macintosh/Desktop/Bilgiler.txt","w")
file.write("Yusuf Erdem şş")
file.close()

file=open("/Users/Macintosh/Desktop/Bilgiler.txt","w") # Dosyayi sildi ve tekrar olusturdu.. Bunu onlemek icin

"""           "a" Kipiyle Dosyalara Yazmak
"append" (ekleme) kelimesinin kısaltması olan "a" kipiyle bir dosyayı açtığımızda , dosya eğer yoksa oluşturulur. Eğer 
öyle bir dosya mevcut ise, dosya tekrar oluşturulmaz ve dosya imleci dosyanın sonuna giderek dosyaya 
ekleme yapmamızı sağlar."""

file = open("/Users/Macintosh/Desktop/bilgiler.txt","a",encoding="utf-8")  # Türkçe karakter kullanacaksak encoding="utf-8" parametresi veriyoruz

# file=open("bilgiler.txt","a",encoding="utf-8") # Seklinde Yazarsam Bulundugu yere Desktop Python Dosya islemleri klasorune acicak

file.write("Yusuf Erdem")
file.close()
file = open("/Users/Macintosh/Desktop/bilgiler.txt","a",encoding="utf-8")
file.write("Irem Yalcin") # Dosyanin Icinde Yusuf ErdemIrem Yalcin Bitisik yaziyor.
file.close()
file = open("/Users/Macintosh/Desktop/bilgiler.txt","a",encoding="utf-8")
file.write("Emre Inan")
file.close() # Yine Bitisik yazdi..... Dosyanin Icindekileri silip Kaydettim

# Bu Karmasanin Onune gecmek icin \n

file = open("/Users/Macintosh/Desktop/denemebilgiler.txt","a",encoding="utf-8")
file.write("Yusuf Erdem\n")
file.close()
file = open("/Users/Macintosh/Desktop/denemebilgiler.txt","a",encoding="utf-8")
file.write("Irem Yalcin\n")
file.close()  # Basarili.


# Bulundugumuz Klasore Bir bilgiler txt acalim
"""
# Dosyaları okumak ve verileri almak için "r" kipiyle açmamız gerekiyor. "r" kipiyle açtığımız dosya eğer bulunmuyorsa
# "FileNotFoundError" hatası dönecektir. Şimdi bulunduğumuz dizinde bulunan "bilgiler.txt" dosyasını açalım.

"""
file = open("bilgiler.txt","w",encoding="utf-8")
file.write("Yusuf Erdem\n")
file.write("Irem Yalcin\n")
file.write("Emre Inan\n")
file.close()
file = open("bilgiler.txt","r", encoding="utf-8")
file.close()
 # file = open("bilgiler2.txt","r",encoding="utf-8") # File Not Found Error
try:
    file = open("bilgiler2.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("Aradiginiz Dosya Bulunamadi!")

"""
Peki bir dosyanın içinden bilgileri nasıl okuyacağız ? Bunun için Pythonda değişik yöntemler bulunuyor.

                    ~~~~~~~~~~~~~~~~ For döngüsü ile okuma ~~~~~~~~~~~~~~~~~~
Şöyle bir kullanım dosyamızdaki herbir satırı tek tek okuyacaktır.
"""

file = open("bilgiler.txt","r", encoding="utf-8")

for i in file:
    print(i)
file.close()  # Burada her bir satırımız boşluklu yazıldı. Bunun nedeni, hem her satır sonunda "\n" karakterinin olması
              # hem de print fonksiyonun bir alt satıra geçmek için boşluk bırakmasıdır. Bunu önlemek için varsayılan
              # değer olarak "\n" karakteri alan end parametresine kendimiz değer verebiliriz.
file = open("bilgiler.txt","r", encoding="utf-8")

for i in file:
    print(i,end="")
file.close()  # Alt Alta bosluk birakmadan yazdi

"""    ~~~~~~~~~~~~~~~ read() fonksiyonu ~~~~~~~~~~~~~~
read() fonksiyonu eğer içine hiçbir değer vermezsek bütün dosyamızı okuyacaktır.

!!read() fonksiyonuna değer vererek belli bir kısmı okumayı Sonra  Ogrensek . Daha doğru olur.

"""
file = open("bilgiler.txt","r", encoding="utf-8")
icerik=file.read()
print("Dosyanin Icerigi:")
print(icerik)

print("Dosyanin Icerigi2:")

icerik2=file.read()
print(icerik2) # Bunun Icerisinde Hicbir sey yok. read() fonksiyonuyla bir dosyayı okuduğumuzda dosya imlecimiz dosyanın
               # en sonuna gider ve read() fonksiyonu 2. okuma da artık boş string döner.

file = open("bilgiler.txt","r", encoding="utf-8")
icerik=file.read()
print("Dosyanin Icerigi:\n",icerik,sep="") # sep="" parametresini ilk satirda 1 bosluk birakmamasi icin yazdim.

file.close()

"""      ~~~~~~~~~~~~~~~~~~~~~~ readline() Fonksiyonu ~~~~~~~~~~~~~~~~~~~~~~~~
readline() fonksiyonu her çağrıldığında dosyanın sadece bir satırını okur. Her seferinde dosya imlecimiz (file) bir satır atlayarak devam eder.
"""

file=open("bilgiler.txt","r",encoding="utf-8")
print(file.readline()) # Yusuf Erden
print(file.readline()) # Irem Yalcin
print(file.readline()) # Emre Inan
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(file.readline()) # Okuyacak Birsey kalmayinca readline fonksiyonu bos string doner.
file.close()

"""        ~~~~~~~~~~~~~~~~~~~~~ readlines() fonksiyonu ~~~~~~~~~~~~~~~~~~~~~~
readlines() fonksiyonu dosyanın bütün satırları bir liste şeklinde döner.
"""
file=open("bilgiler.txt","r",encoding="utf-8")
print(file.readlines())   # ['Yusuf Erdem\n', 'Irem Yalcin\n', 'Emre Inan\n']

"""             Dosyalarda Kullanılan Fonksiyonlar

Dosyaları Otomatik Kapatma
Dosyalarda işlemlerimiz bittiği zaman dosyamızı kapatmamız gerektiğini biliyoruz. Ancak programlamacılık doğası gereği
 çoğu zaman dosyaları kapatmayı unutabiliriz. Bunun için Pythonda dosyalarda işimiz bitince otomatik kapatma özelliği
  bulunuyor. Bundan sonra Pythonda dosya işlemlerimizi şu blok içinde yapacağız.
  
                            with open(dosya_adı,dosya_kipi) as file:
                                 Dosya işlemleri

"""

with open("bilgiler.txt","r",encoding="utf-8") as file:
    for i in file:
        print(i,end="")

"""Eğer dosya işlemlerini bu blok içinde yaparsak işlemimiz bittiği zaman dosyamız otomatik olarak kapanacaktır."""

"""          `````````````Dosyaları İleri Geri Sarmak`````````````````
dosyaları okurken sadece dosyanın en başından başlayabiliyorduk ve dosya imlecimiz okuma işleminin sonunda , dosyanın 
en sonuna gidiyordu. Ancak biz çoğu zaman dosya imlecini (file) dosyanın herhangi bir yerine götürmek isteyebiliriz. 
Bunun için Pythondaki seek() fonksiyonunu kullanacağız. Ancak ondan önce dosya imlecinin hangi byteda olduğunu söyleyen
tell() fonksiyonuna bakalım.

"""
with open("bilgiler.txt","r",encoding="utf-8") as file:
    print(file.tell()) # 0 Bytta

with open("bilgiler.txt","r",encoding="utf-8") as file:
    print(file.tell())
    file.seek(20)
    print(file.tell()) # 20

with open("bilgiler.txt","r",encoding="utf-8") as file:
    print(file.tell())
    file.seek(10)
    icerik=file.read(20) # 20 Byte Okumak Istiyorum dedik
    print(icerik) # m
                  #Irem Yalcin
                  #Emre I   Ciktilarini verdi

with open("bilgiler.txt","r",encoding="utf-8") as file:
    file.seek(5)
    icerik=file.read(10)
    print(file.tell())
    print(icerik)

with open("bilgiler.txt", "r", encoding="utf-8") as file:
    print(file.read())

"""~~~~~~~~~~~~~~~~~~~~Dosyalarda Değişiklik Yapmak ~~~~~~~~~~~~~~~~~~~~~~~~

seek() ve write()
Eğer biz bir dosyanın belli bir yerine seek() fonksiyonu ile gidip, write() fonksiyonunu kullanırsak, yazdığımız 
değerler öncesinde bulunan değerlerin üzerine yazılacaktır. Bunun için hem okuma hem de yazma işlemimizi yapmamızı 
sağlayan "r+" kipini kullanacağız. İlk önce dosyamızda bilgileri görelim."""

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.read())

# with open("bilgiler.txt","r+",encoding = "utf-8") as file:
   # file.seek(10) # 10. byte
   # file.write("Deneme")

with open("bilgiler.txt", "r+", encoding="utf-8") as file:
        print(file.read())

# Dosyaya baktigimda Yusuf ErdeDeneme Yalcin
# Emre Inan gibi bir out veriyor. 10. byte dan itibaren uzerine yaziyor.
# Dosyayi eski haline getirdim.

"""~~~~~~~~~~~~ Dosyanin Sonuna Degisiklik yapmak ~~~~~~~~~~"""



with open("bilgiler.txt","a",encoding = "utf-8") as file:
    file.write("Alpaslan Tokdogan\n") # "append" metoduyla açılan bir dosyanın imleci direk dosyanın sonunda olduğu için sadece write

with open("bilgiler.txt","r",encoding = "utf-8") as file:
    print(file.read())

with open("bilgiler.txt","a",encoding = "utf-8") as file:
    file.write("Emre S Tasci\n")

with open("bilgiler.txt","r",encoding = "utf-8") as file:
    print(file.read())

# Bu Sekilde Dosyanin sonuna ekeleme yapabiliyoruz.
"""Dosyanın Başında Değişiklik Yapmak"""

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    icerik=file.read()
    print(icerik)

    """Yusuf Erdem
       Irem Yalcin
       Emre Inan
       Alpaslan Tokdogan
       Emre S Tasci"""
with open("bilgiler.txt","r+",encoding="utf-8",) as file:
    icerik=file.read()
    icerik="Guido Van Rossum\n"+icerik
    file.seek(0)
    file.write(icerik)

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    icerik=file.read()
    print(icerik)

"""         ~~~~~~~~~~~~~~~~~ Dosyanın Ortasında Değişiklik Yapmak ~~~~~~~~~~~~~~
Dosyaların ortasına herhangi bir satır eklemek için ilk olarak her bir satırı liste halinde almamızı sağlayan readlines()
fonksiyonunu kullanacağız. Daha sonra bu listenin herhangi bir yerine bir eleman ekleyerek
bu listeyi for döngüsü ile dosyaya yazacağız."""

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    print(file.readlines())

    # ['Guido Van Rossum\n', 'Yusuf Erdem\n', 'Irem Yalcin\n', 'Emre Inan\n', 'Alpaslan Tokdogan\n', 'Emre S Tasci\n']

# Ornegin Irem Yalcin Satirinin altina Bir tane daha satır eklemek istiyoruz. Bunun için bu listenin 3.indeksine
# insert() metoduyla bir satır ekleyeceğiz. Daha sonra dosyanın en başına giderek bu listeyi tek tek for döngüsü ile yazacağız.

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Steve Wozniak\n")
    file.seek(0)
    for i in liste:
        file.write(i)

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    icerik = file.read()
    print(icerik)

# Pythonda bir dosyaya listenin içindeki değerleri yazmak için for döngüsü dışında pratik bir fonksiyon bulunuyor.
# writelines fonksiyonu içine verdiğimiz listeyi dosyaya yazacaktır.


with open("bilgiler.txt","r+",encoding="utf-8") as file:
    liste=file.readlines()
    liste.insert(3,"Alan Turing\n")
    file.seek(0)
    file.writelines(liste)

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    icerik=file.read()
    print(icerik)


