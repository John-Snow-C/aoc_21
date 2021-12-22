"""
Advent of code 2021
"""
from pprint import pprint # useful for debugging

rawdata = [line.strip() for line in open('Advofcode input.txt')] # read file
for i in range(len(rawdata)): # replace "->" with ","
    s = rawdata[i]
    s = s.replace(' -> ',',')
    rawdata[i] = s
# create array for x and y values
xylist = [[0] for i in range(len(rawdata))]
for i in range(len(rawdata)): # split into x1 to y2 numbers
    xylist[i] = [int(i) for i in rawdata[i].split(',')]
# Find highest x and y values to define grid to fill in
xmax = ymax = 0
for j in range(len(xylist)):
    if xmax < xylist[j][0]:
        xmax = xylist[j][0]
    if xmax < xylist[j][2]:
        xmax = xylist[j][2]
    if ymax < xylist[j][1]:
        ymax = xylist[j][1]
    if ymax < xylist[j][3]:
        ymax = xylist[j][3]
xmax = xmax+1
ymax = ymax+1
# *********************************************************************
# NB, array rows are y values, so x and y reversed in values! *********
# *********************************************************************
grid = [[0]*ymax for i in range(xmax)]
# read in data to complete grid
for k in range(len(xylist)):
    x1 = xylist[k][0]
    y1 = xylist[k][1]
    x2 = xylist[k][2]
    y2 = xylist[k][3]
    if x1==x2:
        if y2>y1:
            for m in range(y1,y2+1):
                grid[m][x1] = grid[m][x1] + 1
        else:
            for m in range(y2,y1+1):
                grid[m][x1] = grid[m][x1] + 1
    elif y1==y2:
        if x2>x1:
            for m in range(x1,x2+1):
                grid[y1][m] = grid[y1][m] + 1
        else:
            for m in range(x2,x1+1):
                grid[y1][m] = grid[y1][m] + 1  
# code for diagonals
    else:
        fill = abs(x2-x1) + 1 # calculate cells to fill
        if x2>x1:
            xstart = x1
            ystart = y1
            if y2>y1:
                move = 1
            else:
                move = -1
        else:
            xstart = x2
            ystart = y2
            if y1>y2:
                move = 1
            else:
                move = -1
        for n in range(fill):
            grid[ystart][xstart] += 1
            xstart +=1
            ystart +=move
# Count up any where value is greater than 1
dangerspots = 0
for n in range(xmax):
    for o in range(ymax):
        if grid[n][o] > 1:
            dangerspots = dangerspots + 1
print ("dangerspots", dangerspots)
