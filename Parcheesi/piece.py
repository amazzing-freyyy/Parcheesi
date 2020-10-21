#pice.py
class Piece:

    def __init__(self, color='red', position=0):
        self.color = color
        self.position = position

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

    def move(self, ds, Oplayer_piece):
        '''Moves the piece 'ds' spaces foward.'''
        self.position+=ds
        self.eaten(Oplayer_piece)

    def is_safe(self):
        '''Determines if the piece is in a safe spot.'''
        safe_spots=[0,1,8,13,18,25,30,35,42,47,52,59,
                    64,65,66,67,68,69,70,71,72]
        for i in safe_spots:
            if self.get_position()==i:
                return True

    def convert_position(self,Oplayer_piece,key):
        Oplayer_position= Oplayer_piece.get_position() + key
        if Oplayer_position > 68:
            Oplayer_position=Oplayer_position-68
        return Oplayer_position

    def compare_position(self,Oplayer_position):
        '''Determines whether both players are in the same position'''
        if Oplayer_position == self.get_position():
            return True

    def eaten(self, Oplayer_piece):
        '''Determines if the player piece has eaten another
        player's piece.'''

        key=self.choose_key(Oplayer_piece)
        Oplayer_position=self.convert_position(Oplayer_piece,key)

        if Oplayer_piece.is_safe() and self.compare_position(Oplayer_position):
            Oplayer_piece.set_position(0)
            return True
        else:
            return False

    def choose_key(self,Oplayer_piece):
        if self.color=='red':
            if Oplayer_piece.color=='blue':
                return 17
            elif Oplayer_piece.color=='yellow':
                return 34
            elif Oplayer_piece.color=='green':
                return 51
        elif self.color=='blue':
            if Oplayer_piece.color=='yellow':
                return 17
            elif Oplayer_piece.color=='green':
                return 34
            elif Oplayer_piece.color=='red':
                return 51
        elif self.color=='yellow':
            if Oplayer_piece.color=='green':
                return 17
            elif Oplayer_piece.color=='red':
                return 34
            elif Oplayer_piece.color=='blue':
                return 51
        else:
            if Oplayer_piece.color=='blue':
                return 17
            elif Oplayer_piece.color=='yellow':
                return 34
            elif Oplayer_piece.color=='green':
                return 51