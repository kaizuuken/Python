"""Python programlarında bazen bir değişkenin tanımlanmadan kullanılmaya çalıştırılması , bazen de yapılamayacak bir
 aritmetik işlemin yapılması Pythonda hatalara yol açar. Ancak bu istisnai durumlarda, hataların türüne göre
 programlarımızı daha güvenli bir şekilde yazabiliriz.Yani hata çıkarabilecek kodlarımızı öngörerek bu hataları
 programlarımızda yakalayabiliriz. Pythondaki bazı hatalara şunlar örnek verilebilir;
"""

# print(a) yazarsak ; Name Error Hatasi aliriz
# NameError: name 'a' is not defined"""

# int("sasdad12312ds") Value Error
# ValueError: invalid literal for int() with base 10: 'sasdad12312ds'"""

# 2/0  jav Yazarsak
# ZeroDivisionError: division by zero

# print("Yusuf"asdasdsad)
# SyntaxError: invalid syntax


# # # # # # # # # # # # # # # HATA YAKALAMA  # # # # # # # # # # # # # # #


"""try , except blokları
try ,except bloklarının yapısı şu şekildedir;

                try:

                    Hata çıkarabilecek kodlar buraya yazılıyor.
                    Eğer hata çıkarsa program uygun olan except bloğuna girecek.
                    Hata oluşursa try bloğunun geri kalanındaki işlemler çalışmayacak.
                except Hata1:
                    Hata1 oluştuğunda burası çalışacak.
                except Hata2:
                    Hata2 oluştuğunda burası çalışacak.

                    //
                    //
                    //
"""
# a = int("324234dsadsad") # Burası ValueError hatası veriyor.

try:
    a = int("324234dsadsad")
    print("ProgramBurada")
except:  # Hatayi Belirtmessek tum hatalar bu kisma girer.
    print('Bir Hata Olustu..')
print("bloklar sona erdi")


# a = int("32434aaa") - Value Error
# print(2 / 0) - Zero Division Error
# Bu iki hatayi deneyelim

try:
    a=int(input("Num1:"))
    b=int(input("Num2:"))
    print(a/b)
except ValueError:
    print("Lutfen Input'u Dogru giriniz...")
except ZeroDivisionError:
    print("Bir Sayi 0'a Bolunemez.")

# Istersek Bu Iki Hataninda ayni except bloguna girmesini saglayabiliriz.

try:
    x=int(input("Num1:"))
    y=int(input('Num2:'))
    print(x/y)
except (ValueError,ZeroDivisionError):
    print("Zero Division or Value Error")


"""try,except,finally blokları¶
Bazen programlarımızda her durumda mutlaka çalışmasını istediğimiz kodlar bulunabilir.Bunun için biz kendi try,except
 bloklarına ek olarak bir tane finally bloğu ekleyebiliriz. finally blokları hata olması veya olmaması durumunda mutlaka
çalışacaktır. Yapısı şu şekildedir;

                try:

                    Hata çıkarabilecek kodlar buraya yazılıyor.
                    Eğer hata çıkarsa program uygun olan except bloğuna girecek.
                    Hata oluşursa try bloğunun geri kalanındaki işlemler çalışmayacak.
                except Hata1:
                    Hata1 oluştuğunda burası çalışacak.
                except Hata2:
                    Hata2 oluştuğunda burası çalışacak.

                    //
                    //
                    //
                finally:
                    Mutlaka çalışması gereken kodlar buraya
                    Bu blok her türlü çalışacak.
                    # Mesela dosyanin kesinlikle kapanmasi gerekiyor o kodlari buraya yaziyoruz."""

try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a / b) # Hata burada oluşuyor. ZeroDivisionError'a bloğuna giriyoruz.
except ValueError:
    print("Lütfen inputları doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")
finally:
    print("Her durumda çalışıyorum.")


"""
Hata fırlatmak
Bazen kendi yazdığımız fonksiyonlar yanlış kullanılırsa kendi hatalarımızı üretip Pythonda bu hataları fırlatabiliriz. 
Bunun içinde raise anahtar kelimesini kullanacağız. Hata fırlatma şu şekilde yapılabilmektedir;

            raise HataAdı(opsiyonel hata mesajı)
"""

def terscevir(s):
    if (type(s) != str):
        raise ValueError("Lutfen String Bir Deger Gonderin!")
    else:
        return s[::-1]

print(terscevir("Python"))
#print(terscevir(12)) # ValueError: Lutfen String Bir Deger Gonderin! diyor fakat ben bunu try da nasil yakalayacagim?

try:
    print(terscevir(12))
except ValueError:
    print("Fonksiyon Hata Verdi")










