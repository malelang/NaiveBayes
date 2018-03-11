from __future__ import division
def toint(array):
    for i in range(0, len(array)):
        array[i]=int(array[i])
    return array

arch=open("confusionfinal.txt","r")
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
columna0=[]
columna1=[]
columna2=[]
columna3=[]
columna4=[]
for i in range(0,len(matriz)):
    columna0.append(matriz[i][0])
    columna1.append(matriz[i][1])
    columna2.append(matriz[i][2])
    columna3.append(matriz[i][3])
    columna4.append(matriz[i][4])
columnas=[columna0,columna1,columna2,columna3,columna4]
precision=[]
recuerdo=[]
temporal=0
cci=0
sdp=0
sdr=0
for i in range(0,len(matriz)):
    temporal=temporal+matriz[i][i]
    sdp=(matriz[i][i])/sum(columnas[i])
    rdp=(matriz[i][i])/sum(matriz[i])
    precision.append(sdp)
    recuerdo.append(rdp)
cci=temporal/(sum(fila0)+sum(fila1)+sum(fila2)+sum(fila3)+sum(fila4))
medf=[]
for i in range(0,len(precision)):
    cal=(2*precision[i]*recuerdo[i])/(precision[i]+recuerdo[i])
    medf.append(cal)

print("you can go by now.")
"""
print matriz
print columnas
print precision
print recuerdo
print cci
print medf
"""
