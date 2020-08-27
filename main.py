import datetime

now = datetime.datetime.now()

print("Time: {}".format(now.strftime("%H:%M:%S")))
Your_Hour = int(input("What hour do want to wake up?  "))
Your_Minute = int(input("What minute do want to wake up?  "))
Your_Second = int(input("What second do want to wake up?  "))

while True:
    if Your_Hour == datetime.datetime.now().hour and Your_Minute == datetime.datetime.now().minute \
            and Your_Second == datetime.datetime.now().second:
        print("\nIt's time!")
        break
    else:
        continue
