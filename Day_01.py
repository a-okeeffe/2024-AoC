# get input from user, lits separated by whtiespace
list1 = input("left list:").split()
list1 = list(map(int, list1))
list2 = input("right list:").split()
list2 = list(map(int, list2))

def merge_sort(list):
    n = len(list)
    if n == 1:
        return list
    left = merge_sort(list[0:round(n/2)])
    right = merge_sort(list[round(n/2):n])
    left.append(left[-1] + right[-1])
    right.append(left[-1] + right[-1])
    leftn = 0
    rightn = 0

    for i in range(n):
        if left[leftn] < right[rightn]:
            list[i] = left[leftn]
            leftn += 1
        else:
            list[i] = right[rightn]
            rightn += 1

    return list

list1 = merge_sort(list1)
list2 = merge_sort(list2)
sum = 0

for i in range(len(list1)):
    sum = sum + abs(list1[i] - list2[i])

print(sum)
    