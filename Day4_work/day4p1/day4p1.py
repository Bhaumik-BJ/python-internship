#function with no return statement
def my_fun():
    print("Hello Everyone")

my_fun()

#function with return statement
def my_function(name):
    return name

name = my_function("Bhaumik Joshi")
print(name)

#function with multiple return statement
def my_function():
    name = "Bhaumik Joshi"
    contact ="9106718508"
    return name , contact

name, contact = my_function()
print("Name:", name)
print("Contact:", contact)



