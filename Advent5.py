"""
Advent of code 2021
"""
# Read file
n = [line.strip() for line in open('Advofcode input.txt')]
digcount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cstring = ""
gammas = ""
epsilons = ""
gammad = 0
epsilond = 0
# loop through adding up ones and zeros
for i in range(len(n)):
    cstring = n[i]
    for j in range(12):
        digcount [j] = digcount[j] + eval(cstring [j])
for k in range(12):
    if digcount [k] > (len(n)/2):
        gammas = gammas + '1'
        epsilons = epsilons + '0'
    else:
        gammas = gammas + '0'
        epsilons = epsilons + '1'
gammad = int(gammas, 2)
epsilond = int(epsilons, 2)
print ("Gamma and Epsilon are: ", gammad, epsilond)
print ("Answer for puzzle is: ", gammad * epsilond)

