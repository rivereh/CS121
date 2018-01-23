"""
    CS121 W18
    WELCOME PROJECT
    RIVER HILL
    ASKS USER FOR NAME AND WELCOMES THEM
    1/23/18
    PYTHON 3.6.4
"""
import time

currentTime = time.time()

totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = (totalHours % 12) - 8

name = input("Enter a name: ")
print("Welcome,", name, "\b!")

print("The time is", str(currentHour) + ":" + str(currentMinute) + ":" + str(currentSecond))

# test case should output "Hello, name!"

