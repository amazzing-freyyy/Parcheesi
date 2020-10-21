#board.py
from player import *

class Board:

    def __init__(self, players):
        if players > 4:
            self.players=4
        elif players <= 1:
            self.players =2

        self.plater=players
        self.player=[self.players]
        
        for i in range(players):
            if i ==0:
                color='red'
            elif i ==1:
                color='blue'
            elif i ==2:
                color= 'green'
            else :
                color='yellow'

            self.player[i]=Player(color)


    