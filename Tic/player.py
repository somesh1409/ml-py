import numpy as np
import pickle

BOARD_ROWS = 3
BOARD_COLS = 3

class Player:
    def __init__(self, name, exp_rate=0.3, printStatesBool = False):
        self.name = name
        self.states = []  # record all positions taken
        self.lr = 0.3
        self.exp_rate = exp_rate
        self.decay_gamma = 1
        self.states_value = {}  # state -> value
        self.printStatesBool = printStatesBool

    def getHash(self, board):
        boardHash = str(board.reshape(BOARD_COLS * BOARD_ROWS))
        return boardHash

    def chooseAction(self, positions, current_board, symbol):
        if np.random.uniform(0, 1) <= self.exp_rate:
            # take random action
            idx = np.random.choice(len(positions))
            action = positions[idx]
        else:
            value_max = -999
            self.board_states = np.zeros((BOARD_ROWS, BOARD_COLS))
            for p in positions:
                next_board = current_board.copy()
                next_board[p] = symbol
                next_boardHash = self.getHash(next_board)
                value = 0 if self.states_value.get(next_boardHash) is None else self.states_value.get(next_boardHash)
                # print("value", value)
                self.board_states[p] = value
                if value >= value_max:
                    value_max = value
                    action = p
        # print("{} takes action {}".format(self.name, action))
            if (self.printStatesBool):
                print('Board State Values')
                for i in range(0, BOARD_ROWS):
                    print('-------------')
                    out = '| '
                    for j in range(0, BOARD_COLS):
                        out += str(round(self.board_states[i, j],2)) + ' | '
                    print(out)
                print('-------------')
        return action

    # append a hash state
    def addState(self, state):
        self.states.append(state)

    # at the end of game, backpropagate and update states value
    def feedReward(self, reward):
        for st in reversed(self.states):
            if self.states_value.get(st) is None:
                self.states_value[st] = 0
            self.states_value[st] += self.lr * (self.decay_gamma * reward - self.states_value[st])
            reward = self.states_value[st]
            # print(st, ': ', reward)
        # print('------')

    def reset(self):
        self.states = []

    def savePolicy(self):
        fw = open('policy_' + str(self.name), 'wb')
        pickle.dump(self.states_value, fw)
        fw.close()
        print('Policy Saved')
        # print(self.states_value)

    def loadPolicy(self, file):
        fr = open(file, 'rb')
        self.states_value = pickle.load(fr)
        fr.close()
        print('Policy Loaded')
        # print(self.states_value)

class HumanPlayer:
    def __init__(self, name):
        self.name = name

    def chooseAction(self, positions):
        while True:
            row = int(input("Input your action row:"))
            col = int(input("Input your action col:"))
            action = (row, col)
            if action in positions:
                return action

    # append a hash state
    def addState(self, state):
        pass

    # at the end of game, backpropagate and update states value
    def feedReward(self, reward):
        pass

    def reset(self):
        pass
