# #e.g 1  Create a list
# mylist1=[10,20,30,40,'a',10.4,"banana"]
# print(mylist1)
# mylist=list()      #empty list
# print(mylist)

# access individual items
# mylist=['apple','banana','cherry']
# print(mylist[0])
# print(mylist[-1])

# range of indexes
#mylist=['apple','banana','cherry','orange','kiwi','mango']
# print(mylist[2:5])
#print(mylist[-4:-1])

#change item value
# mylist=['apple','banana','cherry']
# print(mylist)
# mylist[0]='mango'
# print(mylist)

#read items using loop
# mylist=['apple','banana','cherry']
# for i in mylist:
#     print(i)

# check if item is in list (Search)
# mylist=['apple','banana','cherry']
# if 'apple' in mylist:
#     print("iten exist")
# else:
#     print("no item found")

#Length of list
# mylist=['apple','banana','cherry']
# print(len(mylist))

#add items in list append(), insert()
# mylist=['apple','banana','cherry']
# mylist.append("orange")     #add item at the end of list
# print(mylist)
# mylist.insert(1,'kiwi')    #add item to specific location
# print(mylist)

#remove item from list  pop() function
# mylist=['apple','banana','cherry']
# mylist.pop(0)
# print(mylist)

#remove item from list del keyword
# mylist=['apple','banana','cherry']
# del mylist[0]
# print(mylist)

#clear()  : to delete all items
# mylist=['apple','banana','cherry']
# mylist.clear()
# print(mylist)

# copy list
# mylist1=['apple','banana','cherry']
# mylist2=mylist1.copy()
# print(mylist2)
# mylist3=list(mylist1)
# print(mylist3)

# combine 2 lists
#using +
# list1=['a','b','c']
# list2=[10,20,30,40]
# list3=list1+list2
# print(list3)

# using loop statement
# list1=['a','b','c']
# list2=[10,20,30,40]
# for i in list2:
#     list1.append(i)
# print(list1)

# using extend()
list1=['a','b','c']
list2=[10,20,30,40]
list1.extend(list2)   #add values from list2 to list1
print(list1)
print(list2)

