print("""
***************************************
User Login
***************************************
""")

sys_username = "Kaizuuken"
sys_password = "Yusufwashere3"

username=input("User Name:")
password=input("Password:")

if username == sys_username and sys_password !=password :
    print("You entered the password incorrectly!")
elif username != sys_username  and sys_password == password :
    print("You entered the  username   incorrectly!.")
elif username != sys_username and password !=sys_password :
    print("You entered the password and username incorrectly!")
else:
    print("Login successful")

