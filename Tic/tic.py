import numpy as np
import arcade

# sys.path.append(".")
from player import Player
from player import HumanPlayer
from state import State

from numpy.core.numeric import cross

BOARD_ROWS = 3
BOARD_COLS = 3

if __name__ == "__main__":
    # training
    p1 = Player("p1")
    p2 = Player("p2")
    p1 = Player("p1", printStatesBool=False, exp_rate=0)
    p2 = Player("p2", printStatesBool=False, exp_rate=0)
    # load previous policy
    p1.loadPolicy("policy_p1")
    p2.loadPolicy("policy_p2")

    st = State(p1, p2, printBoard=False)
    print("training...")
    st.play(10000)

    # save policy
    p1.savePolicy()
    p2.savePolicy()

    # play with human
    p1 = Player("computer", exp_rate=0, printStatesBool=True)
    p1.loadPolicy("policy_p1")

    p2 = HumanPlayer("human")

    st = State(p1, p2)
    # st.play2()

    # arcade.run()