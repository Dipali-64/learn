# required argumnets
def average(a,b):
    print("The average is : ",(a+b)/2)

average(1,5)

def name(fname,mname, lname):
    print("hello",fname,mname,lname)

name("Amy","Bobby","agrawal")

# default
def average(a=9,b=1):
    print("The average is : ",(a+b)/2)

average()
average(b=9)

def name(fname,mname = "Jhon" , lname="Whatson"):
    print("hello",fname,mname,lname)

name("Amy","Bobby","wheeler")

# keyword Arguments
# average(b=9,a=21)

# variable length arguments
def average(*number):
    sum = 0
    for i in number:
        sum = sum + i
    print("Average is :",sum/len(number))
    

average(5,6)


def average(*number):
    sum = 0
    for i in number:
        sum = sum + i
        # The return statement is used to return the value of the expression back to the calling function
    return sum/len(number)

c = average(5,6)
print(c)
