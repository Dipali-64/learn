# A Function is a block of code that performs specific task whenever it is called.

a = 9
b = 8
gMean = (a*b)/(a+b)
print(gMean)

c = 8
d = 10
gMean = (c*d)/(c+d)
print(gMean)

def calculateMean(a,b):
    mean = (a*b)/(a+b)
    print("mean is",mean)

def findMax(a,b):
    if(a>b):
        print("First number is greater")
    elif(b>a):
        print("Second number is greater")
    else:
        print("Both are equals")

findMax(a,b)
calculateMean(a,b)
findMax(c,d)
calculateMean(c,d)

# pass => process aage ka program