names = "Hello,Dipali"
print(len(names))
print(names[0:5])


fruit = "mango"
len1 = len(fruit)
print(len1)
print(fruit[0:4]) 
# including 0 but not 4

print(fruit[0:len(fruit)-3])
# start => 0 
# len(fruit)-1 => 5-3 => 2
# 0 1 2 3 4 
# m a n g o
# ma => 0 is inclusive but 2 is exclusive

print(fruit[-3:-1])
# start => len(fruit)-3 => 2
# end => len(fruit)-1 => 4
# ng => 2 is inclusive,4 is exclusive
print(fruit[-1:-3])


# Quick Quiz

nm = "Harry"
print(nm[-4:-2])