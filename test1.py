import unittest

# Test 1 for uncertainity common to both models
from my_game import Game

class tigerTest(unittest.TestCase):

    def testStateAfterListen(self):
        game = Game()
        # testing 10 times to account for uncertainty
        for i in range(10):
            old_state = game.retState()
            game.agentret("listen")
            new_state = game.retState()
            self.assertFalse(old_state != new_state)  # We will get info regarding test failure msg+name so that's ok .We wish to ensure ideally no repetition that is uncertainity should be pretty here or actually random choices as per game idea

def main():
    unittest.main()

if __name__ == '__main__':   
    main()
