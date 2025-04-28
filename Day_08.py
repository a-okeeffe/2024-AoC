## STATS
# P1 Time:  
# P1 Rank:  
# P2 Time:  
# P2 Rank:  

# given inputs are in input_day02.txt
with open(r'inputs\inpt_day08.txt') as file:
    lines = file.readlines()

# from the input we make a 2D array of characters in the corresponding positions
inpt_grid = []
for line in lines:
    line = list(line)
    line.remove('\n')
    inpt_grid.append(line)

# list of unique frequencies found in the grid
frequencies = []
# collecting the unique frequencies
for row in inpt_grid:
    for digit in row:
        if (not (digit in frequencies)):
            frequencies.append(digit)
# '.' is not a frequency
frequencies.remove('.')

# collection of all antinode positions
antinodes = []
# we'll collect the antinodes for each frequency
for f in frequencies:
    pos = []
    for i in range(0, len(inpt_grid)):
        for j in range(0, len(inpt_grid[0])):
            if (f ==  inpt_grid[i][j]):
                # positions will be (x, y) with y counting *down from the top*
                pos.append((j, i))    
    print(pos)
