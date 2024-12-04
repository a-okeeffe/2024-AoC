## STATS
# P1 Time:  00:10:32
# P1 Rank:  4457
# P2 Time:  01:50:43
# P2 Rank:  15993

# given inputs are in input_day03.txt
import re
with open(r'inputs\inpt_day03.txt') as file:
    lines = file.readlines()

# mult <- the total from the correct mults
mult = 0
for line in lines:
    # regex to find all instances of "mult(***,***)"
    x = re.findall(r"mul\(\d+,\d+\)", line)

    for item in x:
        # second regex to specifically grab the ints to multiply
        y = re.findall(r"\d+", item)
        mult += (int(y[0]) * int(y[1]))

# part 2
# mult2 <- total from counted mults for part 2
# do <- boolean to filter out 'disabled' mults
mult2 = 0
do = True
for line in lines:
    # same regex as part 1 but with the addition of 'do()' and 'don't()'
    x = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)

    # each "do()" sets the filter bool to true, "don't()" sets it to false
    for item in x:
        if item == "do()":
            do = True
        elif item == "don't()":
            do = False
        elif do:
            y = re.findall(r"\d+", item)
            mult2 += (int(y[0]) * int(y[1]))

print("mult() summation: \t\t", mult)
print("filtered mult() summation: \t", mult2)