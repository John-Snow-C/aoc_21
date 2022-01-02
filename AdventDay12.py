"""
Advent of code 2021 day 12
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

def f_tidy_data(f_list):
    f_starts = []
    f_links = []
    for i in range(len(f_list)):
        f_row = f_list[i].split("-")
        if f_row[0] == "start":
            f_starts.append(f_row)
        elif f_row[1] == "start":
            f_row.reverse()
            f_starts.append(f_row)
        elif f_row[0] == "end":
            f_links.append(f_row)
        elif f_row[1] == "end":
            f_row.reverse()
            f_links.append(f_row)
        else:
            f_links.append(f_row)
    return f_starts, f_links

def f_find_links(f_cave, f_links):
    f_joins = []
    for i in range(len(f_links)):
        if f_cave == f_links[i][0]:
            f_joins.append(f_links[i][1])
        else:
            if f_cave == f_links[i][1]:
                f_joins.append(f_links[i][0])
    return f_joins 

def f_extend_path(f_curr_path, f_link, f_smalls):
    f_new_path = []
    f_add = "Y"
    if f_link != f_link.upper(): # small cave
        f_count = f_curr_path.count(f_link)
        if f_count > 1: # already added twice
            f_add = "N"
        elif f_count == 1: # one in so check none yet doubled up
            for i in range(len(f_smalls)):
                f_count = f_curr_path.count(f_smalls[i])
                if f_count > 1:
                    f_add = "N"
# implied "else" is none in yet so add        
    if f_add == "Y":
        f_new_path = list(f_curr_path)
        f_new_path.append(f_link)
    return f_new_path 

def f_all_paths_complete(f_newpaths):
    if len(f_newpaths) > 0:
        f_finished = "N"
    else:
        f_finished = "Y"
    return f_finished

def f_find_small(f_linklist):
    f_small_list = []
    for i in range(len(f_linklist)):
        if f_linklist[i][0] != "end":
            if f_linklist[i][0] != f_linklist[i][0].upper():
                f_small_list.append(f_linklist[i][0])
        if f_linklist[i][1] != "end":
            if f_linklist[i][1] != f_linklist[i][1].upper():
                f_small_list.append(f_linklist[i][1])
    return f_small_list

# -------------- set global values and read data from input file
runtype = "L" # L for live E for example
rundata = "S" # S for strings, I for integers
lastrow, lastcol, data = f_read_file (runtype, rundata)

# -------------- other variables
paths = []
newpaths = []
completepaths = []

# -------------- process

paths, linklist = f_tidy_data(data)
links = tuple(linklist)

small_list = f_find_small(linklist)
small_set = set(small_list)
small_list2 = list(small_set)
small_list2.sort()
small_tup = tuple(small_list2[:])
pprint(small_list)
input()

finished = "N"
while finished == "N":
    print("paths in play", len(paths))
    for i in range(len(paths)):
        curr_path = tuple(paths[i])
        curr_cave = curr_path[-1]
        link_list = f_find_links(curr_cave, links)
        for j in range(len(link_list)):
            new_path = f_extend_path(curr_path, link_list[j], small_tup)
            if len(new_path) > 0: # link added
                if new_path[-1] == "end":
                    completepaths.append(new_path)
                else:
                    newpaths.append(new_path)
    finished = f_all_paths_complete(newpaths)
    if finished == "N":
        paths = newpaths[:]
        newpaths = []

print("puzzle answer = ", len(completepaths))

