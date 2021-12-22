"""
Advent of code 2021
"""
# Read file
n = [line.strip() for line in open('Advofcode input.txt')]
horiz = 0
dep = 0
aim = 0
# loop through changing horizontal and depth values depending on list
for i in range(len(n)):
    direction = n[i][0]
    amount = int(n[i][-1])
    if direction == "f":
        horiz = horiz + amount
        dep = dep + (amount * aim)
    elif direction == "d":
        aim = aim + amount
    else:
        aim = aim - amount
print ("Final horizontal and depth values are: ", horiz, dep)
print ("Answer for puzzle is: ", horiz * dep)

