import random
import time

"""

Sayi Tahmmini Oyunu



1 ile 40 Arasinda sayiyi tahmin edin.



"""

random_num=random.randint(1,40) # 1 ile 40 dahil 1-40 araliginda rastgele sayi uret.
estimation_rights=7
while True:
    estimation = int(input("Estimated:"))
    if estimation <random_num:
        print("information is being questioned...")
        time.sleep(1)  # programi 1 saniyeliyeligine dondur.
        print("Enter a higher number!")
        estimation_rights-=1
    elif estimation>random_num:
        print("information is being questioned....")
        time.sleep(1)
        print("Enter a smaller Num!.")
        estimation_rights-=1
    else:
        print("Information is being questioned...")
        time.sleep(1)
        print("Congratulations You Found The Num in {} guesses!!.".format(8-estimation_rights))
        break
    if estimation_rights == 0:
        print("Your guesswork is over.")
        print("Num is :",random_num)
        break
"""Binary Search yontemi ile log 2^40=5.32  tahminde veya 1-1000 arasindaki bir sayiyi log2^1000=9.96 tahminde  , 
1 ile 1T Arasindaki sayiyi tahmin etmek icin 30 tahmin yeterli olucaktir.
Bu yontem ortadaki sayiyi soyleyerek yarisi veya 20 kati seklinde ortadaki sayidan yola cikarak ilerliyor 
1 ile 40 arasinda ornegin 20-yuksek-30 alcak deiyse 25 yuksek dediyse 27 gibi """




