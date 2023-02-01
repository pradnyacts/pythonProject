#e.g 1
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)
class C(B):
    i,j=5,2
    def m3(self):
        print(self.i*self.j)
c=C()
c.m1()
c.m2()
c.m3()
