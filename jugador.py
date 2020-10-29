#jugador.py
from random import seed
from random import randint
from pieza import *

class Jugador:
    '''Clase para los jugadores de Parcheesi'''

    def __init__(self,color):
        '''Constructor
            -Inicializa la lista de piezas
            -Asigna el color dado en los parametros (R,B,Y,G)
            -Deja saber que hay 4 piezas en start y 0 en el path y home
            -Crea una lista de safe_spots donde las piezas no se pueden comer
            -Las variables start,path y end le deja saber al programa cuantas piezas
                hay en cada las 3 localizaciones'''
        self.color=color
        self.piezas=[Pieza(), Pieza(), Pieza(), Pieza()]
        self.start=4
        self.path=0
        self.end=0
        self.safe_spots=[5,11,16,21,27,32,37,43,48,53,59,64]

    def roll_dices(self):
        '''
        -Retorna 2 valores diferentes que representan las tiradas de los dados
        '''
        return randint(1,6), randint(1,6)

    def spawn(self):
        '''
        -Mueve a una pieza desde su start a el primer spot.
        -Cada color tiene un spot distinto.
        -Le resta 1 a start y le anade uno a path
        '''
        for i in self.piezas:
            if i.spot==0:                    #Se asegura de que la pieza que va a sacar esta en start
                self.start-=1
                self.path+=1
                if self.color == 'R':       #Se asegura del color del jugador para spawn a su pieza en
                    i.spot=5                #   en el spot correcto
                    break
                elif self.color== 'B':
                    i.spot=21
                    break
                elif self.color== 'Y':
                    i.spot=37
                    break
                else:
                    i.spot=53
                    break
            else:
                continue

    def move(self,ds,i):
        '''
        -Mueve a la pieza 'i' una cantidad de pasos 'ds'
        -Retorna False si la pieza 'i' esta en start
        -Retorna True si la pieza 'i' esta en path
        '''
        if self.piezas[i].spot==0:                           #Se asegura que la pieza no este en start
            return False  #nada

        else:
            spot_nuevo=self.piezas[i].spot + ds             #Se anade 'ds' a el spot de la pieza 'i' en 
                                                            #   en una variable aparte para verificar
            if self.color=='R':                             #Como el ultimo spot de 'R' es 64
                pass #nada                                  #   no hay que hacer el ciclo
            else:
                if spot_nuevo > 64:                         #Ciclo circular de los spots
                    spot_nuevo=spot_nuevo-64

            if self.color=='R' and spot_nuevo > 64:         #Verificaciones para chequear si la pieza esta
                self.end_spot_verificacion(72, spot_nuevo,i)  #   en el end path
            
            elif self.color=='B' and spot_nuevo > 16:
                spot_nuevo = 16 - self.piezas[i].spot + 72
                self.end_spot_verificacion(80, spot_nuevo,i)

            elif self.color=='Y' and spot_nuevo > 32:
                spot_nuevo = 32 - self.piezas[i].spot + 80
                self.end_spot_verificacion(88, spot_nuevo,i)
            
            elif self.color=='G' and spot_nuevo > 48:
                spot_nuevo = 48 - self.piezas[i].spot + 88
                self.end_spot_verificacion(96, spot_nuevo,i)

            for j in self.safe_spots:                       #Compara el spot de la pieza 'i' para determinar
                if self.piezas[i].spot == j:                #   si esta en un safe spot
                    self.piezas[i].safe = True
                    break
                else:
                    self.piezas[i].safe = False

            return True

    def end_spot_verificacion(self, end_spot, spot_nuevo,i): 
        '''
        -Solo se usa en la funcion de 'move' para determinar si la pieza llego al end
        -Sirve para acortar el codigo
        '''
        if spot_nuevo > end_spot:
            self.piezas[i].spot = end_spot
            self.end += 1
            self.path -= 1
        else:
            self.piezas[i].spot = spot_nuevo

    def come_a(self, o_jugador,i):
        '''
        -Verifica si la pieza 'i' del jugador esta en el mismo sitio que 
            alguna pieza de 'o_jugador'
        -Si la pieza encuentra alguna que este en el mismo spot manda a la pieza de 'o_jugador'
            para su start
        '''
        for j in o_jugador.piezas:
            if j.safe:                              #Si 'safe' es True, hace nada
                continue #nada
            else:
                if self.piezas[i].spot==j.spot:
                    j.spot = 0
                    j.safe = True
                    o_jugador.path -= 1
                    o_jugador.start += 1
                else:
                    continue #nada