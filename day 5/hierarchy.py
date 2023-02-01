#e.g 1
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)
class C(A):
    i,j=3,5
    def m3(self):
        print(self.i*self.j)

c=C()     #can only access methods from C and A
c.m1()
c.m3()

b=B()     #can only access methods from B and A
b.m1()
b.m2()
