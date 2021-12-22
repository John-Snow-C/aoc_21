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
# read in balls and cross off numbers - i.e. replace with 999
# set "house" to N, then replace wiht R or C
# depending on whether row of col found
house = "N"
ballindex = 0
board = 0
while house == "N":
    ball = balls[ballindex]
    for i in range(len(boards)):
        if boards[i] == ball:
            boards[i] = 999
# test if any row complete
    for j in range(0, len(boards)-4, 5):
        if boards[j] == 999 \
        and boards[j+1] == 999 \
        and boards[j+2] == 999 \
        and boards[j+3] == 999 \
        and boards [j+4] == 999:
            house = "R"
            board = int(j/25)
# test if any column complete
    for k in range(0, len(boards)-24, 25):
        for l in range(5):
            if boards[l+k] == 999 \
            and boards[l+k+5] == 999 \
            and boards[l+k+10] == 999 \
            and boards[l+k+15] == 999 \
            and boards[l+k+20] == 999:
                house = "C"
                board = int(k/25)
#    print ("ballindex", ballindex, "ball", ball) DEBUG
    if house == "N":
        ballindex = ballindex + 1
    if ballindex >= len(balls):
        print ("Past the end of the list, and no house called")
        house = "ERROR, press ctrl C and check the code!"
# add up numbers no crossed off on board with "house"
startpos = board * 25
totunmarked = 0
for i in range(startpos, startpos+25):
    if (boards[i] != 999): #ignore crossed of numbers
        totunmarked = totunmarked + boards[i]
print ("tot = ", totunmarked, "last num = ", ball)
print ("Result = ", totunmarked * ball)
"""

# print ("house = ", house, "Board = ", board, "ball", ball) DEBUG

# Print rows for testing
for i in range(0, len(boards),25): #DEBUG
    print ("---") #DEBUG
    print (boards[i], boards[i+1], boards[i+2], boards[i+3], boards[i+4]) #DEBUG
    print (boards[i+5], boards[i+6], boards[i+7], boards[i+8], boards[i+9]) #DEBUG
    print (boards[i+10], boards[i+11], boards[i+12], boards[i+13], boards[i+14]) #DEBUG
    print (boards[i+15], boards[i+16], boards[i+17], boards[i+18], boards[i+19]) #DEBUG
    print (boards[i+20], boards[i+21], boards[i+22], boards[i+23], boards[i+24]) #DEBUG
"""
