"""
    CS121 W18
    PRINTS THE CURRENT TIME IN PST
    RIVER
    1/18/18
    PYTHON 3.6.4
"""

import time

# get the current time
current_time = time.time()

# calculate the current second, minute, and hour
total_seconds = int(current_time)
current_second = total_seconds % 60
total_minutes = total_seconds // 60
current_minute = total_minutes % 60
total_hours = total_minutes // 60
current_hour = total_hours % 24

# convert to pst by subtracting 8 hours
current_hour -= 8

# print the current time
print("The current time is", current_hour, ":",
      current_minute, ":", current_second, "PST")
