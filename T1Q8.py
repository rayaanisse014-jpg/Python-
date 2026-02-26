######################################################################
# Millions and billions
#

# KEEP THE FOLLOWING LINES UNCHANGED

# Constants
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY
DAYS_PER_YEAR = 365 # IGNORING LEAP YEARS
MILLION = 1000000
BILLION = 1000000000

# INSERT SOLUTION BELOW
pass
# Millions of seconds → days
million = int(input('How many millions of seconds? '))
# Multiply the number of millions by one million to get the number of seconds, then divide by the above quantities to convert from seconds back to days.
second = million * MILLION
Day = second / (SECONDS_PER_MINUTE * MINUTES_PER_HOUR * HOURS_PER_DAY) 
print(f"{million} million seconds is {Day:.1f} days.")

# Billions of seconds → years
billion = int(input('How many billions of seconds? '))
# Compute the number of years it will take for that many billions of seconds to pass.
second = billion * 1000000000
years = second / (SECONDS_PER_MINUTE * MINUTES_PER_HOUR * HOURS_PER_DAY * DAYS_PER_YEAR)
print(f"{billion} billion seconds is {years:.1f} years.")
