from graphics import *
from Piece import *

class Player:

    inside_pieces = 4
    outside_pieces = 0
    home_pieces = 0

    def __init__(self, win, color):
        self.color = color
        self.win = win
        p1 = Piece(win, color)
        p2 = Piece(win, color)
        p3 = Piece(win, color)
        p4 = Piece(win, color)

    def add_inside(self):
        self.inside_pieces += 1
        self.outside_pieces -= 1

    def add_outside(self):
        self.outside_pieces += 1
        self.inside_pieces -= 1

    def add_home(self):
        self.home_pieces += 1
        self.inside_pieces -= 1

    def get_inside(self):
        return self.inside_pieces

    def get_outside(self):
        return self.outside_pieces

    def get_home(self):
        return self.home_pieces

    def move(self, n, places_to_move):
        if n == 1:
            self.p1.move(places_to_move)
        elif n == 2:
            self.p2.move(places_to_move)
        elif n == 3:
            self.p3.move(places_to_move)
        else:
            self.p4.move(places_to_move)


def main():
    win = GraphWin()
    player_1 = Player(win, 'red')
    player_1.move(10, 2, 2)
