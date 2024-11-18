"""
        CS121 W18
        KILO POUNDS CONVERSION CHART
        RIVER HILL
        2/13/18
        PYTHON 3.6.4
    """
kiloCount = 1
poundCount = 20
print(kiloCount, round(kiloCount * 2.2, 1), poundCount, "9")
for x in range(99):
    kiloCount += 2
    poundCount += 5
    print(kiloCount, round(kiloCount * 2.2, 1), poundCount, round((poundCount * 0.453592) + 0.49, 2))

'''
test case should output 

1 2.2 20 9.09
3 6.6 25 11.36
5 11.0 30 13.63
7 15.4 35 15.9
9 19.8 40 18.16

'''