'''
22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
ayuda de la fuerza” realizar las siguientes actividades:
a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
queden más objetos en la mochila;
b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar
para encontrarlo;
c. Utilizar un vector para representar la mochila.
'''
def usar_la_fuerza(vector, obj_eliminados=0):
    #print(vector)
    if(len(vector)== 0):
        print('La mochila no contiene un sable de luz')
    elif(vector[0]=='sable de luz'):
        print('La mochila contiene un sable de luz, fue necesario sacar',obj_eliminados,'objetos de la mochila')
    else:
        vector.pop(0)
        usar_la_fuerza(vector, obj_eliminados+1)

mochila = ['pistola', 'objeto2', 'objeto4', 'sable de luz' ,'objeto5']
usar_la_fuerza(mochila)
