## STATS
# P1 Time:  00:36:15
# P1 Rank:  7275
# P2 Time:  00:44:29
# P2 Rank:  5606

# given inputs are in input_day02.txt
with open(r'inputs\inpt_day04.txt') as file:
    lines = file.readlines()

# wordsearch <- the input file as a 2D character array
wordsearch = []
for line in  lines:
    wordsearch.append(list(line))

# word <- stores "XMAS" characters to aid with recursion
word = ['X', 'M', 'A', 'S']
def aux_letter(i, j, inc, l):
    # check first to make sure indices are in bounds and letter isn't incorrect
    if (i < 0) or (j < 0) or (i >= len(wordsearch)) or (j >= len(wordsearch)) or (wordsearch[i][j] != word[l]):
        return False
    # last letter is the base case, returns true
    if (l == 3) and (wordsearch[i][j] == word[l]):
        return True
    # increment recursive call with given direction (see correct_letter) and next letter in "XMAS"
    return aux_letter(i + inc[0], j + inc[1], inc, l + 1)
    
# circle <- an array with every possible direction from the current index in a 2D array
circle = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
def correct_letter(i, j):
    # words <- counter to check how many directions make a full "XMAS"
    words = 0
    for dot in circle:
        # call the aux method for every direction in the circle from the given index (i, j) and looking for "M"
        if aux_letter(i + dot[0], j + dot[1], dot, 1):
            words += 1
    return words

# xmas_count <- "XMAS" instance counter
xmas_count = 0
# iterate through every letter in the word search
for i in range(len(wordsearch)):
    for j in range(len(wordsearch[0]) - 1):
        # whenever we find an "X", check to see if we can find a full "XMAS"
        if wordsearch[i][j] == "X":
            xmas_count += correct_letter(i, j)

print('there are', xmas_count, 'instances of "XMAS"')


############################# PART 2 #############################

def correct_mas(i, j):
    # check for out of bounds (index must be in 2D array and *not* onthe border)
    if (i <= 0) or (j <= 0) or (i >= len(wordsearch) - 1) or (j >= len(wordsearch) - 1):
        return 0
    
    # array of values diagonally adjacent to our "A"
    corners = [wordsearch[i - 1][j - 1], wordsearch[i - 1][j + 1], wordsearch[i + 1][j - 1], wordsearch[i + 1][j + 1]]

    # If any of the letters aren't an "S" or an "M" or if two opposite corners match we return 0
    for letter in corners:
        if (letter != "S") and (letter != "M"):
            return 0
    if (corners[0] == corners[3]) or (corners[1] == corners[2]):
        return 0
    return 1

# mas_count <- "'MAS' X" counter
mas_count = 0
for i in range(len(wordsearch)):
    for j in range(len(wordsearch[0]) - 1):
        if wordsearch[i][j] == "A":
            mas_count += correct_mas(i, j)

print('there are', mas_count, 'instances of "MAS" X')