"""
Advent of code 2021
"""
from pprint import pprint # useful for debugging

def getvals(r, c): # create list of adjacent numbers
    vals = []
    if r != 0: # if not first row find "up"
        vals.append(eval(data[r-1][c]))
    if r < lastrow - 1: # if not last row find "down"
        vals.append(eval(data[r+1][c]))
    if c != 0: # if not first col find "left"
        vals.append(eval(data[r][c-1]))        
    if c < lastcol - 1: # if not last col find "right"
        vals.append(eval(data[r][c+1]))       
    return(vals)

# -------------- read data from input file
data = [line.strip() for line in open('Advofcode input.txt')] # read file
lastrow = len(data)
lastcol = len(data[0])
risktot = 0

for row in range(lastrow):
    for col in range(lastcol):
        chknum = eval(data[row][col])
        chkvals = getvals(row, col)
        lowest = "Y"
        for x in range(len(chkvals)):
            if not chknum < chkvals[x]:
                lowest = "N"
        if lowest == "Y":
            risktot = risktot + chknum + 1
print ("Risk total", risktot)
