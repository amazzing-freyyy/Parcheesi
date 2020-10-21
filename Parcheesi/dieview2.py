# dieview2.py
#from graphics import *
from random import randint
 
class Dice:
    def __init__(self):
        
        self.rollDie()

    def rollDie(self):
        '''Simulates a dice roll by asigning a
        random value between 1 and 6'''
        self.value=randint(1,6)

    def getValue(self):
        '''Return value of the dice'''
        return self.value()