## STATS
# P1 Time:  
# P1 Rank:  
# P2 Time:  
# P2 Rank:  

# given inputs are in input_day02.txt
with open(r'inputs\inpt_day05.txt') as file:
    lines = file.readlines()

rules = []
updates = []
for line in lines:
    if ("|" in line):
        rules.append(list(map(int, line.split("|"))))

    elif ("," in line):
        updates.append(list(map(int, line.split(","))))


def update_list(list, x, y, xval, yval):
    if x >= y:
        list.pop(x)
        list.insert(y, xval)
    return list

reordered_pages = []
def passes_rules(update):
    bool = True
    newlist = update.copy()

    for rule in rules:
        if ((rule[0] in update) and (rule[1] in update)):
            # find the indices for each rule
            x = update.index(rule[0])
            y = update.index(rule[1])
            if (x >= y):
                #print("x", rule[0], "x:", x, "y", rule[1], "y:", y)
                newlist = update_list(newlist, newlist.index(rule[0]), newlist.index(rule[1]), rule[0], rule[1])
                #print(update)
                #print(rule)
                #print(newlist)
                #print("--------------")
                bool = False
    if (not bool):
        reordered_pages.append(newlist)
        print(newlist)
        print(reordered_pages)
        print(len(reordered_pages))
    return bool

i = 0
update_mids = 0
for update in updates:
    # pass update to the aux method to check if it passes
    if passes_rules(update):
        # if the update passes, add the midpoint to our counter
        update_mids += update[int((len(update) - 1) / 2)]
        i += 1

print(update_mids)


for page in reordered_pages:
    ordered = False
    while (not ordered):
        ordered = True
        for rule in rules:
            if ((rule[0] in page) and (rule[1] in page)):
            # find the indices for each rule
                x = page.index(rule[0])
                y = page.index(rule[1])
                if (x >= y):
                    ordered = False
                    page.pop(x)
                    page.insert(y, rule[0])


nonupdate_mids = 0
for item in reordered_pages:
    nonupdate_mids += item[int((len(item) - 1) / 2)]

print(nonupdate_mids)

## error handling notes:
# we do have the right number of lists in reordered_pages,
# so more likely than not it's the ordering of the list
# that's failing