import random
from time import time


# Splits 'ndx' by 'd', checks if 'n' is missing
# and replaces it with '1' if it is.
# Returns a tuple( int(n), int(d) )
def die_tupler(die):
    die_list = die.split('d')
    if die_list[0] == '':
        die_list[0] = '1'
    return tuple( map(int, die_list) )


# Yield the roll. This is a generator function:
# it returns one value at a time, not the whole list at once.
# This also prevents us from using list methods or accessing 
# the data multiple times.
def test(dice_string, rolls):
    dice_tuples = list( map(die_tupler, dice_string.split('+')) )
    for i in range(rolls):
        yield roll(dice_tuples)


# For each dice tuple, we create a list of all sides that the die has.
# We pick a random side from that list N times. Then we sum them up and add to total.
# 
# This saves us from generating a lot of ranges using
# random.randrange() or random.randint().
def roll(dice_list):
    total = 0
    for dice,sides in dice_list:
        sides_list = list(range(1,sides+1))
        total += sum(sides_list[int(random.random() * len(sides_list))] for i in range(dice))
    return total
    


# We iterate over the results one time, saving the previous result to prev.
#   First, we increment the corresponding count entry.
#   Then, we update the streak_count if it's bigger than the current
#       streak count of the result in question.
#   Finally, update prev to be the curent result.
# Then use the acquired data in COUNT to calculate the average.
# Finally, return the dictionary.
# Shortcuts COUNT and STREAK are used for convenience, so we won't have
#       to type stats['count'][throw] instead of shorter COUNT[throw]
def get_stats(results):
    COUNT = {}
    STREAK = {}
    prev = None
    streak_total = 0
    for i,throw in enumerate(results):

        if throw not in COUNT:
            COUNT[throw] = 0
        COUNT[throw] += 1

        if throw == prev:
            streak_total += 1
        else:
            if prev is not None:
                if prev not in STREAK:
                    STREAK[prev] = 0
                if streak_total > STREAK[prev]:
                    STREAK[prev] = streak_total
            streak_total = 1

        prev = throw
    stats = {'count' : COUNT , 'streak' : STREAK}
    stats['average'] = sum(k*v for k,v in COUNT.items())/i
    return stats




# A simple timing check
start = time()

# Roll five 8-sided dice a million times.
get_stats(test('5d8',1000000))
print(time() - start)
# Reports around 6.4 sec on my machine.