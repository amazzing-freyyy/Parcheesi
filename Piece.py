from graphics import *


class Piece:
    times_moved = 0  # Variable to check times moved by the piece.

    def __init__(self, win, color, x, y):
        self.color = color
        self.win = win
        self.shape = Circle(Point(self.x, self.y), 17)
        self.shape.setFill(color)
        self.x = self.shape.getCenter().geX()
        self.y = self.shape.getCenter().getY()
        self.startX = x
        self.startY = y


    def get_position(self):
        return self.shape.getCenter()

    def get_color(self):
        return self.color

    def return_home(self):
        self.x = 0
        self.y = 0

    def move(self, times):
        for x in range(times):
            if self.times_moved == 63:  # Move when the piece has traveled all around.
                if self.y == 29:
                    self.shape.move(0, 41.5)  # Movement for blue Pieces
                elif self.y == 994.5:
                    self.shape.move(0, -41.5)  # Movement for Green Pieces
                elif self.x == 28.5:
                    self.shape.move(41.5, 0)  # Movement for Yellow Pieces
                else:
                    self.shape.move(-41.5, 0)  # Movement for Red Pieces

            elif self.x == 400 and self.y == 319.5:  # When the piece is in C1(Corner 1)
                self.shape.move(-80, 40)

            elif self.x == 28.9 and self.y == 509:  # When the piece is in C1(Corner 2)
                self.shape.move(82, 87)

            elif self.x == 617 and self.y == 745.5:  # When the piece is in C3(Corner 3)
                self.shape.move(84, -85)

            elif self.x == 701 and self.y == 401:  # When the piece is in C3(Corner 3)
                self.shape.move(-80, -40)

            elif self.x == 400:
                self.shape.move(0, 41.5)

            elif self.y == 401:
                self.shape.move(-41.5, 0)

            elif self.y == 617:
                self.shape.move(41.5, 0)

            elif self.x == 617:
                self.shape.move(0, -41.5)

            self.times_moved += 1

    def returnToSpawn(self):
        # Move the Piece to the Spawn Coordinates
        while self.x != self.startX or self.startY != 29:
            if self.x > self.startX:
                self.shape.move(-1, 0)
            elif self.x < self.startX:
                self.shape.move(1, 0)

            if self.y > self.startY:
                self.shape.move(0, -1)
            elif self.y > self.startY:
                self.shape.move(0, 1)
