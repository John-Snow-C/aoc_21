"""
Advent of code 2021 day 11
"""
from pprint import pprint # useful for debugging
import statistics # useful for median

# -------------- functions

def read_file(runtype, rundata):
    if runtype == "E":
        datastr = [line.strip() for line in open('InputExample.txt')]
    else:
        datastr = [line.strip() for line in open('InputLive.txt')]
    lastrow = len(datastr)
    if rundata == "S":
        data = [[] for i in range(lastrow)]
        for i in range(lastrow):
            data[i] = datastr[i]
    else:
        lastcol = len(datastr[0])
        data = [[0]*lastcol for i in range(lastrow)]
        for i in range(lastrow):
            data[i] = list(map(int, datastr[i]))
    if runtype == "E":
        pprint(data)
        print("---- input ----")
    return(lastrow, lastcol, data)


def add_one_to_all():
    for r in range(lastrow):
        for c in range(lastcol):
            data[r][c] = data[r][c] + 1

def find_ready_to_flash():
    for r in range(lastrow):
        for c in range(lastcol):
            if data[r][c] > 9:
                if len(flash_ready) == 0:
                   flash_ready.append([r,c])
                else:
                    tlist=(r,c)
                    if tlist not in flash_ready:
                       flash_ready.append(tlist)

         
def octopus_flash(list, ft):
    r,c = unpack(list)
    data[r][c] = 0 # set to flashed this step
    ft = ft + 1
    if r > 0: # row above
        if c > 0:
            process_adjacent(r-1, c-1) # up left
        process_adjacent(r-1, c) # one above
        if c < (lastcol-1):
            process_adjacent(r-1, c+1) # up right
    if r < (lastrow-1): # row below
        if c > 0:
            process_adjacent(r+1, c-1) # down left
        process_adjacent(r+1, c) # one below
        if c < (lastcol-1):
            process_adjacent(r+1, c+1) # down right
    if c > 0:
        process_adjacent(r, c-1) # left
    if c < (lastcol-1):
        process_adjacent(r, c+1) # right
    return(ft)
        
        
def unpack(list):
    row = list[0]
    col = list[1]
    return(row, col)

def process_adjacent(pr, pc):
    if data[pr][pc] != 0:
        data[pr][pc] = data[pr][pc] +1
        if data[pr][pc] > 9:
            tlist=(pr,pc)
            if tlist not in flash_ready:
                flash_ready.append(tlist)

def zero_count():
    zcount = 0
    for r in range(lastrow):
        for c in range(lastcol):
            if data[r][c] == 0:
                zcount = zcount + 1
    return(zcount)

# -------------- set global values and read data from input file
runtype = "L" # L for live E for example
rundata = "I" # S for strings, I for integers
lastrow, lastcol, data = read_file (runtype, rundata)

# -------------- other variables
flash_ready = []
flash_total = 0
flashed = 0
step = 1

# -------------- process
while flashed < 100:
    add_one_to_all()
    flash_ready = []
    find_ready_to_flash()
    while len(flash_ready) > 0:
        flash_total = octopus_flash(flash_ready[0], flash_total)
        flash_ready.pop(0)
    flashed = zero_count()
    print("Step", step, "flashed", flashed)
    step = step + 1
