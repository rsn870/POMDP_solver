import numpy as np


### Basic Game Parameters

# The states of the Game
states = ["left", "right"]

# Probabilities with which the states are initialized (pright is probability of
# the state being initalized as left we assume that there is no 'weight' b/w deciding l or r so we initialize to 0.5)
pright = 0.5
prob_states = [pright,1-pright]  # we make an array prob_states to keep track of probs throughout the progress of the game

# The actions that are available to the player
actions = ["left", "right", "listen"]

# The observations which are  returned to the player after every actions
observations = ["left", "right"]

# The probability of getting the correct observation (and wrong observation)
# by listening( the assumption of an initial  75 % accuracy seems decent will update to check what effects does it have (Prediction :Should determine 'risking' nature of AI )
p_correct = 0.75
pro = np.array([p_correct, 1-p_correct]) # So here a (2,) an array is being created here so using the more convenient np.array()


### Value Iteration Parameters

# The discount factor used in value iteration
GAMMA = 1 # Firstly every choice in the game is independent from the previous so there's no inherent discount plus beacuse
          # of the low number of states here I predict a finite Time Horizon so again I don't think that the need for a discount arises
          # therefore keeping it to 1

# each plan is a triplet 
# (action to be taken , a mapping from observation to the current set of conditional planes ( which observation to follow), alpha vector(a # vector where ith component is the value of a conditional Value function at ith state )
# initial  plan ( we initialize to none action , no observation , (alpha vector over two states -left and right )
initial_plan = (None, None, [0, 0])

# a zero map from observations to plans in old set
zero_map = {"left": initial_plan, "right": initial_plan}   # left-> form initial plan and right as well

# set of height 1 plans ( each policy is a tree so we begin for the first height where we have 3 acts)
step_1_set = [("left", trivial_map, []), ("listen", trivial_map, []), ("right", trivial_map, [])]
