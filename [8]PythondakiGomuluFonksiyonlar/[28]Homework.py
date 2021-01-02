"""
Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.

         [(3,4),(10,3),(5,6),(1,9)]

Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.


Not : map() fonksiyonunu kullanmaya çalışın.
"""

liste=[(3,4),(10,3),(5,6),(1,9)]
def area(liste):
    return liste[0]*liste[1]

print(list(map(area,liste))) # [12, 30, 30, 9]

"""Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen 
belirten kenarları bulunduran listeyi ekrana yazdırın.

Not: filter() fonksiyonunu kullanmaya çalışın."""

liste = [(3,4,5),(6,8,10),(3,10,7)]

def triangle(liste):
    if abs(liste[0]+liste[1] > liste[2]) and abs(liste[0]+liste[2] > liste[1] and abs(liste[1]+liste[2]>liste[0])):
        return True
    else:
        return False
print(list(filter(triangle,liste))) # [(3, 4, 5), (6, 8, 10)]

"""
Elinizde şöyle bir liste bulunsun.

    [1,2,3,4,5,6,7,8,9,10]

Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.

Not: İlk önce filter() fonksiyonu ile çift sayıları ayıklayın. Daha sonra reduce() fonksiyonunu kullanın.

"""
from functools import reduce

liste = [1,2,3,4,5,6,7,8,9,10]
evens=[]
def even(x):
    if x % 2 == 0:
        return True
    else:
        return False


evens=print(list(filter(even,liste)))
tatals=0
even=[2, 4, 6, 8, 10]
for i in even:
    tatals+=i
print(tatals)

"""
Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.

        isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.
Not: zip() fonksiyonunu kullanmaya çalışın
"""

names=["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
surnames=["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

name=print(list(zip(names,surnames)))

for i,j in zip(names,surnames):
    print(i,j)

# Kerim Yılmaz
# Tarık Öztürk
# Ezgi Dağdeviren
# Kemal Atatürk
# İlkay Dikmen
# Şükran Kaya
# Merve Polat