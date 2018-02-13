    """
        CS121 W18
        KILO POUNDS CONVERSION CHART
        RIVER HILL
        2/13/18
        PYTHON 3.6.4
    """

    print("Kilograms     Pounds")

    count = 1
    print(count, "            ", round(count * 2.2, 1))
    for x in range(99):
        count += 2
        print(count, "            ", round(count * 2.2, 1))

    '''
    test case should output 
    
    1              2.2
    3              6.6
    5              11.0
    7              15.4
    9              19.8
    
    for first 5
    '''