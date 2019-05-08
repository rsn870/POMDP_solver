import numpy as np

from my_parameters import *


 ##Transition Function that returns the probability of reaching the FINAL state from  the INITIAL state
 ## taking ACTION.

def transition(initial, action, final):
    if action == "listen":
        return (initial == final) * 1        
    elif action == "left" or action == "right":
        return 0.5                  # for listening the prob of reaching final from initial when both are same is 1 by def


# since there is no weightage here there is an equal probability that you're right or wrong (hope so !) so 0.5 is pretty apt



# Function that returns the probability of getting some  OBSERVATION after taking some ACTION
# to land in  a particluar STATE. Obs transition faction

def obstransition(observation, action, state):
    if action == "left" or action == "right":
        return 0.5
    elif action == "listen":
        return p_correct if (observation == state) else 1-p_correct

# again these follow from the game since there's no specific weightage for left/right and there is for listening



#Reward Function

def Rewardfunc(state, action):
    if action == "listen":
        return -1
    elif action == "left" or action == "right":
        if action != state:
            return 10
        else:
            return -100
# Listening carries a penalty when action is not the same as state means you're safe for the moment not so for the other case


#Function that returns an observation and a new state to which the game is
# reinitialised after taking ACTION in STATE.

def newObservation(state, action):
    if action == "listen":
        if state == "left":
            observation = np.random.choice(observations, p=1-pro)  # let's make this as random as possible 
        elif state == "right":
            observation = np.random.choice(observations, p=pro)
    elif action == "left" or action == "right":
        observation = np.random.choice(observations)
        # let's go for reinitializing state randomly
        state = np.random.choice(states, p=prob_states)
    return observation, state
