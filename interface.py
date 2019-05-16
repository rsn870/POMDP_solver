"""
Runs an instance of the tiger game. Command line input has the following format:

python play.py [player] [iterations]

player: The options are "Human" or "AI". If playing with a human player, the
user will be prompted with "What action would you like to make? " The options
are "left", "right" or "listen". The options are case sensitive. If playing with
an AI player, the player will play according to the predetermined strategy.

iterations: The number of  steps over which the game is played.
"""

import sys        #I'm including sys prcisely for sys.exit() etc which are useful in production ready code ! 
                  # you are free to use os or quit in scope of your system for more user-friendly experience 
import numpy as np

from my_game import Game
from agent_action import Agent, AI_Agent, Human_Agent

# _state variable exists for testing only - do not initialize
def play(player, iterations, _state = None):
    time = 0       # we initialize to 0 to ensure that bound of iterations is not crossed
    game = Game()
    if player == "AI":
        player = AI_Agent()
    elif player == "Human":
        player = Human_Agent()
    while time < iterations:
        print("Step " + str(time + 1) + ":"+"\n")
        if isinstance(player, Human_Agent):      # if player is human ! player is object of Human_Agent
            if time == iterations - 1:
                print(">>  This is the final move that you have ! Do your best !")
            move = input(">> What action would you like to take ?")
            move = player.pick_action(move)
        else:
            move = player.pick_action()
        print("You chose to make this move: " + str(move)+"\n")
        reward, observation = game.agentret(move)
        if move not in ("listen", "left", "right"):
            print(">> Illegal move encountered .System anomaly the exeution is being terminated (PS: no cheating !)")
            sys.exit()
        player.update_observation(observation)
        if move == "listen":
            print("> You chose to listen!")
            tiger_sound(observation)
        player.update_reward(reward)
        print("> You received a reward of " + str(reward) + "\n")
        time += 1
    print(">> Game over! Total Reward received is : " + str(player.get_reward()) + "\n")

def tiger_sound(observation):
    print(">> The tiger sound came from the " + observation + " door")

if __name__ == "__main__":       # ensures execution
    args = sys.argv     # the variable no of arguments is equal to the no passed in command line 
    #  to know whether the player is human or AI
    player = args[1]
    # the number of time steps over which the game occurs
    iterations = int(args[2])

    play(player, iterations)
