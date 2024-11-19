"""
    CS121 W18
    KILO POUNDS CONVERSION CHART
    2/13/18
    PYTHON 3.6.4
"""

print("Kilograms     Pounds   |   Pounds     Kilograms")

kilo_count = 1
pound_count = 20
for x in range(99):
    print(kilo_count, "            ", round(kilo_count * 2.2, 1), "       ", pound_count, "            ",
          round(pound_count * 0.453592, 2))
    kilo_count += 2
    pound_count += 5

'''
test case should output 

Kilograms     Pounds   |   Pounds     Kilograms
1              2.2         20              9.07
3              6.6         25              11.34
5              11.0         30              13.61
7              15.4         35              15.88
9              19.8         40              18.14

for first 5
'''
