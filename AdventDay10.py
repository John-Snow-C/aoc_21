"""
Advent of code 2021 day 10
"""
from pprint import pprint # useful for debugging
import statistics

# -------------- functions
def checkline(line): # check line and return incorrect Y or N
    pos = 0
    incorrect = "N"
    while incorrect == "N" and pos < len(data[line]):
        tchar = data[line][pos]
        if tchar in ochar:
            cpos = ochar.index(tchar)
            clist.append(cchar[cpos])
        else:
            if tchar == clist[-1]:
                dummy = clist.pop(-1)
            else:
                incorrect = "Y"
                cexpected.append(clist[-1])
                cerrors.append(tchar)
        pos += 1
    return(incorrect)

def scoreline(chars): # count score and return line value
    s = 0
    for z in range(len(chars)):
        s = s * 5
        thischar = chars[z]
        thispos = cchar.index(thischar)
        thisval = cval2[thispos]
        s = s + thisval
    return(s)

# -------------- read data from input file and create list
#datastr = [line.strip() for line in open('Day10Example.txt')] # read test file
datastr = [line.strip() for line in open('Day10Input.txt')] # read live file
lastrow = len(datastr)
data = [[] for i in range(lastrow)]
for i in range(lastrow):
    data[i] = datastr[i]
# -------------- set up lists
ochar = ["(", "[", "{", "<"]
cchar = [")", "]", "}", ">"]
cval = [3, 57, 1197, 25137]
cval2 = [1, 2, 3, 4]
# -------------- read lines and check characters
clist = []
cexpected = []
cerrors = []
countlist = []
for line in range(lastrow):
    compcount = 0
    clist=[]
    ret = checkline(line)
    if ret == "N":
        clist.reverse()
        compcount = scoreline(clist)
        countlist.append(compcount)
print(statistics.median(countlist))
