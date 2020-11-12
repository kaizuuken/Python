"""Modül Mantığı
Bu konuda modüllerin ne demek olduğunu ve mantığını anlamaya çalışacağız.

Pythonda aslında herbir dosya bir modüldür ve her bir modül içinde fonksiyonlar, sınıflar ve objeler barındırır.
Biz de bu modülleri programımıza dahil ederek içindeki fonksiyonlardan, sınıflardan ve objelerden faydalanabiliriz.

Gerçek hayattan benzetme yapacak olursak bir matematik ödevini yaparken kullandığımız formül kitabı aslında bir modül
olarak düşünülebilir. Bu kitabı ödev yaparken kullanarak ödevimizi çok hızlı ve pratik bir şekilde bitirebiliriz.

Pythonda da modül kavramı oldukça önemli bir kavramdır. Bir Python modülünü programımıza dahil ederek bu modüller içinde
 yazılan fonksiyonlardan ve sınıflardan kullanabilir ve programlarımızı daha efektif bir şekilde yazabiliriz. Eğer modül
  diye bir kavram olmasaydı, programlarımızdaki herbir fonksiyonu ve sınıfı kendimiz yazmak zorunda kalacaktık.

Pythonda Python geliştiricileri tarafından yazılmış bir çok hazır modül bulunmaktadır. Ayrıca , programcıların internete
ve Githuba yükledikleri bir çok modülü programlarımızda kullanabilir ve daha güzel programlar yazabiliriz.

Modül Kavramını anladıysak bir sonraki konuda bir modül bir programa nasıl dahil edilir öğrenmeye çalışalım."""

# *** NOT **** : os modulunu dene.


import math  # Modülü içeri aktarıyoruz. Artık bu modülün tüm fonksiyonlarını kullanabiliriz.

print(dir(math))  # Math modülünün içindekileri görmek için dir fonksiyonunu kullanabiliriz.
help(math)  # Fonksiyonların görevlerini görebilmek için help fonksiyonunu kullanabiliriz.

# Peki bu içeri aktarma yöntemiyle math modülünün herhangi bir fonksiyonunu nasıl kullanacağız ?

print(math.factorial(4))  # 24

print(math.floor(5.6))  # 5

print(math.ceil(5.6))  # 6

# Bu math modulunu matematik olarak kullanmak istiyorum

import math as matematik

print(matematik.factorial(5))  # 120

# modul adini yazmak istemessem? Ama tum fonksiyolari dahil etsin.

from math import *

print(factorial(3))  # 6

# Peki bir modül içindeki fonksiyonların belli bir kısmını almak için ne yapacağız ? Bunun için hangi fonksiyonları
# alacağımızı özellikle belirtmemiz gerekiyor.

from math import factorial, floor

print(factorial(5))

print(ceil(4.2))  # bunu yapmazdi (daha onceden aktarmasaydik! )

# --------------------------------------------------------------------------------------------------------------

from math import *


def factorial(sayi):
    faktoriyel = 1
    print("Kendi Factorial fonksiyonum.")
    if sayi == 0 or sayi == 1:
        return 1
    while sayi >= 1:
        faktoriyel *= sayi
        sayi -= 1
    return faktoriyel


print(factorial(4))  # Out : Kendi Factorial fonksiyonum ; 24

# fakaaaatttt simdi tekrar import edersek python son  gordugu factorial fonksiyonunu calistirir.

from math import *

print(factorial(4))  # 24

import modul1

help(modul1)  # kendi basit modulumude boylece gormus oldum (modulume ayni klasorde olmadan ulastim nasil?)
# macintosh - library - frameworks - Python Framework - versions - lib - python3.8


