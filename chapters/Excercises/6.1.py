"""
    CS121 W18
    PENTAGONAL NUMBER GEN 6.1
    RIVER HILL
    2/13/18
    PYTHON 3.6.4
"""


# function for getting pentagonal number at n
def get_pentagonal_number(n):
    return n * ((3 * n) - 1) / 2


# print the first 100 pentagonal numbers with 10
# on each line
count = 0
while count < 100:
    count += 1
    print(int(get_pentagonal_number(count)), end=" ")
    if count % 10 == 0:
        print()
