# Kullanicidan aldiginiz 3 sayiyi carparak ekrana yazdirin.Ekrana yazdirma islemini format metoduyla yapmaya calisin
print("multiplying 3 numbers entered ")

a = int(input("1st num:"))
b = int(input("2nd num:"))
c = int(input("3rd num:"))

operation = (a * b * c)

print("{} x {} x {} = {}.".format(a, b, c, operation))

# Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

#
# body mass index : weight / Height(m)*Height(m)

print("Body Mass Index")

weight = int(input("Enter your weight:"))
height = float(input("Enter your Height:"))

BMI = (weight/ (height * height))
print("Your Body Mass Index:", BMI)

# Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın
# ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.

print("vehicle fuel calculation")

fuel = float(input("How much fuel does the vehicle consume per 1 km:"))
day = int(input("How many kilometers are you driving a day?:"))
work = int(input("How Many Days are u going to work?:"))

expense = (fuel * day * work)

print("Your Expense:", expense)

# Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.

print("Registration Form")

name = input("Name:")
surname = input("Surname:")
no = int(input("Phone Number:"))

print("Name:{}\nSurname:{}\nTel:{}".format(name, surname, no))

confirmation = input("Do you confirm?(yes veya no):")
print("\n\n\nBilgileriniz Kaydedildi.")

# Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

num1 = int(input("num1:"))
num2 = int(input("num2:"))

num1, num2 = num2, num1

print("Values after change\n {} {}".format(num1, num2))

# Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

print("---finding the hypotenuse---")
a = int(input("side1:"))
b = int(input("side2:"))

hyp = (((a ** 2) + (b ** 2)) ** 0.5)

print("{} and {} hypotenuse of triangle is :{}".format(a, b, hyp))


