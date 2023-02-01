# s="welcome"
# s=str("Welcome")
# name=str()
# name=""

#mutable:can't change value of variable
#immutable: can change value of variable
#string is immutable

# str1="welcome"
# print(id(str1))
# str1=str1+"to python"
# print(id(str1))

# + and *
# str1="welcome"
# print(str1+"python") #concatenation
# print(str1*10)  #print multiple times

#slicing
# str="welcome"
# print(str[1:3])    #el
# print(str[:6])  #welcom
# print(str[2:])   #lcome
# print(str[::-1])   #reverse a string
# print(str[1:-1])   #elcom
# print(str[1:-2])   #elco

#ord() and chr()
# print(ord('A'))    #ASCII char
# print(chr(65))     #get char

#max(), min(), len()
# print(max('abc'))
# print(min('abc'))
# print(len('abc'))

#in and not in operators
# s="Welcome"
# print("Come" in s)
# print("come" in s)
# print("come" not in s)

#string comparison
# print("tim"=="tie")
# print("free"!="freedom")
# print("arrow">"aron")
# print("right">="left")
# print("teeth"=="tee")
# print("yellow"<="fellow")
# print("abc">"")

#testing strings true/false
# s= "Welcome to python"
# print(s.isalnum())
# print("Welcome".isalpha())
# print("2012".isdigit())
# print("first number".isidentifier())
# print(s.islower())
# print("WELCOME".isupper())
# print(" ".isspace())

#searching for substring
# s= "Welcome to python"
# print(s.endswith("thon"))
# print(s.startswith("good"))
# print(s.find("come"))
# print(s.count("o"))

#converting function
# s="String in PYTHON"
# s1=s.capitalize()
# print(s1)
#
# s2=s.title()
# print(s2)
#
# s3=s.lower()
# print(s3)
#
# s4=s.upper()
# print(s4)
#
# s5=s.swapcase()
# print(s5)
#
# s6=s.replace("in", "on")
# print(s6)


# reverse a string
#1.
s="welcome"
rev_str=""
for i in s:
    rev_str=i+rev_str
print(rev_str)

#2
print(s[::-1])