import random
from time import time


# Just generate a list of all the rolls.
# Returning a generator won't work, since it prevents
# us from accesing the data more than 1 time.
def test(dice, sides, rolls):
    return list( roll(dice, sides) for i in range(rolls) )


# Random the roll a number of times and then
# sum it all up and return the value.
def roll(dice,sides):
    return sum(random.randint(1, sides) for i in range(dice))


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
get_stats(test(5,8,1000000))
print(time() - start)
# Reports around 12.5 sec on my machine.