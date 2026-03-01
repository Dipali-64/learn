#break 
for i in range(12):
    if(i==10):
        break
    print("5 x",i+1,"=",5*(i+1))

print("Exit")

# continue

for i in range(12):
    if(i==10):
        print("skip the iteration")
        continue
    print("5 x",i+1,"=",5*(i+1))


# do while loop emulation
i=0
while True:
    print(i)
    i = i+1
    if(i%7== 0):
        break