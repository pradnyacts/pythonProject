def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function()

@decorator_function
def display1():
    print("display function ran")
display1()








# def div(a,b):
#     print(a/b)
#
# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner
# div=smart_div(div)
# div(2,4)
