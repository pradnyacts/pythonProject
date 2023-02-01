#e.g1
# global_var=20
# def fun():
#     local_var=30
#     print(local_var)
#     print(global_var)
# fun()
# print(global_var)
# #print(local_var)    #NameError: name 'local_var' is not defined

#e.g 2
# xy=100    #global variable
# def cool():
#     xy=200
#     print("local",xy)   #local variable
# cool()
# print("Global", xy)

#e.g 3
# xy=100    #global variable
# def cool():
#     global xy
#     xy=200
#     print("local",xy)   #local variable
# cool()
# print("Global", xy)

#e.g 4
# x=100
# def cool():
#     #global x
#     x=300
#     print(x)
# #cool()
# print(x)

#e.g 5
# def cool():
#     global x
#     x=100
#     print(x)
# cool()
# print(x)

#e.g 6