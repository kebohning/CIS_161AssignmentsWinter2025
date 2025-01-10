#Kate Bohning
#CS Winter Term 2025
#Week 1

import datetime
from calendar import month

#Part 1
print("Weclome to my program!")

petType = "Mexican Street Dog"
petName = "Chili Bean Macias"
petPronoun = "his"

print(f"My dog is a {petType} and {petPronoun} name is {petName}")

#Part 2
name = "Kate"
age = 35
year_saving = 45

print(f"Hello {name}! you are currently {age} years old. in 10 years you will be {age + 10}.")
print(f"If you save ${year_saving} each year, in 5 years you will have saved ${year_saving * 5}")
print(f"Your average monthly savings is ${year_saving / 5}")

#Part 3
jan = datetime.datetime.now()

def is_even(number):
  return number % 2 == 0

if(is_even(jan.month)) == True:
    days = 30
if(is_even(jan.month)) == False:
    days = 31
if(jan.month) == 2:
    days = 28

print(f"there are {days * 24 * 60 * 60} seconds in this month")

