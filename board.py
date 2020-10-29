#board.py
from jugador import *

class Board:
    '''Clase que maneja funciones del juego.'''

    def __init__(self):
        '''
        Constructor
            -Inicializa una lista de jugadores
            -Rojo->'R',Azul->'B', Amarillo->'Y', Verde->'G'
        '''
        self.jugadores=[Jugador('R'),Jugador('B'),Jugador('Y'),Jugador('G')]

    def ciclo(self, jugador):
        '''
        -Maneja el orden de los jugadores
        '''
        if jugador ==3:
            jugador=0
        else:
            jugador+=1
        return jugador

    def turno(self, i, move_or_spawn, pieza,d):
        '''
        -Le pide al jugador 'i' si quiere mover o spawn a una pieza
            dependiendo de cuantas tenga en el start
        -En caso de que quiera mover, le pide el que quiere mover
            (move_or_spawn=True/False)
        -Por ultimo, chequea si cae en la misma posicion que otro jugador 
            y lo devuelve al mismo a su origen
        -'d' es una lista de 2 dijitos y representa los valores de los dados
        '''
        for j in d:
            if j==5:                                    #Se asegura de que si el valor del dado es 5
                if self.jugadores[i].start==4:          #Si todas las piezas estan en start solo puede spawn
                    self.jugadores[i].spawn()
                elif 0<self.jugadores[i].start<4:       #Si tiene 1,2o3 piezas en el path decide si hace spawn
                    if move_or_spawn:                   #   o si mueve
                        self.jugadores[i].move(j,pieza)
                    else:
                        self.jugadores[i].spawn()
                else:                                   #Si nada esta en start mueve automaticamente
                    self.jugadores[i].move(j,pieza)
            else:                                       #Si el valor del dado no es 5 solo puede mover
                self.jugadores[i].move(j,pieza)
            
            self.compare_positions(i,pieza)             #Compara cosiciones con otros jugadores

    def compare_positions(self, i, pieza):
        '''
        -Verifica si la pieza del jugador 'i' callo en la misma posicion de otro jugador.
        '''
        for j in self.jugadores:
            if self.jugadores[i].color==j.color:    #Se asegura que no compare con el mismo color
                continue                                            
            else:
                self.jugadores[i].come_a(j,pieza)    #Setea la posicion del otro jugador en su start