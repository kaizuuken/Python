
"""Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve
şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Weight / Height(m) *  height(m)

 If BMİ  18.5'un under -------> Thin

 If  BMI is between 18.5 and 25 ------> Normal

 If BMİ is between 25 and 30  --------> overweight

 BMİ is Over 30 -------------> Obese"""

print("""
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Body Mass Index Calculator
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
""")

weight =int(input("Kilonuzu Giriniz:"))
height =float(input("Boyunuzu giriniz:"))

bmi = weight/ (height*height)

if bmi <= 18.5:
    print("You are thin.")
elif 18.5<bmi<25:
    print("Your weight Normal")
elif 25<bmi<30:
    print("you are overweight.")
elif bmi>30:
    print("Get well soon, you are obese.")

###############################################

"""Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın."""

num1=int(input("1st Num:"))
num2=int(input("2nd Num:"))
num3=int(input("3rd Num:"))

if num1>=num2 and num1>=num3:
    print("Biggest Num:",num1)
elif num2>=num1 and num2>=num3:
    print("Biggest Num:",num2)
elif num3>=num2 and num3>=num1:
    print("Biggest Num:",num3)

"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD
   
    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
"""
print("#### Donem Ici Not Hesaplama Araci #####")
midterm1=int(input("1st midterm:"))
midterm2=int(input("2snd midterm:"))
final=int(input("Final exam:"))

average=((midterm1*0.30) + (midterm2*0.30) + (final*0.40))

if average >=90:
    print("AA")
elif 90>average>=85:
    print("BA")
elif 85>average>=80:
    print("BB")
elif 80>average>=75:
    print("CB")
elif 75>average>=70:
    print("CC")
elif 70>average>=65:
    print("DC")
elif 65>average>=60:
    print("DD")
elif 60>average>=55:
    print("FD")
elif 55>average>=50:
    print("FF")
elif average<50:
    print("Are we stuck again?")


"""
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan
üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , 
dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı ,
eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa,
ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o
Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.
Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, 
Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
abs(-4) 
4
"""

print("    Geometrik Sekil Hesaplama Islemi    ")

sekil=input("Ucgenin mi Tipini Bulmak Istiyorsunuz Dortgenin Mi?:")
if sekil == "Dortgen":
    Kenar1=int(input("1. Kenari Giriniz:"))
    Kenar2=int(input("2. Kenari Giriniz:"))
    Kenar3=int(input("3. Kenari Giriniz:"))
    Kenar4=int(input("4. Kenari Giriniz:"))
    if Kenar1==Kenar2==Kenar3==Kenar4:

        print("Girdiginiz Dortgen Bir Karedir.")
    else:
        print("Dikdortgen Girdiniz")
elif (sekil == "Ucgen"):
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if (a == b and a == c):
            print("Eşkenar Üçgen...")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen....")
        else:
            print("Çeşitkenar Üçgen...")
    else:
        print("Üçgen belirtmiyor...")

else:
    print("Geçersiz Şekil...")






