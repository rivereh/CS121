"""
    CS121 W18
    POPULATION
    RIVER HILL
    PRINTS POPULATION FOR NEXT 5 YEARS GIVEN CURRENT POPULATION
    1/16/18
    PYTHON 3.6.4
"""

currentPopulation = 312032486
secondsInYear = 31536000
birthsInYear = secondsInYear / 7
deathsInYear = secondsInYear / 13
immigrantsInYear = secondsInYear / 45

for x in range(1, 6):
    totalPopulationInYear = round(birthsInYear + immigrantsInYear - deathsInYear) * x \
                            + (currentPopulation - 1)
    print(totalPopulationInYear)

# Test case should output 314812582, 317592679, 320372776, 323152873, 325932970
