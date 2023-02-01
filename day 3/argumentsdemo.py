#e.g1
# def fun(i,j):
#     print(i,j)
# fun(10,20)        #positional arguments: position matter
# fun(j=20,i=10)    #Keyword arguments: position doesnot matter

#e.g 2   default values assigned to positional arguments
# def fun(i,j=10):
#     print(i,j)
# fun(100,200)
# fun(100)         #will take default j value 10

#e.g 3 Keyword arguments
# def greet(name,greetmsg):
#     print(greetmsg+" "+name)
# greet(name="pradnya", greetmsg="hello")
# greet(greetmsg="hello",name="pradnya")

#e.g 4
# def fun(a,b,c):
#     print(a,b,c)
# fun(10,20,30)    #positional
# fun(a=10,b=20,c=30)     #keyword
# fun(b=20,a=10,c=30)     #keyword
# fun(10,20,c=30)         #positional and keyword
# #fun(10,b=20,30)         #SyntaxError: positional argument follows keyword argument
# #positional argument must appear before keyword argument
# #fun(a=10,20,30)         #SyntaxError: positional argument follows keyword argument
# fun(10,30,b=30)          #TypeError: fun() got multiple values for argument 'b'

#e.g 5  function can return multiple values
def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
print(largest(100,200))
print(largest(20,10))



