"""
Advent of code 2021 day 18
"""
from pprint import pprint # useful for debugging
import statistics # useful for median
import math # to get rounding functions

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

def f_make_nlist(f_str): # create list with numbers
    f_nlist = []
    i = 0
    while i < (len(f_str)):
        if f_str[i] == "[" or f_str[i] == "," or f_str[i] == "]":
            f_nlist.append(f_str[i])
            i += 1
        else:
            if f_str[i+1] == "[" or f_str[i+1] == "," or f_str[i+1] == "]":
                f_nlist.append(eval(f_str[i])) # single digit number
                i += 1
            else:
                f_2dig = f_str[i]+f_str[i+1]
                f_nlist.append(eval(f_2dig)) # two digit number
                i += 2
    return f_nlist

def f_print_nlist(f_nlist): # print number list in more readable form
    f_str = ""
    for i in range(len(f_nlist)):
        if f_nlist[i] == "[" or f_nlist[i] == "," or f_nlist[i] == "]":
            f_str = f_str + f_nlist[i]
        else:
            f_str = f_str + str(f_nlist[i])
    print("nlist", f_str)
    input("-------------------")
    return

def f_make_slist(f_nlist): # create list with "N"s
    f_slist = []
    for i in range(len(f_nlist)):
        if f_nlist[i] == "[" or f_nlist[i] == "," or f_nlist[i] == "]":
            f_slist.append(f_nlist[i])
        else:
            f_slist.append("N")
    return f_slist

def f_print_slist(f_slist): # print string list in more readable form
    f_str = ""
    for i in range(len(f_slist)):
        f_str = f_str + f_slist[i]
    print("slist", f_str)
    input("-------------------")
    return

def f_add_num(f_nlist, f_newnum): # add next number
    f_newlist = ["["]
    for i in range(len(f_nlist)):
        f_newlist.append(f_nlist[i])
    f_newlist.append(",")
    f_addlist = f_make_nlist(newnum)
    for i in range(len(f_addlist)):
        f_newlist.append(f_addlist[i])
    f_newlist.append("]")
    return f_newlist

def f_find_explode_pair(f_slist):
    f_pairlist = []
    for i in range(4, len(f_slist) - 8): # find pairs
        f_test = ""
        for j in range(i,i+5):
            f_test = f_test + f_slist[j]
        if f_test == "[N,N]":
            f_pairlist.append(i)
    f_found = "N"
    while (len(f_pairlist) > 0) and (f_found == "N"): #find if 4 "["s to left
        j = f_pairlist[0]
        f_leftbracket= 0
        while (j > 0) and (f_leftbracket < 4):
            if f_slist[j] == "[":
                f_leftbracket += 1
            elif f_slist[j] == "]":
                f_leftbracket -= 1
            j -= 1
        if f_leftbracket >= 4:
            f_explodepos = f_pairlist[0]
            f_found = "Y"
        else:
            f_pairlist.pop(0)
    if f_found == "N":
        f_explodepos = 0
    return f_explodepos

def f_do_explode(f_nlist, f_explodepos, f_slist):
    f_leftval = f_nlist[f_explodepos + 1]
    i = f_explodepos
    f_foundnum = "N"
    while (i > 0) and (f_foundnum == "N"): # find first num to left
        i -= 1
        if f_slist[i] == "N" : #found number, check if in pair
            f_foundnum = "Y"
    if f_foundnum == "Y":
        f_nlist[i] = f_nlist[i] + f_leftval #add to left number
    f_rightval = f_nlist[f_explodepos + 3]
    i = f_explodepos + 3
    f_foundnum = "N"
    while (i < (len(f_slist)-1)) and (f_foundnum == "N"): # find num to right
        i +=1
        if f_slist[i] == "N":
            f_foundnum = "Y"
    if f_foundnum == "Y":
        f_nlist[i] = f_nlist[i] + f_rightval
    for i in range(4): #replace pair with 0
        f_nlist.pop(f_explodepos)
    f_nlist[f_explodepos] = 0
# remove and put in 0
    return f_nlist

