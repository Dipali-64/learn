a = "1"
b = "2"
print(a+b)

a = 1
b = 2 
print(a+b)

# The conversion of one data type into the other data type is known as type casting in python or type conversion in python.

a = "1"
b = "2"
print(int (a) + int (b)) 
# first it will convert string stored in a into integer and then it also convert string stored in b into integer and then add them


# Type casting types :
#  -> Explicit conversion => done via developer or programmer manually as per requirement
# -> Implicit conversion => done via python

string =  "15"
number = 7
string_number = int(string)
sum = string_number + number
print("The sum of both the number is :",sum)

c = 1.8
d = 7
print(c+d)