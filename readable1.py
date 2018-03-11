def toint(array):
    for i in range(0, len(array)):
        array[i]=int(array[i])
    return array

arch=open("confusion1.txt","r")
modelo=arch.read()
rol=modelo.splitlines()
fila0=rol[0].split("\t")
fila1=rol[1].split("\t")
fila2=rol[2].split("\t")
fila3=rol[3].split("\t")
fila4=rol[4].split("\t")
matriz=[fila0,fila1,fila2,fila3,fila4]
for i in range(0,len(matriz)):
    matriz[i]=toint(matriz[i])
