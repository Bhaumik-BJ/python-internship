class Scheme:

    def __init__(self, scheme_id, scheme_name, outgoing_rate, message_charge):
        self.scheme_id = scheme_id
        self.scheme_name = scheme_name
        self.outgoing_rate = outgoing_rate
        self.message_charge = message_charge

    def fun1(self, Scheme_id, Scheme_name , Outgoing_rate, Message_charge):
        sc = Scheme(Scheme_id, Scheme_name , Outgoing_rate, Message_charge)
        ls.append(sc)

    def display(self):
        print("Scheme_id: ", sc.scheme_id)
        print("Scheme_name: ", sc.scheme_name)
        print("Outgoing_Rate: ", sc.outgoing_rate)
        print("Message_charge: ", sc.message_charge)



class Customer(Scheme):

    def __init__(self, cust_id, name, mobile_no):
        self.cust_id = cust_id
        self.name = name
        self.mobile_no = mobile_no

    def  fun2(self, Cust_id, Name, Mobile_no):
        cs = Customer(Cust_id, Name, Mobile_no)
        ls1.append(cs)

    def display(self):
        print("Customer Id:", cs.cust_id)
        print("Customer name:", cs.name)
        print("Customer Mobile Number: ", cs.mobbile_no)

ls =[]
ls1 =[]
c = Customer()
c.fun1(14254, 'summer_offer', 30, 10)
c.fun2(91043, 'Bhaumik', 9106718508)
c.display()


