# player.py
from dieview2 import *
#from graphics import *
from Piece import *

class Player:
    
    def __init__(self,color='red'):
        self.color=color
        self.die=[2]
        self.piece=[4]

        #setting die
        for i in range(2):
            self.die[i]=Dice()
        
        #setting color
        for i in range(4):
            self.piece[i]=Piece(color,0)
        
        #piece locations
        self.start=4
        self.end=0
        self.path=0
        
    def release_piece(self,p):
        '''Releases one piece from home to the starting
        point.'''
        for i in range(2):
            if self.die[i].getValue()==5:
                self.piece[p].move(1)
                self.start-=1
                self.path+=1

    def choose_piece(self,i,p,other_player):
        '''Chooses which piece will be moved.'''
        for Oplayer_piece in other_player.piece:
            self.piece[p].move(self.die[i],Oplayer_piece)

    def return_start(self,p):
        '''Returns a piece to it's home position.'''
        self.piece[p].set_position=0
    
    def roll_dices(self):
        '''Rolls both dices.'''
        for i in range(2):
            self.die[i].rollDie()

    def set_ref_num(self,s_num):
        '''Set's reference number.'''
        self.s_num=s_num

    def get_s_num(self):
        '''Return's reference number.'''
        return self.s_num

