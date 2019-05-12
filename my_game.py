import numpy as np
import random

from my_model import *
from my_parameters import *

class Game:
    """
    The game itself. Each instance of a game contains two parameters: state
    and time.
    """
     # DO NOT INITIALIZE STATE - FOR UNITTESTING PURPOSES ONLY (MAINLY AS A MEANS TO QUANTIFY UNCERTAINITY AND CONVERGENCE OF ITERATION
  # COMMENT OUT CONSTRUCTOR BEFORE THE GAME IS TO  BE PLAYED (REASON: MAINLY TO AVOID MUTIPLE INITIALISATIONS 1 ONLY PER GAME !)

    def __init__(self, _state = None):
        self._state = _state if _state else np.random.choice(states, p=prob_states)
        self._time = 0

   



    def retState(self):
        return self._state    # A RETURN FUNCTION FOR CURRENT STATE

    def agentret(self, action):
        """
        What the game agent does in response to what the player does ! Basically return the current rewrd + get the new state +obs
        """
        rwrd = Rewardfunc(self._state, action)
        obsrv, self._state = newObservation(self._state, action)
        self._time += 1

        return rwrd, obsrv
