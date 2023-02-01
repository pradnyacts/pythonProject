def square(x):
    return x*x
def cube(x):
    return x*x*x
def my_map(func, arg_list):      #func as argument
    result=[]
    for i in arg_list:
        result.append(func(i))
    return result
squares= my_map(square,[1,2,3,4,5])
cube= my_map(cube,[1,2,3,4,5])

print(squares)
print(cube)

