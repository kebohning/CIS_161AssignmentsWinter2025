#Week 3 Python Assignment
#Kate Bohning

#Part 1

name = input("What is your name? ")
print(f"Hello {name}")

#Part 2 and 3
age = input("How old are you? ")
age = int(age)
print(f"In five years you will be {age + 5} years old")
print("you must use an F string to concatenate integers and strings ")
print("python implies an input() as a string. it must be made an integer to use math functions")

#Part 4 and 5

wage = input("What is your hourly wage? ")
hours = input("How many hours have you worked?")

wage = float(wage)
hours = float(hours)

print(f"Your weekly wage is: ${wage * hours}")
print(f"Your annual gross wage is: ${wage * hours * 52}")

