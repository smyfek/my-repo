#! /usr/bin/env python
import random

lotterynumbers = []

for i in range (0,5):
    number = random.randint(1,39)
    # checking if numbers have been already picked
    while number in lotterynumbers:
        number = random.randint(1,39)
    # now we have a unique number, let's upend it to our list.
    lotterynumbers.append(number)
#Sort the list in ascending Orderer
lotterynumbers.sort()

# Lucky stars numbers

thunderball = []

for i in range (0,1):
    number = random.randint(1,14)
    # checking if numbers have been already picked
    while number in thunderball:
        number = random.randint(1,14)
    # now we have a unique number, let's upend it to our list.
    thunderball.append(number)
#Sort the list in ascending Orderer
thunderball.sort()

# Display lottery numbers
print()
print("Your Numbers for today are: ")
print (lotterynumbers)
print()
print("Your Thunderball is: ")
print (thunderball)
print()