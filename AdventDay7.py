"""
Advent of code 2021
"""

import sys
sys.setrecursionlimit(1500)

# function to sum digits from 1 to n
def recursion(n):
    if n == 1:
        return 1
    elif n ==0:
        return 0
    else:
        return n + recursion(n - 1)

data = [line.strip() for line in open('Advofcode input.txt')] # read file
#print(data) #DEBUG

crab_str = data[0].split(",")
#print(crab_str) #DEBUG

crab_list = [int(i) for i in crab_str]
#print(crab_list) #DEBUG

import statistics

# calculate mean value rounded to nearest integer
align = round((statistics.mean(crab_list)))
print ("align ",align)#DEBUG

leastfuel = 90000000
for a in range(align-10, align+10): # check values either side to find least
# calculate fuel
    fuel = 0
    for i in range(len(crab_list)):
        fuel = fuel + recursion(abs((crab_list[i] - a)))
    if fuel < leastfuel:
        leastfuel = fuel
    print ("align value", a, "fuel", fuel, "leastfuel now", leastfuel)
