"""
Advent of code 2021 day 14
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

def f_get_all_letters(f_poly, f_rules):
    f_templet = []
    for i in range(len(f_poly)):
        f_templet.append(f_poly[i])
    for i in range(len(f_rules)):
        f_temp_pair = f_rules[i][0]
        f_templet.append(f_temp_pair[0])
        f_templet.append(f_temp_pair[1])
        f_templet.append(f_rules[i][1])
    f_letterset = set(f_templet)
    f_all_letters = []
    for x in f_letterset:
        f_all_letters.append(x)
    f_all_letters.sort()
    return f_all_letters

def f_get_all_pairs(f_all_letters):
    f_pairlist = []
    f_all_pairs = []
    for i in range(len(f_all_letters)):
        for j in range(len(f_all_letters)):
            f_pair = f_all_letters[i]+f_all_letters[j]
            f_pairlist.append(f_pair)
    f_pairlist.sort()
    for i in range(len(f_pairlist)):
        f_row = [f_pairlist[i], 0,0]
        f_all_pairs.append(f_row)
    return f_pairlist, f_all_pairs

def f_start_pairs(f_pairlist, f_allpairs,f_polystart):
    for i in range(len(f_polystart)-1):
       f_pair = f_polystart[i]+f_polystart[i+1]
       f_row = f_pairlist.index(f_pair)
       f_allpairs[f_row][1] = f_allpairs[f_row][1]+ 1
       f_allpairs[f_row][2] = f_allpairs[f_row][2]+ 1
    return f_allpairs

def f_insert(f_pairlist, f_all_pairs, f_rules, f_counts):
    for i in range(len(f_rules)):
        f_pair = f_rules[i][0]
        f_insert = f_rules[i][1]
        f_newpair1 = f_pair[0]+f_insert
        f_newpair2 = f_insert+f_pair[1]
        f_row = f_pairlist.index(f_pair)
        if f_all_pairs[f_row][1] > 0: # is one to do insert on
#            if f_all_pairs[f_row][2] > 0:
            f_add = f_all_pairs[f_row][1] # number to insert
            f_all_pairs[f_row][2] = f_all_pairs[f_row][2] - f_add # lose pairs
            f_row = f_pairlist.index(f_newpair1) # add first pairs
            f_all_pairs[f_row][2] = f_all_pairs[f_row][2] + f_add
            f_row = f_pairlist.index(f_newpair2) # add second pairs
            f_all_pairs[f_row][2] = f_all_pairs[f_row][2] + f_add
            f_cpos = all_letters.index(f_insert)
            f_counts[f_cpos] = f_counts[f_cpos] + f_add
    return f_all_pairs, f_counts

def f_tidy_up(f_polyinsert):
    f_polytidy = []
    for i in range(len(f_polyinsert)):
        if len(f_polyinsert[i]) == 1:
            f_polytidy.append(f_polyinsert[i])
    return f_polytidy

def f_print(f_poly):
    f_line = ""
    for i in range(len(f_poly)):
        f_line = f_line + f_poly[i]
    print(f_line)
    return ()

def f_create_polygap(f_poly):
    f_polygap = []
    for i in range(len(f_poly)-1):
        f_polygap.append(f_poly[i])
        f_polygap.append(" ")
    f_polygap.append(f_poly[i+1])
    return f_polygap

def f_fill_in_pairs(f_polygap):
    for i in range(1,len(f_polygap),2):
        f_polygap[i] = f_polygap[i-1]+polygap[i+1]
    return f_polygap

# -------------- set global values and read data from input file
runtype = "L" # L for live E for example
rundata = "S" # S for strings, I for integers
lastrow, lastcol, data = f_read_file (runtype, rundata)

polystart = data[0]
rules = []
for i in range(2, len(data)):
    row = data[i]
    pair = row[0:2]
    insertchar = row[6]
    rule = [pair, insertchar]
    rules.append(rule)
all_letters = f_get_all_letters(polystart, rules)
pairlist, all_pairs = f_get_all_pairs(all_letters)
all_pairs = f_start_pairs(pairlist, all_pairs, polystart)

counts = [0 for i in range(len(all_letters))] 
for i in range(len(polystart)):
    letter = polystart[i]
    cpos = all_letters.index(letter)
    counts[cpos] = counts[cpos] +1

# -------------- process
steps = 40
for i in range(steps):
    all_pairs, counts = f_insert(pairlist, all_pairs, rules, counts)
    for j in range(len(all_pairs)): # move 2 to 1 for next step
        all_pairs[j][1] = all_pairs[j][2]
    print("step", i+1) #DEBUG
    rlen = 0 #DEBUG
    for i in range(len(counts)):
        rlen = rlen + counts[i]
    print("length", rlen)
lmax = max(counts)
lmin = min(counts)
print("puzzle answer", lmax-lmin)
