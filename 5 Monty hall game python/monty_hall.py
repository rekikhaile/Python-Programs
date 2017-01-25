import random
##import pylab

def one_try():
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)
    choice = doors.pop(0)
    doors.remove('goat')
    # True if stick wins
    return choice == 'car'


def run_trials(trials):
    stick_wins = 0
    swap_wins = 0
    for t in range(trials):
        if one_try():
            stick_wins += 1
        else:
            swap_wins += 1

    return (stick_wins, swap_wins)

def display_sim(sim_result, title):
    stick_wins, swap_wins = sim_result
    pylab.pie([stick_wins, swap_wins],
              colors = ['r', 'c'],
              labels = ['stick', 'change'],
              autopct = '%.2f%%')
    pylab.title(title)

print(run_trials(100))

#sim_result = run_trials(10000)
##display_sim(sim_result, 'Monty hall')
##pylab.show()



    
    
        
    
