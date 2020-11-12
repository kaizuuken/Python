print("""
****************************
Welcome to ATM Program!
Operation;

1.Balance inquiry

2.Pay Into

3.Withdraw Money

Press 'q' to exit the program.
****************************
""")

balance=1000

while True:
    operation = input("Select Action:")
    if operation == "q":
        print("We hope you come again.")
        break
    elif operation == "1":
        print("Your Balance Is {}.".format(balance))

    elif operation == "2":
        payinto=int(input("enter quantity:"))
        balance+=payinto
    elif operation == "3":
        Withdraw=int(input("Plase enter quantity:"))
        if balance - Withdraw < 0:
            print("Your balance is insufficient. Please enter a value in the range 0-{}.".format(balance))
            continue  # Bunu silsemde de islemi yapip en basa dondu.
        else:
            balance = balance - Withdraw


    else:
        print("Invalid Action.")


