#python default argument

def sum1(a=5, b=10):
    print("sum1:",a+b)

sum1(10,20)
sum1()

#python keyword argument
def sum2(a,b):
    print("sum2:",a+b)

sum2(a=10, b=30)

#python variable length argument

def sum3(*num):
    sum3= 0
    for n in num:
        sum3 = sum3 + n
    print("sum3:", sum3)


sum3(10,20,30)