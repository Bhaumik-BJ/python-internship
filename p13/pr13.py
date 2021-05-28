Num1 = int(input("Enter the Number1:"))
Num2 = int(input("Enter the Number2:"))
Num3 = int(input("Enter the Number3:"))


if Num1 < Num3:
    if Num1 < Num2:
        print("Number1 is Smaller")
    else:
        print("Number2 is Smaller")

else:
    if Num3 < Num2:
        print("Number3 is Smaller")
    else:
        print("Number2 is Smaller")