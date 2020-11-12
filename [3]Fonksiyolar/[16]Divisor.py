def disivor(num):
    disivors=[]
    for i in range(2,num+1):
        if num % i == 0:
            disivors.append(i)
    return disivors

while True:
    try:
        num = input("ENTER A NUMBER (Press 'q' For quit) :")
        if num=="q":
            print("The program is terminating ")
            break
        else:
            num=int(num)
            print("disivors:",disivor(num))
    except ValueError:
        print("Value Error ! Please Enter a Number.")


