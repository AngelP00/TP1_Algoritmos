'''
23. Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una
matriz de [n x n], solo se puede mover de a una casilla a la vez –no se puede mover en diagonal–
y que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0)
y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda
avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo.
'''
from colorama import init, Fore
init(autoreset=True)

def mostrar_laberinto_coloreado(laberinto, camino_para_colorear):
    for i in range(len(laberinto)):
        #print(laberinto[i])
        for n in range(len(laberinto[0])):
            if([i,n] in camino_para_colorear):
                print("'",Fore.GREEN + laberinto[i][n],"'",end="")
            else:
                print("'",laberinto[i][n],"'",end="")
        print()


#devuelve un vector que en espacio contiene un camino para salir del laberinto
def salir_del_laberinto(laberinto, x, y, camino_recorrido=[], caminos_para_salir_del_laberinto = []):
    salida = 'salida'
    camino = 'camino'
    pared = '======'
    if(x>=0 and x<= len(laberinto)-1 and y>=0 and y <= len(laberinto[0])-1):
        if(laberinto[x][y]== salida):
            camino_recorrido.append([x,y])
            print('salida encontrada')
            caminos_para_salir_del_laberinto.append(camino_recorrido+[])
            camino_recorrido.pop()
        elif(laberinto[x][y]!= pared):
            camino_recorrido.append([x,y])
            #mostrar_laberinto_coloreado(laberinto, camino_recorrido)
            #print('')
            laberinto[x][y]= pared
            salir_del_laberinto(laberinto, x+1, y, camino_recorrido, caminos_para_salir_del_laberinto)#abajo
            salir_del_laberinto(laberinto, x-1, y, camino_recorrido, caminos_para_salir_del_laberinto)#arriba
            salir_del_laberinto(laberinto, x, y+1, camino_recorrido, caminos_para_salir_del_laberinto)#derecha
            salir_del_laberinto(laberinto, x, y-1, camino_recorrido, caminos_para_salir_del_laberinto)#izquierda
            #mostrar_laberinto_coloreado(laberinto, camino_recorrido)
            #print('')
            camino_recorrido.pop()
            laberinto[x][y] = camino
    return caminos_para_salir_del_laberinto


laberinto = [['camino', 'camino', 'camino', 'camino', 'camino', 'camino', 'camino'],
            ['======', '======', '======', '======', 'camino', '======', 'camino'],
            ['camino', 'camino', 'camino', '======', 'camino', '======', 'camino'],
            ['camino', '======', 'camino', 'camino', 'camino', 'camino', 'camino'],
            ['camino', '======', '======', '======', '======', '======', '======'],
            ['camino', 'camino', 'camino', 'camino', 'camino', 'camino', 'salida']]

laberinto1 = [['camino', 'camino', 'camino', 'camino'],
            [ '======', 'camino', '======', 'camino'],
            [ '======', 'camino', 'camino', 'camino'],
            [ '======', 'camino', 'salida', 'camino']]

caminos_para_salir_del_laberinto = []
caminos_para_salir_del_laberinto = salir_del_laberinto(laberinto, 0, 0)

if len(caminos_para_salir_del_laberinto) >=1:
    #muestra todos los caminos que se pueden usar para salir del laberinto
    print(Fore.YELLOW+'Hay',len(caminos_para_salir_del_laberinto),Fore.YELLOW+'caminos para salir del laberinto')
    for i in range(len(caminos_para_salir_del_laberinto)):
        print(Fore.YELLOW +'Camino',i+1,':')
        mostrar_laberinto_coloreado(laberinto, caminos_para_salir_del_laberinto[i])
        print()

    #muestra el camino mas corto para salir del laberinto
    pos_camino_mas_corto = 0
    for i in range(1,len(caminos_para_salir_del_laberinto)):
        if len(caminos_para_salir_del_laberinto[i]) < len(caminos_para_salir_del_laberinto[pos_camino_mas_corto]):
            pos_camino_mas_corto = i
    print(Fore.YELLOW +'El camino mas corto es el camino',  pos_camino_mas_corto+1,Fore.YELLOW +':')
    mostrar_laberinto_coloreado(laberinto, caminos_para_salir_del_laberinto[pos_camino_mas_corto])
else:
    print('No se ha encontrada la salida del laberinto')
