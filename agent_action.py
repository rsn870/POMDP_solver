import numpy as np

from my_game import Game
from my_parameters import *
# from algorithm  import * decomment out and choose one of PBVI or new algorithm(s) to check result

# The actions available to the player
actions = ["left", "right", "listen"]

class Agent:
    """
    Any player in the Tiger game.
    """
    def __init__(self):
        self._reward = 0
        self._observation = None

    def act(self, game, action):
        reward, observation = game.agentret(action)
        self._reward += reward
        self._observation = observation

    def update_reward(self, new_reward):
        self._reward += new_reward

    def update_observation(self, new_observation):
        self._observation = new_observation

    def get_reward(self):
        return self._reward

class AI_Agent(Agent):
    """
    An AI agent.
    """
    def __init__(self, bright = 0.5):
        super(AI_Agent, self).__init__()  # we are trying to get overwritten attributes in inherited class 
                                          # basically we wish to initialize rwd  and obs !
        # The belief probability that the agent is in the right state  since there is no weight we initialize with 0.5
        # Note that bleft is simply 1 - bright
        self._bright = bright

  """ def pick_action(self):
        """
        Temporarily using a random strategy.
        """
        return algostrategy(self._bright, step_1_set)   decomment out and replace with strategy func eg Pointbased for PBVI , specific func based on specific method employed
"""
class Human_Agent(Agent):
    """
    A human agent.
    """
    def __init__(self):
        super(Human_Agent, self).__init__()                          #nothing extraneous required here !

    def pick_action(self, action):
        return action
