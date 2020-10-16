#pice.py
class Piece:

    def __init__(self, color, position):
        self.color = color
        self.position = 0
        self.is_safe=False

    def set_position(self,newPosition):
        '''Sets the position of the piece.
        There are 73 different positions from 0 to 72.'''
        self.position=newPosition

    def set_color(self,color):
        '''Set the color of the piece.'''
        self.color=color

    def get_position(self):
        '''Returns the position of the piece'''
        return self.position

    def get_color(self):
        '''Return the color of the piece.'''
        return self.color

    def move(self, ds):
        '''Moves the piece 'ds' spaces foward.'''
        self.position+=ds
        self.safe()

    def safe(self):
        '''Determines if the piece is in a safe spot.'''
        safe_spots=[0,1,8,13,18,25,30,35,42,47,52,59,
                    64,65,66,67,68,69,70,71,72]
        for i in safe_spots:
            if self.get_position()==i:
                self.is_safe=True