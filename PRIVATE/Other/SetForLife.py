#! /usr/bin/env python
import random

lotterynumbers = []

for i in range (0,5):
    number = random.randint(1,47)
    # checking if numbers have been already picked
    while number in lotterynumbers:
        number = random.randint(1,47)
    # now we have a unique number, let's upend it to our list.
    lotterynumbers.append(number)
#Sort the list in ascending Orderer
lotterynumbers.sort()

# Lucky stars numbers

lifeball = []

for i in range (0,1):
    number = random.randint(1,10)
    # checking if numbers have been already picked
    while number in lifeball:
        number = random.randint(1,10)
    # now we have a unique number, let's upend it to our list.
    lifeball.append(number)
#Sort the list in ascending Orderer
lifeball.sort()

# Display lottery numbers
print()
print("Your Numbers for today are: ")
print (lotterynumbers)
print()
print("Your Life Ball is: ")
print (lifeball)
print()