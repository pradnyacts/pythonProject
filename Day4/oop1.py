#e.g1
# class MyClass:
#     def myfun(self):
#         pass
#     def display(self,name):
#         print(name)
# mc=MyClass()
# mc.myfun()
# mc.display("pradnya")

#e.g 2
# class MyClass:
#     def m1(self):
#         print("this is instance method")
#     @staticmethod
#     def m2(self,number):
#         print(number)
# mc1=MyClass()
# mc1.m1()     #calling instance method using object
# #mc1.m2(100,200)
# MyClass.m2(100,200)   #calling static method using class name

#e.g 3
# class MyClass():
#     a,b=10,20   #class variable
#     def add(self):
#         print(self.a+self.b)      # to access class variable , access using self.
#
#     def mul(self):
#         print(self.a*self.b)
# mc=MyClass()
# mc.add()
# mc.mul()

#e.g 4 Global, class, local
# i,j=15,25     #global variable
# class MyClass:
#     a,b=10,20     #class variable
#     def add(self,x,y):         #local variables
#         print(x+y)              #local variables to method
#         print(self.a+self.b)    #access class variable using self keyword
#         print(i+j)              #Global variables
# mc=MyClass()
# mc.add(40,50)

#e.g 5
# a,b=15,25     #global variable
# class MyClass:
#     a,b=10,20     #class variable
#     def add(self,a,b):         #local variables
#         print(a+b)              #local variables to method
#         print(self.a+self.b)    #access class variable using self keyword
#         print(globals()['a']+globals()['b'])              #gloabl variables
# mc=MyClass()
# mc.add(40,50)

#e.g 6 multiple objects for single class
# class MyClass():
#     def display(self,name):
#         print("This is display method", name)
# ob1=MyClass()
# ob1.display("prad")
# ob2=MyClass()
# ob2.display("john")

#.eg 7 Constructor:
# class MyClass:
#     def __init__(self):
#         print("this is constructor")
#     def m1(self):
#         print("hello")
#     def m2(self,x,y):
#         return(x+y)
# mc=MyClass()    #constructor will be executed automatically
# mc.m1()         #method we need to call explicitly
# res=mc.m2(10,20)
# print(res)

#e.g 8 constructor with arguments
# class MyClass:
#     name="john"
#     def __init__(self,name):
#         print(name)
#         print(self.name)
# mc=MyClass("prad")   #passing parameter to constructor

#e.g 9: create emp class , create constructor which accept 3 parameter eid, empname, salary.
# Print the data using display() method
# class Emp():
#
#     def __init__(self,eid,name,sal):
#         self.eid=eid      #convert local variable to Class variable
#         self.name=name
#         self.sal=sal
#     def dislay(self):
#         print(self.eid,self.name,self.sal)
#
# mc=Emp(100,"john",20000)
# mc.dislay()
# mc2=Emp(200,"prad",30000)
# mc2.dislay()

#e.g 10
class Emp():

    def __init__(self,eid,name,sal):
        self.eid=eid      #convert local variable to Class variable
        self.name=name
        self.sal=sal
    def __str__(self):      #Constructor only use for strings
        return(self.name)


e1=Emp(100,"john",20000)
print(e1)


















