#! /usr/bin/env python
import random

lotterynumbers = []

for i in range (0,5):
    number = random.randint(1,50)
    # checking if numbers have been already picked
    while number in lotterynumbers:
        number = random.randint(1,50)
    # now we have a unique number, let's upend it to our list.
    lotterynumbers.append(number)
#Sort the list in ascending Orderer
lotterynumbers.sort()

# Lucky stars numbers

luckystars = []

for i in range (0,2):
    number = random.randint(1,12)
    # checking if numbers have been already picked
    while number in luckystars:
        number = random.randint(1,12)
    # now we have a unique number, let's upend it to our list.
    luckystars.append(number)
#Sort the list in ascending Orderer
luckystars.sort()

# Display lottery numbers
print()
print("Your Euromillions numbers for today are: ")
print (lotterynumbers)
print()
print("Your lucky stars are: ")
print (luckystars)
print()