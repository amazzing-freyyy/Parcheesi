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
                s_num=1
            elif i ==1:
                color='blue'
                s_num=2
            elif i ==2:
                color= 'green'
                s_num=3
            else :
                color='yellow'
                s_num=4

            self.player[i]=Player(color,s_num)


    