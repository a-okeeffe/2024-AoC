# given inputs are in input_day01.txt
import sys

with open('inputs/inpt_day01.txt') as file:
    lines = file.readlines()

# separate the text file into two lists
list1 = []
list2 = []
for line in lines:
    temp = list(map(int, line.split()))
    list1.append(temp[0])
    list2.append(temp[1])

# cmd inputs for debug
# list1 = input("left list:").split()
# list1 = list(map(int, list1))
# list2 = input("right list:").split()
# list2 = list(map(int, list2))

# merge sort function: list -> sorted list
def merge_sort(list):
    n = len(list)
    if n <= 1:
        return list
    
    # recursive call on each half of the list
    left = merge_sort(list[0:round(n/2)])
    right = merge_sort(list[round(n/2):n])
    # I append a larger value on the end of each list to avoid overflow err
    left.append(left[-1] + right[-1])
    right.append(left[-1] + right[-1])
    # iteration indices for each list
    leftn = 0
    rightn = 0

    # for each idx in list, get the next lowest number
    for i in range(n):
        if left[leftn] < right[rightn]:
            list[i] = left[leftn]
            leftn += 1
        else:
            list[i] = right[rightn]
            rightn += 1

    return list

# sort the two given lists
list1 = merge_sort(list1)
list2 = merge_sort(list2)
sum = 0

# iterate through both lists and grab the sum of the distance
for i in range(len(list1)):
    sum = sum + abs(list1[i] - list2[i])

print(sum)
    