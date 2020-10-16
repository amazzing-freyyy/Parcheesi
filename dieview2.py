# dieview2.py
#from graphics import *
from random import randint
 
class Dice:
    def __init__(self):
        
        self.rollDie()

    def rollDie(self):
        self.value=randint(1,6)

    def getValue(self):
        return self.value()