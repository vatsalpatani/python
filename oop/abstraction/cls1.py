class RBI:
    def Interest(self):
        pass

class SBI(RBI):
    def Interest(self):
        print("SBI Interest is 3%")

class HDFC(RBI):
    def Interest(self):
        print("HDFC Interest is 2%")


obj1 = SBI()
obj2 = HDFC()

obj1.Interest()
obj2.Interest()

# output  :
#     SBI Interest is 3%
#     HDFC Interest is 2%