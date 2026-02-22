import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

if(timestamp>0 and timestamp<12):
    print("Good Morning,Sir")
elif(timestamp>=12 and timestamp<4):
    print("Good Afternoon,Sir")
elif(timestamp>=4 and timestamp<=24):
    print("Good Evening,Sir")