contries = ("Spain","Italy","India","England","Germany")
temp = list(contries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
contries = tuple(temp)
print(contries)

# you can concatinate two tupples

tuple1=(0,1,2,3,2,3,1,3,2)
res = tuple1.count(3)
print("count :",res)
res = tuple1.index(2) #first ocuurance of that element
print(res)