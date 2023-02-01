# #e.g1  Single Inheritance
# class A:
#    def m1(self):
#        print("this is m1 from Class A")
#
# class B(A):                              #declaring inheritance : class B inherits from class B
#     def m2(self):
#         print("this is m2 method from class B")
#
# b=B()     #declare object for class B
# b.m1()      #access method of class A using class B object
# b.m2()

#e.g 2 Single inheritance
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)
b=B()
b.m1()
b.m2()
