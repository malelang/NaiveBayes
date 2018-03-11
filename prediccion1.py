import math
import sys
import shutil
import os
def normdist(miu,sigma,value):
    pi=math.pi
    exponente= ((value-miu)**2)/(2*(sigma**2))
    divisor=sigma*(math.sqrt(2*pi))
    resultado=(math.exp(-exponente))/divisor
    return resultado

def tofloat(array):
    for i in range(0, len(array)):
        array[i]=float(array[i])
    return array

def toint(array):
    for i in range(0, len(array)):
        array[i]=int(array[i])
    return array

def tostr(array):
    for i in range(0, len(array)):
        array[i]=str(array[i])
    return array

arch=open("modelo1.txt","r")
modelo=arch.read()
rol=modelo.splitlines()
pdrugs=rol[0].split(" ")
pbp=rol[1].split(" ")
pch=rol[2].split(" ")
pse=rol[3].split(" ")
dne=rol[4].split(" ")
dnn=rol[5].split(" ")
dnk=rol[6].split(" ")

pdrugs=tofloat(pdrugs)
pbp=tofloat(pbp)
pch=tofloat(pch)
pse=tofloat(pse)
dne=tofloat(dne)
dnn=tofloat(dnn)
dnk=tofloat(dnk)

tablacondicionalbp=[[pbp[0],pbp[1],pbp[2]],[pbp[3],pbp[4],pbp[5]],[pbp[6],pbp[7],pbp[8]],[pbp[9],pbp[10],pbp[11]],[pbp[12],pbp[13],pbp[14]]]
tablacondicionalch=[[pch[0],pch[1],pch[2]],[pch[3],pch[4],pch[5]],[pch[6],pch[7],pch[8]],[pch[9],pch[10],pch[11]],[pch[12],pch[13],pch[14]]]
tablacondicionalse=[[pse[0],pse[1]],[pse[2],pse[3]],[pse[4],pse[5]],[pse[6],pse[7]],[pse[8],pse[9]]]

cp=open("carpetatres.txt", "r")
cont=cp.read()
rol=cont.splitlines()

numero=[]
edad=[]
sexo=[]
bp=[]
colesterol=[]
sodio=[]
potasio=[]
droga=[]
datos=[]
matriz=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range(0,len(matriz)):
    matriz[i]=toint(matriz[i])

for i in range (1,len(rol)):
    a=rol[i].split(" ")
    b=a[0].split("\t")
    numero.append(b[0])
    edad.append(b[1])
    sexo.append(b[2])
    bp.append(b[3])
    colesterol.append(b[4])
    sodio.append(b[5])
    potasio.append(b[6])
    droga.append(b[7])

for i in range (0, len(edad)):
    temporal=[edad[i],sexo[i],bp[i],colesterol[i],sodio[i],potasio[i]]
    datos.append(temporal)


for i in range (0, len(datos)):
    age=datos[i][0]
    sex=datos[i][1]
    bloodpressure=datos[i][2]
    cholesterol=datos[i][3]
    sodium=datos[i][4]
    potasium=datos[i][5]

    logaritmicos=[]
    normales=[]
    condse=[]
    condbp=[]
    condch=[]
    conded=[]
    condna=[]
    distnormaled=[]
    distnormalna=[]
    distnormalk=[]

    if(sex=="F"):
        for k in range(0,len(tablacondicionalse)):
            condse.append(tablacondicionalse[k][0])
    elif(sex=="M"):
        for k in range(0,len(tablacondicionalse)):
            condse.append(tablacondicionalse[k][1])

    if(bloodpressure=="HIGH"):
        for k in range(0,len(tablacondicionalbp)):
            condbp.append(tablacondicionalbp[k][0])
    elif(bloodpressure=="NORMAL"):
        for k in range(0,len(tablacondicionalbp)):
            condbp.append(tablacondicionalbp[k][1])
    elif(bloodpressure=="LOW"):
        for k in range(0,len(tablacondicionalbp)):
            condbp.append(tablacondicionalbp[k][2])

    if(cholesterol=="HIGH"):
        for k in range(0,len(tablacondicionalch)):
            condch.append(tablacondicionalch[k][0])
    elif(cholesterol=="NORMAL"):
        for k in range(0,len(tablacondicionalch)):
            condch.append(tablacondicionalch[k][1])
    elif(cholesterol=="LOW"):
        for k in range(0,len(tablacondicionalch)):
            condch.append(tablacondicionalch[k][2])

    for k in range(0,5):
        distnormaled.append(normdist(dne[k],dne[k+5],float(age)))
        distnormalna.append(normdist(dnn[k],dnn[k+5],float(sodium)))
        distnormalk.append(normdist(dnk[k],dnk[k+5],float(potasium)))

    finalA=[pdrugs[0],condse[0],condbp[0],condch[0],distnormaled[0],distnormalna[0],distnormalk[0]]
    finalB=[pdrugs[1],condse[1],condbp[1],condch[1],distnormaled[1],distnormalna[1],distnormalk[1]]
    finalC=[pdrugs[2],condse[2],condbp[2],condch[2],distnormaled[2],distnormalna[2],distnormalk[2]]
    finalX=[pdrugs[3],condse[3],condbp[3],condch[3],distnormaled[3],distnormalna[3],distnormalk[3]]
    finalY=[pdrugs[4],condse[4],condbp[4],condch[4],distnormaled[4],distnormalna[4],distnormalk[4]]

    vdv=[finalA,finalB,finalC,finalX,finalY]

    for k in range(0,len(vdv)):
        for j in range(0,len(vdv[k])):
            vdv[k][j]=math.log10(vdv[k][j])

    for k in range(0,len(vdv)):
        logaritmicos.append(sum(vdv[k]))

    for k in range(0,len(logaritmicos)):
        normales.append(10**(logaritmicos[k]))

    final=logaritmicos.index(max(logaritmicos))
    comparador=""
    pospredicho=0
    if final==0:
        comparador="drugA"
    elif final==1:
        comparador="drugB"
        pospredicho=1
    elif final==2:
        comparador="drugC"
        pospredicho=2
    elif final==3:
        comparador="drugX"
        pospredicho=3
    elif final==4:
        comoparador="drugY"
        pospredicho=4

    if comparador==droga[i]:
        posreal=pospredicho
    elif droga[i]=="drugA":
        posreal=0
    elif droga[i]=="drugB":
        posreal=1
    elif droga[i]=="drugC":
        posreal=2
    elif droga[i]=="drugX":
        posreal=3
    elif droga[i]=="drugY":
        posreal=4

    matriz[posreal][pospredicho]=matriz[posreal][pospredicho]+1

for i in range(0,len(matriz)):
    matriz[i]=tostr(matriz[i])
with open("confusion1.txt","w") as mat:
    mat.seek(0)
    mat.truncate()
    for i in range(0, len(matriz)):
        mat.write(matriz[i][0]+"\t"+matriz[i][1]+"\t"+matriz[i][2]+"\t"+matriz[i][3]+"\t"+matriz[i][4]+"\n")
    mat.close
print("Done.")
