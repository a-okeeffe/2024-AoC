## STATS
# P1 Time:  
# P1 Rank:  
# P2 Time:  
# P2 Rank:  

# given inputs are in input_day02.txt
with open(r'inputs\inpt_day06.txt') as file:
    lines = file.readlines()

floorplan = []
for line in lines:
    floorplan.append(list(line)[:-1])

pos = []
orient = ''
for i in range(len(floorplan)):
    if ('v' in floorplan[i]):
        pos.append(i)
        pos_change = [1, 0]
        orient = 'v'
    elif ('>' in floorplan[i]):
        pos.append(i)
        pos_change = [0, 1]
        orient = '>'
    elif ('<' in floorplan[i]):
        pos.append(i)
        pos_change = [0, -1]
        orient = '<'
    elif ('^' in floorplan[i]):
        pos.append(i)
        pos_change = [-1, 0]
        orient = '^'

pos.append(floorplan[pos[0]].index(orient))
floorplan[pos[0]][pos[1]] = 'X'


# Below function is for PART 2
def to_right(pos, pos_change):

    pc = [(pos_change[1]), (-1 * pos_change[0])]
    loop = False
    if(pc[0] == 0):
        i = pos[1]
        while (i > 0) and (i < len(floorplan[0])):
            if (floorplan[pos[0]][i] == '#'):
                loop = to_right([pos[0], i], pc)
                break
            i += pc[1]    
        
    elif (pc[1] == 0):
        i = pos[0]
        while (i > 0) and (i < len(floorplan)):
            if (floorplan[i][pos[1]] == '#'):
                loop = to_right([i, pos[1]], pc)
                break
            i += pc[0]    

    return loop



in_map = True
steps = 1
obstruction_pos = []
obs = 0
while in_map:

    i = pos[0] + pos_change[0]
    j = pos[1] + pos_change[1]
    if (i < 0) or (i >= len(floorplan)) or (j >= len(floorplan[0])) or (j < 0):
        in_map = False
        break
    else:

        if (floorplan[i][j] == '#'):
            #obstruction_pos.append([i, j])
            pos_change = [(pos_change[1]), (-1 * pos_change[0])]  
        elif (floorplan[i][j] == 'X'):
            pos = [i, j]
        else:
            pos = [i, j]
            floorplan[i][j] = 'X'
            steps += 1
            #if(to_right(pos, pos_change)):
            #    obs += 1
print(steps)

# Part 1 correct answer is 4454

# for i in range(2, len(obstruction_pos)):
#     i0 = obstruction_pos[i][0]
#     j0 = obstruction_pos[i][1]
#     i_1 = obstruction_pos[i - 1][0]
#     j_1 = obstruction_pos[i - 1][1]
#     i_2 = obstruction_pos[i - 2][0]
#     j_2 = obstruction_pos[i - 2][1]

#     if ((i0 - 1) == i_1) and ((j_1 - 1) == j_2):
#         obs += 1
#     elif ((j0 - 1) == j_1) and ((i_1 + 1) == i_2):
#         obs += 1
#     elif ((i0 + 1) == i_1) and ((j_1 + 1) == j_2):
#         obs += 1   
#     elif ((j0 + 1) == j_1) and ((i_1 - 1) == i_2):
#         obs += 1
print(obs)


            



