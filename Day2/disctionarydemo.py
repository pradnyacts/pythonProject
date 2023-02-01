#create dictionary
# d={101:'x',102:'y',103:'z'}
# print(d.keys())
# print(d.values())
# print(d)

#access items
# d={
#     "brand":"honda",
#     "model": "civic",
#     "year":2021
# }
# print(d["brand"])
# #using get()
# x=d.get("brand")
# print(x)

#change values in dictionary
# d={
#     "brand":"honda",
#     "model": "civic",
#     "year":2021
# }
# d["year"]=2022
# print(d)

#reading items using loop
# d={
#     "brand":"honda",
#     "model": "civic",
#     "year":2021
# }
# for i in d:
#     print(i)  #prints only keys from dictionary
#     print(d[i])  # print values
#
# for i in d.values():    #print values
#     print(i)
#
# for x,y in d.items():
#     print(x,y)    #print both keys and values

# key exist in dictionary
# d={
#     "brand":"honda",
#     "model": "civic",
#     "year":2021
# }
# if "brand" in d:
#     print("item exist")
# else:
#     print("NO")

#total items in dictionary
# d={
#     "brand":"honda",
#     "model": "civic",
#     "year":2021
# }
#
# print(len(d))

#add items to dictionary
# d={
#     "brand":"honda",
#     "model": "civic",
#     "year":2021
# }
#
# d["color"]="red"
# print(d)

#remove item from dictionary
# d={
#     "brand":"honda",
#     "model": "civic",
#     "year":2021
# }
# d.pop("year")
# print(d)

# del d["year"]
# print(d)
#
# d.clear()    # clear all items
# print(d)


#copy dictionary
d1={
    "brand":"honda",
    "model": "civic",
    "year":2021
}
d2=d1
print(d2)
d3=d1.copy()
print(d3)