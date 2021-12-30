"""
Advent of code 2021 to run ,alt.<ctrl><shift><enter>
"""
from pprint import pprint # useful for debugging

def getcells(r, c): # get adjacent cells
    cells = []
    if c != 0: # if not first col find "left"
        cells.append([r,c-1])
    if c < lastcol - 1: # if not last col find "right"
        cells.append([r,c+1])
    if r != 0: # if not first row find "up"
        cells.append([r-1,c])
    if r < lastrow - 1: # if not last row find "down"
        cells.append([r+1,c])
    return(cells)

def getvals(lrup): # get values from adjacent cells
    vals = []
    for cellnum in range(len(lrup)):
        row = lrup[cellnum][0]
        col = lrup[cellnum][1]
        vals.append(data[row][col])
    return(vals)

def oneval(rcpair): # get one value from cell
    val = 0
    cellr = rcpair[0]
    cellc = rcpair[1]
    val = data[cellr][cellc]
    return(val)


def fillbasin(lp, r, c,): # fill one basin from lowpoint
# NB always work on cellstodo first occurence
# initial pass is lowpoint valie, row and column
    cellsdone = []
    cellstodo = []
    thiscellval = 0
    addcell=[r,c] # add passed lowpoint to cells done
    cellsdone.append(addcell)
    newcells = getcells(r,c) # get cells around lowpoint into cell to do
    cellstodo = newcells
    while len(cellstodo) > 0:
        thiscellval = oneval(cellstodo[0])
        nrow = cellstodo[0][0]
        ncol = cellstodo[0][1]
        if cellstodo[0] in cellsdone: # already done so remove and loop
            cellstodo.remove(cellstodo[0])
        elif thiscellval == 9: # a 9 so put in value and pop into done
            basins[nrow][ncol] = 9
            popcell = cellstodo.pop(0)
            cellsdone.append(popcell)
        else: # get surrounding cells then find if is in basin
            newcells = getcells(nrow, ncol)
            for nc in range(len(newcells)): # split before appending
                cellstodo.append(newcells[nc])
            chkvals = getvals(newcells)
            inbasin = "N"
            for x in range(len(chkvals)):
                if  thiscellval > chkvals[x]:
                    inbasin = "Y"
            if inbasin == "Y":
                basins[nrow][ncol] = lp # put low point value in
                popcell = cellstodo.pop(0)
                cellsdone.append(popcell)

# -------------- read data from input file and create integer list
#datastr = [line.strip() for line in open('Day9Example.txt')] # read test file
datastr = [line.strip() for line in open('Day9Input.txt')] # read live file
lastrow = len(datastr)
lastcol = len(datastr[0])
lowpoints = 0
data = [[0]*lastcol for i in range(lastrow)]
for i in range(lastrow):
    data[i] = list(map(int, datastr[i]))

# -------------- mark low points in copy
basins = [[0]*lastcol for i in range(lastrow)]
lowpoints = []
lowval = 10
for row in range(lastrow):
    for col in range(lastcol):
        chknum = data[row][col]
        lrup = getcells(row, col)
        chkvals = getvals(lrup)
        lowest = "Y"
        for x in range(len(chkvals)):
            if chknum > chkvals[x]:
                lowest = "N"
        if lowest == "Y":
            basins[row][col] = lowval # put lowpoint marker in (10, 11 etc.)
            templow = [lowval, row, col]
            lowpoints.append(templow) # add to list of lowpoints
            lowval +=1
# -------------- fill basins
for i in range(len(lowpoints)):
    fillbasin(lowpoints[i][0], lowpoints[i][1],lowpoints[i][2])

# create single list so count works
all = []
for x in range(lastrow):
    for y in range(lastcol):
        all.append(basins[x][y])
# find all basin sizes
basinsize = []
for i in range(len(lowpoints)):
    basinsize.append(all.count(lowpoints[i][0]))
basinsize.sort()
b1 = basinsize[-1]
b2 = basinsize[-2]
b3 = basinsize[-3]
print("Basins", b1, b2, b3)
print("Answer ", b1*b2*b3)
