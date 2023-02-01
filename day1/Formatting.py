name="john"
age=20
sal=20000
print("Name is: %s, Age is %d, sal is %g" %(name,age,sal ))
print("Name is: {}, Age is {}, sal is {}" .format(name,age,sal ))

#take input from user and type conversion
num1=int(input("Enter First no: "))
num2=int(input("Enter second no: "))
print(type(num1))    #<class 'str'>
print(type(num2))
print(num1+num2)   #concatenate string

#approach 2
num1=input("Enter First no: ")
num2=input("Enter second no: ")
print(type(num1))    #<class 'str'>
print(type(num2))
print(int(num1)+int(num2))   #concatenate string
