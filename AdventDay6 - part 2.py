"""
Advent of code 2021
"""
# saving live input file created weird characters so revert to cut and paste!
#fish = [4,5,3,2,3,3,2,4,2,1,2,4,5,2,2,2,4,1,1,1,5,1,1,2,5,2,1,1,4,4,5,5,1,2,1,1,5,3,5,2,4,3,2,4,5,3,2,1,4,1,3,1,2,4,1,1,4,1,4,2,5,1,4,3,5,2,4,5,4,2,2,5,1,1,2,4,1,4,4,1,1,3,1,2,3,2,5,5,1,1,5,2,4,2,2,4,1,1,1,4,2,2,3,1,2,4,5,4,5,4,2,3,1,4,1,3,1,2,3,3,2,4,3,3,3,1,4,2,3,4,2,1,5,4,2,4,4,3,2,1,5,3,1,4,1,1,5,4,2,4,2,2,4,4,4,1,4,2,4,1,1,3,5,1,5,5,1,3,2,2,3,5,3,1,1,4,4,1,3,3,3,5,1,1,2,5,5,5,2,4,1,5,1,2,1,1,1,4,3,1,5,2,3,1,3,1,4,1,3,5,4,5,1,3,4,2,1,5,1,3,4,5,5,2,1,2,1,1,1,4,3,1,4,2,3,1,3,5,1,4,5,3,1,3,3,2,2,1,5,5,4,3,2,1,5,1,3,1,3,5,1,1,2,1,1,1,5,2,1,1,3,2,1,5,5,5,1,1,5,1,4,1,5,4,2,4,5,2,4,3,2,5,4,1,1,2,4,3,2,1]
fish = [3,4,3,1,2]
day = 1
days = 18
dcount = nextdcount = [0,0,0,0,0,0,0,0,0]
for i in range(len(dcount)):
    dcount[i] = fish.count(i) # set up counts of fish by internal timer
for d in range(days):
    for f in range(len(dcount)):
        if f==0: # 0 generates a new fish and becomes 6
            nextdcount[8]=dcount[0]
            nextdcount[6]=dcount[0]
        elif f==7: # 6 already populated so add not replace
            nextdcount[f-1] = nextdcount[f-1] + dcount[f]
        else:
            nextdcount[f-1] = dcount[f]
    dcount = nextdcount[:]
    nextdcount = [0,0,0,0,0,0,0,0,0]
totalfish = sum(dcount)
print ("Total fish after",days,"days is", totalfish)
