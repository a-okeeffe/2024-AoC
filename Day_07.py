## STATS
# P1 Time:  
# P1 Rank:  
# P2 Time:  
# P2 Rank:  

# given inputs are in input_day02.txt
with open(r'inputs\inpt_day07.txt') as file:
    lines = file.readlines()

equations = []
for line in lines:
    line = list(line.split())
    line[0] = line[0][:-1]
    equations.append(list(map(int, line)))

def calc(vals, ops):
    for i in range(len(vals) - 1):
        if (ops[i] == 0):
            vals[i + 1] = vals[i] + vals[i + 1]
        if (ops[i] == 1):
            vals[i + 1] = vals[i] + vals[i + 1]
    return vals[-1]
#for equation in equations:
#    target = equation[0]
#    units = equation[1:]
#    ops = [0] * (len(units) - 1)
#    nosol = True
#    while nosol:
#        for i in range(len(ops)):
#
#            if calc(units, ops) == target:
#                nosol == False



