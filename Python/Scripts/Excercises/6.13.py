"""
    CS121 W18
    SUM SERIES
    RIVER HILL, JIN
    2/20/18
    PYTHON 3.6.4
"""

temp = 0
print("i  m(i)\n")
for x in range(1, 21):
    temp += x / (x + 1)
    print(str(x) + ")", round(temp, 4))
