#e.g 1
# print("This is starting point")
# print("This is starting point")
# print("This is starting point")
# try:
#     print(x)
# except:
#     print("Exception ocuured")
#
# print("This is end point")
# print("This is end point")
# print("This is end point")

#e.g 2
# print("This is starting point")
# print("in progress")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("zero exception")
#
# print("prog completed")

#e.g 3 multiple except blocks: try except else finally
# try:
#     num1,num2=10,0
#     res=num1/num2
#     print(res)
# except ZeroDivisionError:
#     print("ZeroDivisionError exception")
# except SyntaxError:
#     print("SyntaxError")
# except:
#     print("Exception handled")
# else:
#     print("no exception")
# finally:
#     print("always execute")

#user defined exceptions
def enterage(num):
    if num<0:
        raise ValueError("only integers are allowed")
    if num%2==0:
        print("even")
    else:
        print("odd")
# enterage(10)
# enterage(5)
# enterage(0)
num=-1
try:
    enterage(num)
except ValueError:
    print("value error")
print("compelted")







