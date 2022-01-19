"""
Advent of code 2021 day 15
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

def f_getnodes(f_r, f_c, f_visited, f_lastrow, f_lastcol):
    f_nodes = []
    if f_r > 0:
        if f_visited[f_r - 1][f_c] != "V":
            f_nodes.append("U")
    if f_r < (f_lastrow - 1):
        if f_visited[f_r + 1][f_c] != "V":
            f_nodes.append("D")
    if f_c > 0:
        if f_visited[f_r][f_c - 1] != "V":
            f_nodes.append("L")
    if f_c < (f_lastcol - 1):
        if f_visited[f_r][f_c + 1] != "V":
            f_nodes.append("R")
    return f_nodes

def f_getvalues(f_nodes, f_data, f_grid, f_row, f_col, f_unvis):
    f_newU = f_newD = f_newR = f_newL = 9999
    for i in range(len(f_nodes)):
        if f_nodes[i] == "U":
            f_newU = f_data[f_row - 1][f_col] + grid[f_row][f_col]
            if f_newU < grid[f_row - 1][f_col]:
                grid[f_row - 1][f_col] = f_newU
                f_tempu = [f_row - 1, f_col, f_newU]
                f_unvis.append(f_tempu)
        elif f_nodes[i] == "D":
            f_newD = f_data[f_row + 1][f_col] + grid[f_row][f_col]
            if f_newD < grid[f_row + 1][f_col]:
                grid[f_row + 1][f_col] = f_newD
                f_tempu = [f_row + 1, f_col, f_newD]
                f_unvis.append(f_tempu)
        elif f_nodes[i] == "L":
            f_newL = f_data[f_row][f_col - 1] + grid[f_row][f_col]
            if f_newL < grid[f_row][f_col - 1]:
                grid[f_row][f_col - 1] = f_newL
                f_tempu = [f_row, f_col - 1, f_newL]
                f_unvis.append(f_tempu)
        elif f_nodes[i] == "R":
            f_newR = f_data[f_row][f_col + 1] + grid[f_row][f_col]
            if f_newR < grid[f_row][f_col + 1]:
                grid[f_row][f_col + 1] = f_newR
                f_tempu = [f_row, f_col + 1, f_newR]
                f_unvis.append(f_tempu)
        else:
            print("f_getvalues CODING ERROR!")
    return f_unvis

def f_nextnode(f_unvis):
    f_lowval = 9999
    f_lowidx = 9999
    for nxt in range(len(f_unvis)):
        if f_unvis[nxt][2] < f_lowval:
            f_lowval = f_unvis[nxt][2]
            f_lowidx = nxt
    f_r = f_unvis[f_lowidx][0]
    f_c = f_unvis[f_lowidx][1]
    f_unvis.pop(f_lowidx) 
    return f_r, f_c, f_unvis

def f_expandby5(f_data, f_lastrow, f_lastcol):
    f_newlastrow = f_lastrow * 5
    f_newlastcol = f_lastcol * 5
    f_newdata = [[0]*f_newlastrow for i in range(f_newlastcol)]
    for f_r in range(f_lastrow): # put in original tile
        for f_c in range(f_lastcol):
            f_newdata[f_r][f_c] = f_data[f_r][f_c]
    for f_r in range(f_lastrow): # fill in tiles to right
        for f_c in range(f_lastcol):
            f_val = data[f_r][f_c]
            for f_xcol in range(f_lastcol + f_c, f_newlastcol, f_lastcol):
                f_val += 1
                if f_val > 9:
                    f_val = 1
                f_newdata[f_r][f_xcol] = f_val
    for f_c in range(f_newlastcol): # fill in tiles down
        for f_r in range(f_lastrow):
            f_val = f_newdata[f_r][f_c]
            for f_xrow in range(f_lastrow + f_r, f_newlastrow, f_lastrow):
                f_val += 1
                if f_val > 9:
                    f_val = 1
                f_newdata[f_xrow][f_c] = f_val
    return f_newdata, f_newlastrow, f_newlastcol
    
# -------------- set global values and read data from input file
runtype = "L" # L for live E for example
rundata = "I" # S for strings, I for integers
lastrow, lastcol, data = f_read_file (runtype, rundata)
newdata, lastrow, lastcol = f_expandby5(data, lastrow, lastcol)
data = newdata[:]

path = [[0,0]]
grid = [[9999]*lastrow for i in range(lastcol)]
visited = [[""]*lastrow for i in range(lastcol)]
data[0][0] = 0
grid[0][0] = 0
visited[0][0] = "V"
unvis = []

# -------------- process
r = c = prog = 0 
done = "N"
while done == "N":
    prog += 1
    if prog % 1000 == 0:
        print("Progress", prog)   
    nodes = f_getnodes(r, c, visited, lastrow, lastcol)
    unvis = f_getvalues(nodes, data, grid, r, c, unvis)
    visited[r][c] = "V"
    r, c, unvis = f_nextnode(unvis)
    if len(unvis) == 0:
        done = "Y"
print("answer", grid[lastrow - 1][lastcol - 1])                                        
