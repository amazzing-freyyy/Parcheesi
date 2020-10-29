#Parcheesi game
from board import *

def main():
    #Usuario entra la cantidad de jugadores y el programa valida que este entre 2 y 4
    c=int(input('Bienvenido a Parcheesi\nEntre la cantidad de jugadores: '))
    while not 2<=c<=4:
        c=int(input('La cantidadd e jugadores debe ser entre 2 y 4.\nEntre nuevamente: '))

    ganador=''                      #variable que guarda el primero que tenga todas sus piezas en end
    d=[0,0]                         #lista de valores de dados
    i=0                             #variable contadora para los jugadores
    alguien_gano=False               #variable que indica si alguien gano
    board=Board()                   #inicializacion de Board()
    while not alguien_gano:
        print('---------------------')
        board.info_jugador(i)       #imprime info del jugador

        q=input("\nPresione 'Enter' para tirar dados o 'q' para salir del juego... ")
        if q=='q':
            break
        d[0],d[1]=board.jugadores[i].roll_dices()       #asigna valores de los dados y se imprimen
        print(d)

        move_or_spawn=False             #variable que indica si el jugador va a spawn o move una pieza
        pieza=0                         #en caso de que el jugador no tenga piezas en el path
        for ds in d:                                                                                            #Loop por dado
            if board.jugadores[i].start != 4:                                                                   #Si el jugador tiene 4 en start solo puede spawn
                if  ds==5:                                                                                      #verifica si el dado es 5
                    move_or_spawn= bool(int(input("Entra '1' si quieres mover o '0' para spawn: ")))            #Jugador decide si mover o spawn a un pieza
                    if move_or_spawn:
                        pieza= int(input('\nIndica la pieza que quieres mover: '))                              #Jugador entra la pieza que quiere mover y la valida
                        while not 1<=pieza<=4:
                            pieza= int(input('Esa pieza no existe. Entra nuevamente la pieza: \t'))
                        while board.chequea_spot(i,pieza):
                            pieza= int(input('Esa pieza no esta en el path. Entra otra pieza: \t'))
                else:                                                                                           #Si el dado no es 5 solo mueve
                    move_or_spawn=True
                    pieza= int(input('\nIndica la pieza que quieres mover: '))                                  #Jugador entra la pieza que quiere mover y la valida
                    while not 0<pieza<5:
                        pieza= int(input('Esa pieza no existe. Entra nuevamente la pieza: \t'))
                    while board.chequea_spot(i,pieza-1):
                        pieza= int(input('Esa pieza no esta en el path. Entra otra pieza: \t'))
            
            elif board.jugadores[i].start ==0:                                                                  #Si no hay piezas en start solo mueve
                move_or_spawn=True
                pieza= int(input('\nIndica la pieza que quieres mover: '))                                  #Jugador entra la pieza que quiere mover y la valida
                while not 0<pieza<5:
                    pieza= int(input('Esa pieza no existe. Entra nuevamente la pieza: \t'))
                while board.chequea_spot(i,pieza-1):
                    pieza= int(input('Esa pieza no esta en el path. Entra otra pieza: \t'))
            
            else:                                                                                               #Si las piezas estan en start hacen spawn automaticamente
                pass

            board.turno(i,move_or_spawn,pieza-1,ds)    #Realiza las deciciones del jugador
            if move_or_spawn:       
                print(f'Pieza {pieza} se movio {ds} espacios.')
            

        if d[0]==d[1]:                          #Si el jugador tuvo 2 dados iguales va denuevo
            i-=1
        i=board.ciclo(i,c)                        #Cambia al jugador

        alguien_gano,ganador=board.gano()       #Verifica si alguien gano

    if q!='q':
        #Imprime quien gano
        input(f"El ganador es {ganador}.\nPresione 'Enter' para cerrar...")


main()