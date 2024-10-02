class headerprint:
    def __init__(self):
        print('---------------------------------------')
        print("Welcome to TNEB")
        print("----------------------------------------")
class footerprint:
    def __init__(self):
        print('---------------------------------------')
        print("Please Pay the bill on time other wise sub will be disconnect please pay on time")
        print("----------------------------------------")
class elebillcal():

    def __init__(self,units):
        self.units=units
    def billcal(self):
        # program for calculating electricity bill in Python

        if (self.units <= 100):
            payAmount = self.units * 1.5
            fixedcharge = 25.00
        elif (self.units <= 200):
            payAmount = (100 * 1.5) + (self.units - 100) * 2.5
            fixedcharge = 50.00
        elif (self.units <= 300):
            payAmount = (100 * 1.5) + (200 - 100) * 2.5 + (self.units - 200) * 4
            fixedcharge = 75.00
        elif (self.units <= 350):
            payAmount = (100 * 1.5) + (200 - 100) * 2.5 + (300 - 200) * 4 + (self.units - 300) * 5
            fixedcharge = 100.00
        else:
            payAmount = 0
            fixedcharge = 1500.00

        Total = payAmount + fixedcharge;
        print(f"Electicity bill={Total}")


units=int(input("please enter the number of units you consumed in a month"))
h=headerprint()
b=elebillcal(units)
b.billcal()
f=footerprint()