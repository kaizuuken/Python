print("""
*************************
Kullanici Girisi Programi
*************************
""")

sys_username="Kaizuuken"
sys_password="Yusufwashere3"
Right=3
while True:
    username=input("Kullanici Adi:")
    password=input("Parola:")
    if username == sys_username and sys_password != password:
        print("You entered the password incorrectly!")
        Right-=1
    elif username != sys_username and sys_password == password:
        print("You entered the  username   incorrectly!.")
        Right -= 1
    elif username != sys_username and password != sys_password:
        print("You entered the password and username incorrectly!")
        Right -= 1
    else:
        print("Login successful")

    if Right==0:
        print("Your right to enter is finished")
        break
