x = int(input("Enter the Starting Number:"))
y = int(input("Enter the Ending Number:"))

for x in range(y+1):

    if x % 3 != 0:
        continue

    print("value is :", x)



