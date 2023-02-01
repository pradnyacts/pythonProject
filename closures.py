def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func
hi_func=outer_func("hi")
hello_func=outer_func("hello")
hi_func()
hello_func()




# def outer_func(msg):
#     message= msg
#     def inner_func():
#         print(message)
#     return inner_func
# hi_func=outer_func("hi")
# hello_func=outer_func("hello")
# hi_func()
# hello_func()

# def outer_func():
#     message= 'hi'
#     def inner_func():
#         print(message)
#     return inner_func
# my_func=outer_func()
# #print(my_func.__name__)
# my_func()

