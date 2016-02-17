'''
simulation of the monty hall problem.
Author: Hasan Iqbal
'''
import random

change_wins = 0
no_change_wins = 0

num_tests = 10000

for j in xrange(0, num_tests):
    case = []
    choices = [0, 1, 2]
    random_int = random.randint(1, 3)
    if random_int == 1:
        case = [1, 0, 0]
    elif random_int == 2:
        case = [0, 1, 0]
    else:
        case = [0, 0, 1]
    #sample test case: [0, 1, 0], meaning, the car is behind the second door, array index 1
    init_guess = random.randint(0, 2)
    correct_idx = case.index(1) # correct car index

    if(init_guess == correct_idx):
        no_change_wins += 1 #in this case, obviously changing would loose
    else:
        opened_door = set(choices) - set([correct_idx]) - set([init_guess]) #host opens the other door
        changed_guess_set = set(choices) - set([init_guess]) - set(opened_door) #player changes his mind
        changed_guess =  list(changed_guess_set)[0] #player selects the the other door
        if(changed_guess == correct_idx): #obviously it's correct!
            change_wins += 1

print (change_wins/float(num_tests))*100
print (no_change_wins/float(num_tests))*100