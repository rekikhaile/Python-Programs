import random

##coins = int(input("Please enter the number of coins you start with: "))
##goal = int(input("Please enter your desired goal: "))
##trials = int(input("Please enter the number of trials: "))
##init_trials = trials
##
##print(coins, goal, trials)
####coins = 7
####goal = 10
####trials = 100
##wins = 0
##bets = 0

def one_try(coins,goal):
    bets = 0
    while 0 < coins < goal:
        coins += (1 if random.randint(0,1) else -1)
        bets += 1
    return bets, coins==goal

def start_simulating(coins,goal,tries):
    results = []
    for i in range(tries):
        results.append(one_try(coins,goal))
    return results
        
def averages(results):
    total = len(results)
    wins = len([game for game in results if game[1]])
    avg_winrate = wins/total * 100.0
    print(avg_winrate)



##while trials != 0:
##    start_coins = coins
##    desired_goal = goal
##    while start_coins > 0 and start_coins < goal:
##        choice = random.randint(0, 1)
##        if choice == 0:
##            start_coins += 1
##        else:
##            start_coins -= 1
##        bets += 1
##        
##    trials -= 1
##    if start_coins == desired_goal:
##        wins += 1
##
##
####print('The number of bets is %s\n' % number_of_bets, 'Victory' if wins else 'Loss')
##print('The ratio of wins/trials is %0.2f' % (wins/init_trials * 100))
##print('The average number of bets is %s' % (bets//init_trials)) 
