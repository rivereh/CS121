"""
    CS121 W18
    PRINTS POPULATION FOR NEXT 5 YEARS 
    GIVEN CURRENT POPULATION
    RIVER
    1/16/18
    PYTHON 3.6.4
"""

current_population = 312032486
seconds_in_year = 31536000
births_in_year = seconds_in_year / 7
deaths_in_year = seconds_in_year / 13
immigrants_in_year = seconds_in_year / 45

for x in range(1, 6):
    total_population_in_year = round(births_in_year + immigrants_in_year - deaths_in_year) * x \
        + (current_population - 1)
    print(total_population_in_year)

# test case should output 314812582, 317592679, 320372776, 323152873, 325932970
