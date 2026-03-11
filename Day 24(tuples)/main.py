# tuple
tup = (1,5,6)
print(type(tup),tup)

# tuples are ordered collection of data items. They store multiple items in a single variable. Tuples items are seperated by commas and enclosed within round brackets ().Tuples are unchangeable meaning we can not alter them after creation.

print(tup[0])
print(tup[-1])
print(tup[2])

if 5 in tup:
    print("Yes 5 is present in this tuple")
