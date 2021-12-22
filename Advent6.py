"""
Advent of code 2021
"""

n = [line.strip() for line in open('Advofcode input.txt')] # read file
nstored = n
newn = []
oxgend = 0
digcount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Live version
for pos in range(len(digcount)): # loop through positions
    for i in range(len(n)): # loop through data
        cstring = n[i] # store string
        digcount [pos] = digcount[pos] + eval(cstring [pos])
        if digcount [pos] == (len(n)/2): # same number so use 1
            keep = '1'
        elif digcount [pos] > (len(n)/2):
            keep = '1'
        else:
            keep = '0'
    for i in range(len(n)): # loop through data again to extract right lines
        cstring = n[i] # store string
        if cstring [pos] == keep:
                newn.append(cstring)
    n = newn[:] # store selected numbers in n
    newn = [] # reset new list
oxgend = int(cstring, 2) # Translate binary to decimal
print ("oxgend" ,oxgend) # DEBUG**
# Repeat process for CO2 scrubber rating, least common value,
# if equal use values with a 0.
n = nstored[:] # Reset to original list
newn = []
co2d = 0
digcount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Live version
for pos in range(len(digcount)): # loop through positions
    for i in range(len(n)): # loop through data
        cstring = n[i] # store string
        digcount [pos] = digcount[pos] + eval(cstring [pos])
        if digcount [pos] == (len(n)/2): # same number so use 0
            keep = '0'
        elif digcount [pos] > (len(n)/2):
            keep = '0'
        else:
            keep = '1'
    print ("keep", keep) # DEBUG ******
    for i in range(len(n)): # loop through data again to extract right lines
        cstring = n[i] # store string
        if cstring [pos] == keep:
                newn.append(cstring)
    n = newn[:] # store selected numbers in n
    newn = [] # reset new list
co2d = int(cstring, 2) # Translate binary to decimal

print ("Oxygen renewal rating ", oxgend)
print ("CO2 scrubber ", co2d)
print ("Answer for puzzle is: ", oxgend * co2d)

