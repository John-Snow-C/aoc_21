"""
Advent of code 2021 day 17
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

def f_step (f_xpos, f_ypos, f_xv, f_yv):
    f_xpos = f_xpos + f_xv
    f_ypos = f_ypos + f_yv
    if f_xv !=0:
        if f_xv > 0:
            f_xv = f_xv - 1
        else:
            f_xv = f_xv + 1
    f_yv = f_yv - 1

    return f_xpos, f_ypos, f_xv, f_yv  

def f_status(f_xpos, f_ypos, f_x1, f_x2, f_y1, f_y2):
    f_status = ""
    if f_xpos >= f_x1 and\
       f_xpos <= f_x2 and\
       f_ypos >= f_y1 and\
       f_ypos <= f_y2:
        f_status = "H" # i.e. in target so hit
    elif (f_ypos < 0) and\
         (abs(f_ypos) > abs(f_y1)):
        f_status = "M" # i.e. below target so miss
    else:
        f_status = "C" # i.e. continue steps
    return f_status
   
# -------------- set global values and read data from input file
runtype = "L" # L for live E for example
rundata = "S" # S for strings, I for integers
lastrow, lastcol, data = f_read_file (runtype, rundata)
instring = data[0]
xystring = instring[13:]
ystart = xystring.index("y")
xstr = xystring[:ystart-2]
ystr = xystring[ystart:]
dot = xstr.index(".")
x1 = eval(xstr[2:dot])
x2 = eval(xstr[dot + 2:])
dot = ystr.index(".")
y1 = eval(ystr[2:dot])
y2 = eval(ystr[dot + 2:])

# -------------- process

status = "C"
hitlist = []
for initxv in range(1,500):
    print("initxv", initxv)
    for inityv in range(-200, 900):
        xpos = ypos = 0
        xv = initxv
        yv = inityv
        status = "C"
        while status == "C":
            xpos, ypos, xv, yv = f_step(xpos, ypos, xv, yv) # do next step
            status = f_status(xpos, ypos, x1, x2, y1, y2) # Continue, Hit, Miss
        if status == "H":
            hitlist.append([initxv, inityv])
#pprint(hitlist)
print("answer is", len(hitlist))      











