with open('inputs/inpt_day02.txt') as file:
    lines = file.readlines()

safe_list = [] # True is safe
for line in lines:
    # report <- a list of ints for each line
    report = list(map(int, line.split()))

    prev = report[0]
    direction = 0
    safe = True

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
            break
    safe_list.append(safe)

sum = sum(safe_list)
print('there are', sum, 'safe reports')