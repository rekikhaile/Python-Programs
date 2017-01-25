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


# Just generate a list of all the rolls.
# Returning a generator won't work, since it prevents
# us from accesing the data more than 1 time.
def test(dice_string, rolls):
    dice_tuples = list( map(die_tupler, dice_string.split('+')) )
    return list( roll(dice_tuples) for i in range(rolls) )


# For each tuple (n, sides) randoms n rolls
# of a 'sides'-sided die. Sums all the rolls
# up and adds to total.
def roll(dice_list):
    total = 0
    for dice,sides in dice_list:
        total += sum(random.randint(1, sides) for i in range(dice))
    return total


# First we get all the unique rolls from results using set()
#       We iterate through the set and count the occurences.
# Then, we use the acquired data to calculate the mean, so that
#       we are not going through the whole list again.
# Finally, we loop through the list, saving the previous value.
#       If the value is same as prev, increase the streak count.
#       Else, save the streak count if it's a new maximum.
#               Notice .get() method, which returns a 0 if the key is not in the dict.
#       In the end, update the prev to the current element.
def get_stats(results):
    stats = {}
    stats['count'] = dict((throw, results.count(throw)) for throw in set(results))
    stats['average'] = sum(k*v for k, v in stats['count'].items())/len(results)
    stats['streak'] = {}

    streak_total = 0
    prev = None
    for throw in results:
        if throw == prev:
            streak_total += 1
        else:
            if prev is not None:
                stats['streak'][prev] = max(streak_total,stats['streak'].get(prev,0))
            streak_total = 1
        prev = throw

    return stats
    

# A simple timing check
start = time()

# Roll five 8-sided dice a million times.
get_stats(test('5d8',1000000))
print(time() - start)
# Reports around 12.9 sec on my machine.