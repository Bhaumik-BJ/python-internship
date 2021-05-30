#global and local variable in python

x = 10 #This is global value

def my_fun():
    x = 15 #This is local value we can't assign this value outside the function
    print("Inner value of x is:",x)



my_fun()
print("Outer value of x is:",x)