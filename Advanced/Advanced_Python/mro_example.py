class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(C, B):  # Multiple Inheritance
    #def show(self):
        #print('D')
    pass
obj = D()
obj.show()  # Output: B (B comes before C in the hierarchy)
#print(D.__mro__)  # MRO Order
