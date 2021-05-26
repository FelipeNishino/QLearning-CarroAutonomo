from random import choice, random
from tabulate import tabulate
from Constants import *
from time import sleep
import numpy as np
import os

class QLearn():
    def __init__(self, alfa, gama, epsilon, epsilonDecay, epsilonMin, rewards, environment):
        self.alfa = alfa
        self.gama = gama
        self.epsilon = epsilon
        self.epsilonDecay = epsilonDecay
        self.epsilonMin = epsilonMin
        self.rewards = rewards
        self.environment = environment
        self.previousState = {}
        self.State = {}
        
    def initializeStates(self):
        for row in range(10):
            for column in range(10):
                    for direction in Directions:
                        self.previousState[f"{row}{column}{direction.value}"] = 0
                        self.State[f"{row}{column}{direction.value}"] = 0

    def checkBoundaries(self, state, action):
        row, column = int(state[0]) , int(state[1])
        
        if action == Directions.UP: return f"{max(row - 1, 0)}{column}", self.environment[max(row - 1,0)][column]
        elif action == Directions.RIGHT: return f"{row}{min(column + 1, 9)}", self.environment[row][min(column + 1, 9)]
        elif action == Directions.DOWN: return f"{min(row + 1, 9)}{column}", self.environment[min(row + 1, 9)][column]
        elif action == Directions.LEFT:  return f"{row}{max(column - 1, 0)}", self.environment[row][max(column - 1, 0)]

    def reward(self, state, action):
        futurePos, symbol = self.checkBoundaries(state, action)
        return self.rewards[c] if futurePos == state else self.rewards[symbol]

    def Q(self, state, action):
        futurePos, symbol = self.checkBoundaries(state, action)

        val = []
        if symbol in [c, p, t]:
            val.append(self.rewards[symbol])
        else:
            for direction in Directions:
                val.append(self.previousState[f"{futurePos}{direction.value}"])

        return self.previousState[f"{state}{action.value}"] + self.alfa * (self.reward(state, action) + self.gama * np.max(val) - self.previousState[f"{state}{action.value}"])

    def getInitialPosition(self):
        pos = []
        for row in range(10):
            for column in range(10):
                if self.environment[row][column] == b:
                    pos.append((row,column))
        return choice(pos)

    def train(self, maxGen):
        self.initializeStates()

        for generation in range(maxGen):
            if generation % 100 == 0: print(f"Geração {generation}/{maxGen}")
            initialPosAgent = self.getInitialPosition()
            
            state = f"{initialPosAgent[0]}{initialPosAgent[1]}"
            
            for o_0 in range(200):
                self.State[f"{state}{Directions.UP.value}"] = self.Q(state, Directions.UP)
                self.State[f"{state}{Directions.RIGHT.value}"] = self.Q(state, Directions.RIGHT)
                self.State[f"{state}{Directions.DOWN.value}"] = self.Q(state, Directions.DOWN)
                self.State[f"{state}{Directions.LEFT.value}"] = self.Q(state, Directions.LEFT)
                
                possibleActions =  [ 
                    self.State[f"{state}{Directions.UP.value}"],
                    self.State[f"{state}{Directions.RIGHT.value}"],
                    self.State[f"{state}{Directions.DOWN.value}"],
                    self.State[f"{state}{Directions.LEFT.value}"] 
                ]

                action = choice(list(Directions)) if random() < self.epsilon else Directions(np.argmax(possibleActions))

                state, o_0 = self.checkBoundaries(state, action)

                self.previousState = self.State.copy()

            self.epsilon *= self.epsilonDecay
            self.epsilon = max(self.epsilon, self.epsilonMin)
        print(f"Geração {maxGen}/{maxGen}")

    def exec(self, row , column):
        state = f"{row}{column}"
        self.draw((row,column))    

        while (self.environment[row][column] != t):
            possibleActions =  [ 
                self.State[f"{state}{Directions.UP.value}"],
                self.State[f"{state}{Directions.RIGHT.value}"],
                self.State[f"{state}{Directions.DOWN.value}"],
                self.State[f"{state}{Directions.LEFT.value}"] 
            ]

            action = Directions(np.argmax(possibleActions))
            print(f"Direction: {symbolToUnicode[action.value]}")
            state, o_0 = self.checkBoundaries(state, action)
            row, column = int(state[0]), int(state[1])
            self.draw((row,column))

    def draw(self, carPosition):        
        sleep(0.4)
        os.system('cls' if os.name=='nt' else 'clear')
        table = []
        for row in range(10):
            col = []
            for column in range(10):
                if (row, column) == carPosition:
                    col.append("🛺")
                else:
                    col.append(symbolToUnicode[self.environment[row][column]])
            table.append(col)

        print(tabulate(table, [], tablefmt="fancy_grid"))
        