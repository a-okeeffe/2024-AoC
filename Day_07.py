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


for equation in equations:
    total = equation[0]
    units = equation[1:]
    print(units)
    operation = ["{0:04b}".format(x) for x in range(2 ** (len(units) - 1))]
    print(operation)

    #for ops in range(len(operation)):

