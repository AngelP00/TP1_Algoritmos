def numero_romano_a_decimal(numero_romano):
    #print('Numero romano:',numero_romano)
    letra_a_numero = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    #asignar_numero_a_letra
    if(numero_romano[len(numero_romano)-1] in letra_a_numero):
        h = letra_a_numero[numero_romano[len(numero_romano)-1]]
    else:
        h=0

    if len(numero_romano)<=1:
        return h
    #asignar_numero_a_letra
    if(numero_romano[len(numero_romano)-2] in letra_a_numero):
        n = letra_a_numero[numero_romano[len(numero_romano)-2]]
    else:
        n=0

    if(h==0) or (n==0)or repeticiones_no_permitidas(numero_romano):
        return -10000
    if(n<h) and((n==h/5)or(n==h/10)):#n solo puede ser I,X o C
        if(len(numero_romano)>=3):
            if numero_romano[len(numero_romano)-2]==numero_romano[len(numero_romano)-3]:
                return -10000
        if(len(numero_romano)-2>=1):#si quedan uno o mas elementos
            r=numero_romano_a_decimal(numero_romano[0:len(numero_romano)-2])
            if((h-n)<r):
                return (h-n)+r
        else:
            return h-n
    elif(n>h):
        if(len(numero_romano)-2>=1):#si quedan uno o mas elementos
            r=numero_romano_a_decimal(numero_romano[0:len(numero_romano)-2])
            if((n+h)<r)or(r==10)or(r==100)or(r==1000):
                return (n+h)+r
        else:
            return n+h
    elif (n==h)and(n!=5 and n!=50 and n!=500):
        if(len(numero_romano)-2>=1):#si quedan uno o mas elementos
            r=numero_romano_a_decimal(numero_romano[0:len(numero_romano)-2])
            if((n+h)<r)or(r!= 5 and r!=50 and r!=500):
                return (n+h)+r
        else:
            return n+h
    print('no existe')
    return -10000#no existe


def repeticiones_no_permitidas(numero_romano):
    for i in range(0, len(numero_romano)):
        if(len(numero_romano)-i>=4):
            #print('numero romano =',numero_romano)
            if(numero_romano[len(numero_romano)-i-1]==numero_romano[len(numero_romano)-i-2]==numero_romano[len(numero_romano)-i-3]==numero_romano[len(numero_romano)-i-4]):
                return True
    if(numero_romano.count('D')>1) or (numero_romano.count('L')>1) or (numero_romano.count('V')>1):
        return True
    elif(numero_romano.count('I')>=4):
            return True
    return False

entrada='MCCXXI'
num_decimal = numero_romano_a_decimal(entrada.upper())
if num_decimal > 0:
    print('El numero romano',entrada.upper(),'equivale al numero',num_decimal,'en decimal')
else:
    print(entrada.upper(),'No es un numero romano')