class employee:

    def EMP(self):
        print("Name: Bhaumik Joshi")
        print("Designation: Python Developer")


class employee1(employee):

    def EMP1(self):

        print("salary:20000")


e = employee1()
e.EMP()
e.EMP1()