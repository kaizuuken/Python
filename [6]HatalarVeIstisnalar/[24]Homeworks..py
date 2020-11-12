
"""Problem 1
Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.

liste = ["345","sadas","324a","14","yusuf"]

Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın. Bunu yaparken try,except bloklarını kullanmayı unutmayın.

"""

list = ["345","sadas","324a","14","ysf"]
for i in list:
    try:
        i = int(i)
        print(i)
    except ValueError:
        print("Element is not an integer")

"""Problem 2
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, eğer sayı çift ise return ile bu değeri
 dönsün. Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın. Daha sonra, içinde çift ve tek sayılar
  bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın."""

def oddeven(num):
    if num %2 == 0:
        return num
    else:
        raise ValueError # burayi yazmasak 34 2 None None None Olarak ilerleyecekti. Raise ile hatayi firlatmis olduk.

list1 = [34,2,1,3,33,100,61,1800]

for i in list1:
    try:
        print(oddeven(i))
    except ValueError:
        pass

