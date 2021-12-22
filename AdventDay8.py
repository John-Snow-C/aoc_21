"""
Advent of code 2021
"""
from pprint import pprint # useful for debugging

def findchar(s1, s2): # find character in S1 but not in S2
    if len(s2)>len(s1): # need longest string in S1
        tempstring = s2
        s2 = s1
        s1 = tempstring
    loop = len(s1)
    s3=""
    for x in range(loop):
        if not s1[x] in s2:
            s3= s1[x]
    return(s3)

def remchar(s, y): # Remove character passed for every item in current decode
    for y in range(10):
        snew = decode_number[y][1].replace(s,"")
        decode_number[y][1] = snew

# -------------- read data from input file
data = [line.strip() for line in open('Advofcode input.txt')] # read file

# -------------- split data into signal and output
drow=[]
for i in range(len(data)):
    drow.append(data[i].split(" | ")) #NB " | " and space to avoid extra spaces

# -------------- split signals into an array, sorting each alphabetically
signals=[]
for i in range(len(drow)):
    signals.append(drow[i][0].split(" "))

# -------------- sort each signal into alphabetical order
for i in range(len(signals)):
    for j in range(10):
        signals[i][j] = ''.join(sorted(signals[i][j]))

# -------------- split outputs into an array
outputs=[]
for i in range(len(drow)):
    outputs.append(drow[i][1].split(" "))

# -------------- sort each output into alphabetical order
for i in range(len(outputs)):
    for j in range(4):
        outputs[i][j] = ''.join(sorted(outputs[i][j]))

# -------------- decode each row in turn
# put signals into list for decoding
grandtot = 0
for i in range(len(signals)):
#    print("i", i, "pprint drow") #DEBUG
#    pprint(drow) #DEBUG
    found5 = found6 = 0 # 3 each of length 5 and 6 so increment position
    decode_number = [[0, "", ""] for i in range(10)] # list to decode numbers
#NB populate list in order by length of code, 2, 3, etc up to 7
    for j in range(10):
        tempcode = signals[i][j]
        lencode = len(tempcode)
        if lencode == 2:
            decode_number[0][1] = decode_number[0][2] = tempcode
            decode_number[0][0] = 1
        elif lencode == 3:
            decode_number[1][1] = decode_number[1][2] = tempcode
            decode_number[1][0] = 7
        elif lencode == 4:
            decode_number[2][1] = decode_number[2][2] = tempcode
            decode_number[2][0] = 4
        elif lencode == 5:
            decode_number[3+found5][1] = decode_number[3+found5][2] = tempcode
            found5 +=1
        elif lencode == 6:
            decode_number[6+found6][1] = decode_number[6+found6][2] = tempcode
            found6 +=1
        else:
            decode_number[9][1] = decode_number[9][2] = tempcode
            decode_number[9][0] = 8
#    print ("Original decode") #DEBUG
#    pprint(decode_number) #DEBUG
# find what code represents what number
    s1 = decode_number[1][1] # letter in 7 but not in 1
    s2 = decode_number[0][1]
    rems = findchar(s1,s2)
    remchar(rems, i) # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#    print ("Decode after removing", rems) #DEBUG
#    pprint(decode_number) # DEBUG
#    input()
    twonum = decode_number[1][1] # one of letters is in all but number 2
    twotst = twonum[0]
    found = 0
    for k in range(10): # check if first letter in all
        if twotst in decode_number[k][1]:
            found +=1
    if not found == 9: # not found in all signals but 1, then other letter
        twotst = twonum[1]
    for m in range(3,6): # check which of 3 options is 2
        if twotst not in decode_number[m][1]:
            decode_number[m][0] = 2
    remchar(twotst, i)  # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#    print ("Decode after finding 2", twotst, "and removing") #DEBUG
#    pprint(decode_number) # DEBUG
    threetst = decode_number[0][1] # remaining letter in 1 is just in number 3
    for n in range(3,6): # check 3 options except the one flagged as number 2
        if decode_number[n][0] != 2:
            if threetst in decode_number[n][1]:
                decode_number[n][0] = 3
            else:
                decode_number[n][0] = 5 # last of 5 long codes
    remchar(threetst, i)  # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#    print ("Decode after finding 3", threetst, "and removing") #DEBUG
#    pprint(decode_number) # DEBUG
    for o in range(6,9): # of 6 lengths one has four char left number 6 
        if len(decode_number[o][1]) == 4:
            decode_number[o][0] = 6
#    print ("Decode after finding 6") #DEBUG
#    pprint(decode_number) # DEBUG
    ninenum = decode_number[2][1] # one of letters left in 4 is in 9
    ninetst = ninenum[0]
    found = 0
    for p in range(6,9): # check if first letter in any length 6
        if ninetst in decode_number[p][1]:
            found +=1
    if found > 2: # wrong letter!
        ninetst = ninenum[1]
#    print("ninetst", ninetst) #DEBUG
    for p in range(6,9): # rerun loop now know which is the right letter
        if ninetst in decode_number[p][1]:
            if decode_number[p][0] != 6: # provided not already set to 6
                decode_number[p][0] = 9 # note that final number 0 already set
#    print ("Decode after finding 9") #DEBUG
#    pprint(decode_number) # DEBUG
    decode_number.sort()
#    print ("Sorted by digit")
#    pprint(decode_number) # DEBUG
    decode=[] # create array with just codes
    for q in range(len(decode_number)):
        decode.append(decode_number[q][2])
#    print ("Decode for data row", i) #DEBUG
#    pprint(decode) # DEBUG
# decode output values
#    print ("Outputs") #DEBUG
#    pprint(outputs) # DEBUG
    rowval = ""
    for r in range(4): # Always four outputs per row
        sig = outputs[i][r]
        sigval = decode.index(sig)
        rowval = rowval + str(sigval)
#        print("Sigval", sigval, rowval) #DEBUG
#        input() #DEBUG
    print("xxx", rowval[0])
    if rowval[0] == "0":
        print (rowval)
        rowval = rowval [1]+rowval[2]+rowval[3]
        print(rowval)
    rowtot = eval(rowval)
    grandtot = grandtot + rowtot
#    print ("data row (i)", i, "signals", \
#           outputs[i][0], outputs[i][1], outputs[i][2], \
#           outputs[i][3], "rowtot", rowtot)
#    input() #DEBUG
print ("Grand total", grandtot)
