#e.g 1  super and method overriding
# class A:
#     def m1(self):
#         print("This is m1 from A class")
# class B(A):
#     def m1(self):                             #method overriding
#         print("This is m1 from class B")
#         super().m1()                        # super to call parent method
#
# b=B()
# b.m1()

# #e.g 2
# class A:
#     a,b=10,20
#
# class B(A):
#     i,j=100,200
#     def m(self,x,y):
#         print(x+y)    #local variables
#         print(self.i+self.j)    #class variables
#         print(self.a+self.b)    #class variables
#
# b=B()
# b.m(1000,2000)

# #e.g2 Overriding variables
# class Parent:
#     name="scott"
# class Child(Parent):
#     name="john"        #overriding variable
#     def test(self):
#         print(super().name)      #to access parent variable
# c=Child()
# print(c.name)         #will print name from child (latest)
# c.test()              #to access paren variable


# e.g 3:Overriding methods
class Bank:
    def roi(self):
        return 0
class XBank(Bank):
    def roi(self):        #method overriding
        return 10
class YBank(Bank):
    def roi(self):        #method overriding
        return 20
x=XBank()
print(x.roi())
y=YBank()
print(y.roi())