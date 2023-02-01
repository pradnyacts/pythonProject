#create set
# set1={'apple',2,3,4,5}   #unordered
# print(set1)

#access values
# myset={'apple','banana','kiwi'}
# for i in myset:
#     print(i)

#item exist in set(search)
# myset={'apple','banana','kiwi'}
# if 'banana' in myset:
#     print("item exist")
# else:
#     print("not exist")

#add item to set :add()----single item and update(): multiple items
# myset={'apple','banana','kiwi'}
# #myset.add("orange")
# myset.update(["mango", "grapes"])
# print(myset)

# find no of items in set
# myset = {'apple', 'banana', 'kiwi'}
# print(len(myset))

#remove items from set: remove() and discard()
#if item doesn't exist in set and user try to remove then discard gives no error. but remove gives error
# myset = {'apple', 'banana', 'kiwi'}
# # myset.remove('banana')
# # print(myset)
# # myset.remove('xyz')  #KeyError: 'xyz'
# # print(myset)
# myset.discard('apple')
# myset.discard('xyz')
# print(myset)

# clear all items in set
# myset = {'apple', 'banana', 'kiwi'}
# # myset.clear()
# # print(myset)
# del myset
# print(myset)    #NameError: name 'myset' is not defined

# join 2 sets: UNION
# set1={'apple', 'banana', 'kiwi'}
# set2={1,2,3,4}
# set3= set1.union(set2)
# print(set3)

# join using update()
set1={'apple', 'banana', 'kiwi'}
set2={1,2,3,4}
set1.update(set2)
print(set1)

