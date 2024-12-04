## STATS
# P1 Time:  20:43:39
# P1 Rank:  110939
# P2 Time:  20:52:17
# P2 Rank:  85238

# given inputs are in input_day02.txt
with open(r'inputs/inpt_day02.txt') as file:
    lines = file.readlines()

safe_list = [] # True is safe
damp_list = [] # True is safe, tolerates 1 mistake
for line in lines:
    # report <- a list of ints for each line
    report = list(map(int, line.split()))

    prev = report[0]
    direction = 0
    safe = True
    damp_safe = True
    damped = 0

    # normalizing the positivity of the increment before the loop
    if report[0] < report[1]:
        direction = 1
    else:
        direction= -1

    for i in range(1, len(report)):
        # check the adjusted difference and make sure it's \in [1,3]
        inc = (report[i] - report [i - 1]) * direction
        if (inc < 1) or (inc > 3):
            safe = False
            # have to go through an extra step with the dampener
            if damped == 1:
                damp_safe = False
                break
            else:
                damped = 1
    safe_list.append(safe)
    damp_list.append(damp_safe)

safe_sum = sum(safe_list)
damp_sum = sum(damp_list)
print('there are', safe_sum, 'safe reports')
print('there are', damp_sum, 'safe reports with the Problem Dampener')