# #polymorphism and method overloading
# class Human:
#     def sayHello(self,name=None):
#         if name is not None:
#             print("Hello", name)
#         else:
#             print("hello")
# h=Human()
# h.sayHello("Scott")
# h.sayHello()            #method overloading: method with diff parameter: polymorphism. one method different forms

#e.g 2  method overloading and polymorphism
class Cal:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
c=Cal()
c.add()
c.add(10,20)
c.add(100,200,300)       #1 method and diff forms