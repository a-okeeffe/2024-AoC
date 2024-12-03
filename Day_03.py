import re
with open('inputs\inpt_day03.txt') as file:
    lines = file.readlines()

mult = 0
for line in lines:
    x = re.findall("mul\(\d+,\d+\)", line)

    for item in x:
        y = re.findall("\d+", item)
        mult += (int(y[0]) * int(y[1]))

# part 2
mult2 = 0
do = True
for line in lines:
    x = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", line)

    for item in x:
        if item == "do()":
            do = True
        elif item == "don't()":
            do = False
        elif do:
            y = re.findall("\d+", item)
            mult2 += (int(y[0]) * int(y[1]))
    print(mult2)


print(mult)
print(mult2)