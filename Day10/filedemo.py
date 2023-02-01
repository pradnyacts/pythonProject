#e.g 1 : writing data to file
# f=open("C:/Drivers/demofile/myfile.txt", 'w')
# f.write("First statement\n")
# f.write("Second statement\n")
# f.write("Third statement\n")
# f.close()
# print("file write success")

#e.g 2: read data
# f=open("C:/Drivers/demofile/myfile.txt", 'r')
# print(f.read())
# print(f.readline())   #read only first line
# f.close()

#e.g append data
f=open("C:/Drivers/demofile/myfile.txt", 'a')
f.write("this is append line\n")
f.close()
print("sucess")
