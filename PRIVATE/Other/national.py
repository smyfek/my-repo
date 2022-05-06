#! /usr/bin/env python
import random

lotterynumbers = []

for i in range (0,6):
    number = random.randint(1,59)
    # checking if numbers have been already picked
    while number in lotterynumbers:
        number = random.randint(1,59)
    # now we have a unique number, let's upend it to our list.
    lotterynumbers.append(number)
#Sort the list in ascending Orderer
lotterynumbers.sort()

# Lucky stars numbers

# Display lottery numbers
print()
print("Your National lottey numbers for today are: ")
print (lotterynumbers)
print()