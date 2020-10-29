from jugador import *

class Board:
    '''Clase que maneja funciones del juego.'''

    def __init__(self):
        '''
        Constructor
            -Inicializa una lista de jugadores
            -Rojo->'Red',Azul->'Blue', Amarillo->'Yellow', Verde->'Green'
        '''
        self.jugadores=[Jugador('Red'),Jugador('Blue'),Jugador('Yellow'),Jugador('Green')]

    def ciclo(self, jugador,c):
        '''
        -Maneja el orden de los jugadores
        -'c' determina la cantidad de jugadores que hay jugando
        '''
        if jugador ==(c-1):
            jugador=0
        else:
            jugador+=1
        return jugador

    def turno(self, i, move_or_spawn, pieza,ds):
        '''
        -Le pide al jugador 'i' si quiere mover o spawn a una pieza
            dependiendo de cuantas tenga en el start
        -En caso de que quiera mover, le pide el que quiere mover
            (move_or_spawn=True/False)
        -Por ultimo, chequea si cae en la misma posicion que otro jugador 
            y lo devuelve al mismo a su origen
        -'d' es una lista de 2 dijitos y representa los valores de los dados
        '''
        if ds==5:                                    #Se asegura de que si el valor del dado es 5
            if self.jugadores[i].start==4:          #Si todas las piezas estan en start solo puede spawn
                self.jugadores[i].spawn()
            elif self.jugadores[i].start < 4:       #Si tiene 1,2o3 piezas en el path decide si hace spawn
                if move_or_spawn:                   #   o si mueve
                    self.jugadores[i].move(ds,pieza)
                else:
                    self.jugadores[i].spawn()
            else:                                   #Si nada esta en start mueve automaticamente
                self.jugadores[i].move(ds,pieza)
        else:                                       #Si el valor del dado no es 5 solo puede mover
            self.jugadores[i].move(ds,pieza)
            
        self.comparar_posiciones(i,pieza)           #Compara posiciones con otros jugadores

    def comparar_posiciones(self, i, pieza):
        '''
        -Verifica si la pieza del jugador 'i' callo en la misma posicion de otro jugador.
        '''
        for j in self.jugadores:
            if self.jugadores[i].color==j.color:     #Se asegura que no compare con el mismo color
                continue                                            
            else:
                self.jugadores[i].come_a(j,pieza)    #Setea la posicion del otro jugador en su start

    def gano(self):
        '''
        -Retorna 'True' y el color del ganador
        -Si no hay un ganador retorna 'False'
        '''
        for i in self.jugadores:
            if i.end == 4:                          #Verifica cuantas piezas tiene en el fin
                return True, i.color
            else:
                return False, ''

    def info_jugador(self,i):
        '''
        -Imprime informacion del jugador y sus piezas
        '''
        print(f'\nJugador= {self.jugadores[i].color}\nstart= {self.jugadores[i].start}\npath= {self.jugadores[i].path}\nend= {self.jugadores[i].end}\n')
        if self.jugadores[i].start == 4:
            print('No hay piezas en el path')
        else:
            for j in self.jugadores[i].piezas:
                if j.spot!=0:                                                                         #Deja saber que piezas estan en el path y su distacia por recorer
                    print(f'Pieza {self.jugadores[i].piezas.index(j)+1} esta a {64+self.jugadores[i].last_spot+8-j.spot} del end.')

                    if j.safe:
                        print(f'Pieza {self.jugadores[i].piezas.index(j)+1} esta safe.')                #Deja saber si la pieza esta safe
                
    def chequea_spot(self, i, j):
        '''
        -Retorna True si la pieza que se entro no esta en path
        '''
        if (self.jugadores[i].piezas[j].spot == 0 or self.jugadores[i].piezas[j].spot== 72 or             #Asegura que la pieza no este en end ni start
            self.jugadores[i].piezas[j].spot== 80 or self.jugadores[i].piezas[j].spot== 88 or
            self.jugadores[i].piezas[j].spot== 96) :
            
            return True