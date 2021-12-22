"""
Advent of code 2021
"""
rawdata = [line.strip() for line in open('Advofcode input.txt')] # read file
# get list of numbers drawn
numlist = rawdata[0] # take first line (which has ball numbers)
numstr = numlist[0] # get first digit
balls = [] # holder for list of ball numbers
for i in range(1,len(numlist)): # loop to find numbers and lose commas
    if numlist[i] == ",":
        balls.append(eval(numstr))
        numstr = ""
    else:
        numstr = numstr + numlist[i]
balls.append(eval(numstr)) # put in final number

# get list of numbers on boards, as a single list
boards = [] # holder for list of board numbers
for i in range(1,len(rawdata)): # loop to read data rows
    thisrow = rawdata[i]
    if len(thisrow)>0: # i.e. ignore blank rows
        numstr = "" # reset holder to "empty"
        for j in range(0,len(thisrow)): # loop to read each character
            if thisrow[j] == " ": # If it's a space
                if numstr != "": # Number stored
                    boards.append(eval(numstr)) # Save number
                    numstr = ""
            else:
                numstr = numstr + thisrow[j]
        boards.append(eval(numstr)) # Save final number in row
# -----------------------------------
boardcount = int((len(boards)/25)) # count number of boards
boardsdone=[]
lastboard=[]
for i in range(boardcount): # create list of "N"s
    boardsdone.append("N")
# read in balls and cross off numbers - i.e. add 900 so can see original value
ballindex = -1 # set to minus one so first item in loop to add one works
while "N" in boardsdone: # keep going while any board not completed
    ballindex = ballindex + 1
    ball = balls[ballindex]
# change any of current ball to number + 900 (so 0 => 900 and > 100 check)
    for i in range(len(boards)):
        if boards[i] == ball:
            boards[i] = boards[i]+ 900
# test each board in turn
    for b in range(boardcount):
        if boardsdone[b] == "N": # only check boards not already completed
            s = b * 25 # set start of board
            for r in range(s, s+25, 5): # check for rows completed
                if boards[r] > 100 \
                    and boards [r+1] > 100 \
                    and boards [r+2] > 100 \
                    and boards [r+3] > 100 \
                    and boards [r+4] > 100:
                    boardsdone [b] = "R"
                    lastboard.append(b)
            for c in range(s, s+5): # check for cols completed
                if boards[c] > 100 \
                    and boards[c+5] > 100 \
                    and boards[c+10] > 100 \
                    and boards[c+15] > 100 \
                    and boards[c+20] > 100:
                    boardsdone [b] = "C"
                    lastboard.append(b)
# Add up remaining numbers for last board complete
finalboard = lastboard[len(lastboard)-1]
finaltot = 0
s = finalboard * 25 # set start of board
for x in range(s, s+25):
    if boards[x] < 100: # ignore crossed of numbers
        finaltot = finaltot + boards[x]
print ("finaltot", finaltot, "ball", ball, "answer", ball * finaltot)
