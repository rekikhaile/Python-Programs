import random

def roll(number_of_dice, sides_per_dice):
    total = 0

    for i in range(number_of_dice):
        total += random.randint(1, sides_per_dice)

    return total

def test(number_of_dice, sides_per_dice, number_of_rolls):
    results = []

    for i in range(number_of_rolls):
        results.append(roll(number_of_dice, sides_per_dice))

    return results

def get_stats(results):
    statistics = {}

    statistics["count"] = {}
    statistics["sequence"] = {}

    total = 0
    roll_count = len(results)
    current_sequence_value = -1
    current_sequence_length = 0

    for result in results:
        if result == current_sequence_value:
            current_sequence_length += 1
        else:
            current_sequence_value = result
            current_sequence_length = 1
        
        try:
            statistics["count"][result] = statistics["count"][result] + 1

            if current_sequence_length > statistics["sequence"][result]:
                statistics["sequence"][result] = current_sequence_length
        except KeyError:
            statistics["count"][result] = 1
            statistics["sequence"][result] = 1

        total += result

    statistics["average"] = float(total) / roll_count

    return statistics