def f_checkregnum(f_slist, f_i):
    f_max = len(f_slist) - 4
    f_lofpair = []
    if f_i > f_max:
        f_lofpair = "No"
    else:
        f_lofpair = f_slist[f_i-1] + \
                    f_slist[f_i] + \
                    f_slist[f_i+1] + \
                    f_slist[f_i+2] + \
                    f_slist[f_i+3]
    f_rofpair = []
    if f_i < 2:
        f_rofpair = "No"
    else:
        f_rofpair = f_slist[f_i-3] + \
                    f_slist[f_i-2] + \
                    f_slist[f_i-1] + \
                    f_slist[f_i] + \
                    f_slist[f_i+1]
    if f_lofpair == "[N,N]" or f_rofpair == "[N,N]":
        f_foundnum = "N"
    else:
        f_foundnum = "Y"
    return f_foundnum

def f_find_split(f_slist, f_nlist):
    i = 0
    f_foundnum = "N"
    while (i < (len(f_slist)-1)) and (f_foundnum == "N"): # find first num
        i += 1
        if f_slist[i] == "N" : # found number
            if f_nlist[i] > 9: # check if big enough to split
                f_foundnum = "Y"
    if f_foundnum == "Y":
        f_splitpos = i
        f_splitnum = f_nlist[i]
    else:
        f_splitpos = 0
        f_splitnum = 0
    return f_splitpos, f_splitnum

def f_do_split(f_nlist, f_splitpos):
    f_num = (f_nlist[f_splitpos]/2)
    f_lnum = math.floor(f_num)
    f_rnum = math.ceil(f_num)
    f_nlist.pop(f_splitpos)
    f_nlist.insert(f_splitpos,"]")
    f_nlist.insert(f_splitpos,f_rnum)
    f_nlist.insert(f_splitpos,",")
    f_nlist.insert(f_splitpos,f_lnum)
    f_nlist.insert(f_splitpos,"[")
    return f_nlist

def f_find_pairs(f_slist):
    f_pairlist = []
    for i in range(0, len(f_slist) - 4): # find pairs
        f_test = ""
        for j in range(i,i+5):
            f_test = f_test + f_slist[j]
        if f_test == "[N,N]":
            f_pairlist.append(i)
    return f_pairlist

def f_replace_pair(f_nlist, f_pos):
    f_lnum = (f_nlist[f_pos + 1] * 3)
    f_rnum = (f_nlist[f_pos + 3] * 2)
    f_mag = f_lnum + f_rnum
    for f_pop in range(5): # remove pair
        f_nlist.pop(f_pos)
    f_nlist.insert(f_pos,f_mag) # insert magnitude
    return f_nlist

# -------------- set global values and read data from input file
runtype = "L" # L for live E for example
rundata = "S" # S for strings, I for integers
lastrow, lastcol, data = f_read_file (runtype, rundata)

# -------------- process
maxmag = 0
for r in range(lastrow):
    for s in range(lastrow):
        if r != s: #Ignore same pair
            nlist = f_make_nlist(data[r]) # get first num
            slist = f_make_slist(nlist)
            newnum = data[s] # get next num
            nlist = f_add_num(nlist, newnum) # add numbers
            slist = f_make_slist(nlist)
            explodepos = f_find_explode_pair(slist)
            splitpos, splitnum = f_find_split(slist, nlist)
            while explodepos !=0 or splitpos > 0:
                if explodepos != 0:
                    nlist = f_do_explode(nlist, explodepos, slist)
                elif splitpos > 0:
                    nlist = f_do_split(nlist, splitpos)
                slist = f_make_slist(nlist)
                explodepos = f_find_explode_pair(slist)
                splitpos, splitnum = f_find_split(slist, nlist)
            pairlist = f_find_pairs(slist)
            while len(pairlist) > 0:
                for p in range(len(pairlist)-1, -1, -1):
                    nlist = f_replace_pair(nlist, pairlist[p])
                slist = f_make_slist(nlist)
                pairlist = f_find_pairs(slist)
            currmag = nlist[0]
            print(r,s,currmag)
            if currmag > maxmag:
                maxmag = currmag
print("Max = ", maxmag)









