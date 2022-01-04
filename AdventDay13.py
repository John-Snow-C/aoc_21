"""
Advent of code 2021 day 13
"""
from pprint import pprint # useful for debugging
import statistics # useful for median

# -------------- functions

def f_read_file(f_runtype, f_rundata):
    f_lastrow = f_lastcol = 0
    if f_runtype == "E":
        f_datastr = [line.strip() for line in open('InputExample.txt')]
    else:
        f_datastr = [line.strip() for line in open('InputLive.txt')]
    f_lastrow = len(f_datastr)
    if f_rundata == "S":
        f_data = [[] for i in range(f_lastrow)]
        for i in range(f_lastrow):
            f_data[i] = f_datastr[i]
    else:
        f_lastcol = len(f_datastr[0])
        f_data = [[0]*f_lastcol for i in range(f_lastrow)]
        for i in range(f_lastrow):
            f_data[i] = list(map(int, f_datastr[i]))
    if f_runtype == "E":
        pprint(f_data)
        print("---- test input ----")
    return f_lastrow, f_lastcol, f_data

def f_find_max(f_dots):
    f_colmax = f_rowmax = 0
    for i in range(len(f_dots)):
        if f_dots[i][0] > f_colmax:
            f_colmax = f_dots[i][0]
        if f_dots[i][1] > f_rowmax:
            f_rowmax = f_dots[i][1]
    return f_colmax, f_rowmax

def f_printgrid(f_grid, f_colmax, f_rowmax):
    f_line = ""
    for f_row in range(f_rowmax+1):
        for f_col in range(f_colmax+1):
            f_line = f_line + f_grid[f_row][f_col]
        print(f_line)
        f_line = ""
    return()

def f_fill_grid(f_grid, f_dots):
    f_filledgrid = f_grid[:]
    for i in range(len(f_dots)):
        f_col = f_dots[i][0]
        f_row = f_dots[i][1]
        f_filledgrid[f_row][f_col] = "#"
    return f_filledgrid

def f_fold (f_grid, f_currfold, f_colmax, f_rowmax):
    f_fold_type = f_currfold[0]
    f_fold = f_currfold[1]
    f_foldx2 = f_fold * 2
    if f_fold_type == "y":
        f_newcolmax = f_colmax
        f_newrowmax = f_fold - 1
        f_newgrid = [["."]*(f_newcolmax+1) for i in range(f_newrowmax+1)]
        for row in range(f_rowmax+1):
            for col in range(f_colmax+1):
                if row < f_fold:
                    f_newgrid[row][col] = f_grid[row][col]
                else:
                    if f_grid[row][col] == "#":
                        f_newgrid[f_foldx2 - row][col] = f_grid[row][col]
    else:
        f_newcolmax = f_fold - 1
        f_newrowmax = f_rowmax
        f_newgrid = [["."]*(f_newcolmax+1) for i in range(f_newrowmax+1)]
        for col in range(f_colmax+1):
            for row in range(f_rowmax+1):
                if col < f_fold:
                    f_newgrid[row][col] = f_grid[row][col]
                else:
                    if f_grid[row][col] == "#":
                        f_newgrid[row][f_foldx2 - col] = f_grid[row][col]
    return f_newgrid, f_newcolmax, f_newrowmax

def f_count(f_grid, f_colmax, f_rowmax):
    f_count = 0
    for f_row in range(f_rowmax+1):
        for f_col in range(f_colmax+1):
            if f_grid[f_row][f_col] == "#":
                f_count += 1
    return f_count

# -------------- set global values and read data from input file
runtype = "L" # L for live E for example
rundata = "S" # S for strings, I for integers
lastrow, lastcol, data = f_read_file (runtype, rundata)

dots = []
row = data[0].split(",") # get first dot
x = eval(row[0])
y = eval(row[1])
nextdot = [x , y]
dots.append(nextdot)
i=1
while len(data[i]) > 0: # create rest of dots list
    row = data[i].split(",")
    x = eval(row[0])
    y = eval(row[1])
    nextdot = [x , y]
    dots.append(nextdot)
    i +=1
i += 1 # move past blank row and get first fold
folds = []
foldtext = (data[i])[11: ]
nexttext = foldtext.split("=")
x_or_y = nexttext[0]
foldline = eval(nexttext[1])
nextfold = [x_or_y, foldline]
folds.append(nextfold)
for j in range (i+1, lastrow): # create rest of folds list
    foldtext = (data[j])[11: ]
    nexttext = foldtext.split("=")
    x_or_y = nexttext[0]
    foldline = eval(nexttext[1])
    nextfold = [x_or_y, foldline]
    folds.append(nextfold)

# -------------- process
dots.sort()
colmax, rowmax = f_find_max(dots)
grid = [["."]*(colmax+1) for i in range(rowmax+1)]
filledgrid = f_fill_grid(grid, dots)

for i in range(len(folds)):
    currfold = folds[i]
    newgrid, newcolmax, newrowmax = f_fold(grid, currfold, colmax, rowmax)
    grid = newgrid[:]
    colmax = newcolmax
    rowmax = newrowmax
f_printgrid(grid, colmax, rowmax) #DEBUG
# part 1 code countx = f_count(grid, colmax, rowmax)
# part 1 codeprint("count is", countx)


