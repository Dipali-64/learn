# l = [3,5,7]
# print(l)
# print(type(l))
# print(l[0])
# print(l[1])
# print(l[2])

# list are ordered collection of data items.
# They store multiple items in a single variables
# list items are seperated by commas and enclosed within square brackets.
# lists are changeable meaning we can alter them after creation.

marks = [90,80,70,"harry",True]
# print(marks)
# As we can see,a single list can contain items of different data types.

print(marks[-3])
print(marks[len(marks)-3])  #first convert it into posistive index by using len

if "harry" in marks:
    print("Yes")
else:
    print("No")

if "hary" in "harry":
    print("yes")


print(marks[1:4:2]) #jump index

# list comprehension
lst = [i*i for i in range(4)]
print(lst)

lst = [i*i for i in range(10) if i%2==0]
print(lst)