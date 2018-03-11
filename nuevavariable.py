
from ideapython import *
import math


def normdist(miu,sigma,value):
    pi=math.pi
    exponente= ((value-miu)**2)/(2*(sigma**2))
    divisor=sigma*(math.sqrt(2*pi))
    resultado=(math.exp(-exponente))/divisor
    return resultado


print("Ingrese los siguientes valores para el nuevo registro \n")
age=float(input("Su edad:"))
sodium=float(input("Sus niveles de sodio:"))
potasium=float(input("Sus niveles de potasio:"))
print("\n Ingrese en el siguiente valor alguna de las dos opciones \n")
print("M para sexo masculino, F para sexo femenino")
sex=raw_input("Su genero:")
print("\n Ingrese en los siguientes valores alguna de las tres opciones \n")
print("HIGH para presion sanguinea alta, NORMAL para presion sanguinea normal o LOW para presion sanguinea baja")
bloodpressure=raw_input("Su presion sanguinea:")
print("\n HIGH para colesterol alto, NORMAL para colesterol normal o LOW para colesterol bajo")
cholesterol=raw_input("Su nivel de colesterol:")

totales=[]
nuevos=[]
ssp=sodium/potasium
finalA=[]
finalB=[]
finalC=[]
finalX=[]
finalY=[]

if(sex=="F"):
    finalA.append(vectorcondicionalA[0])
    finalB.append(vectorcondicionalB[0])
    finalC.append(vectorcondicionalC[0])
    finalX.append(vectorcondicionalX[0])
    finalY.append(vectorcondicionalY[0])
elif(sex=="M"):
    finalA.append(vectorcondicionalA[1])
    finalB.append(vectorcondicionalB[1])
    finalC.append(vectorcondicionalC[1])
    finalX.append(vectorcondicionalX[1])
    finalY.append(vectorcondicionalY[1])
else:
    print("Usted ha digitado un valor erroneo")
    raise TypeError

if(bloodpressure=="HIGH"):
    finalA.append(vectorcondicionalA[2])
    finalB.append(vectorcondicionalB[2])
    finalC.append(vectorcondicionalC[2])
    finalX.append(vectorcondicionalX[2])
    finalY.append(vectorcondicionalY[2])
elif(bloodpressure=="NORMAL"):
    finalA.append(vectorcondicionalA[3])
    finalB.append(vectorcondicionalB[3])
    finalC.append(vectorcondicionalC[3])
    finalX.append(vectorcondicionalX[3])
    finalY.append(vectorcondicionalY[3])
elif(bloodpressure=="LOW"):
    finalA.append(vectorcondicionalA[4])
    finalB.append(vectorcondicionalB[4])
    finalC.append(vectorcondicionalC[4])
    finalX.append(vectorcondicionalX[4])
    finalY.append(vectorcondicionalY[4])
else:
    print("Usted ha digitado un valor erroneo")
    raise TypeError

if(cholesterol=="HIGH"):
    finalA.append(vectorcondicionalA[5])
    finalB.append(vectorcondicionalB[5])
    finalC.append(vectorcondicionalC[5])
    finalX.append(vectorcondicionalX[5])
    finalY.append(vectorcondicionalY[5])
elif(cholesterol=="NORMAL"):
    finalA.append(vectorcondicionalA[6])
    finalB.append(vectorcondicionalB[6])
    finalC.append(vectorcondicionalC[6])
    finalX.append(vectorcondicionalX[6])
    finalY.append(vectorcondicionalY[6])
elif(cholesterol=="LOW"):
    finalA.append(vectorcondicionalA[7])
    finalB.append(vectorcondicionalB[7])
    finalC.append(vectorcondicionalC[7])
    finalX.append(vectorcondicionalX[7])
    finalY.append(vectorcondicionalY[7])
else:
    print("Usted ha digitado un valor erroneo")
    raise TypeError

finalA.append(normdist(listmed[0],vstdev[0],age))
finalB.append(normdist(listmed[1],vstdev[1],age))
finalC.append(normdist(listmed[2],vstdev[2],age))
finalX.append(normdist(listmed[3],vstdev[3],age))
finalY.append(normdist(listmed[4],vstdev[4],age))
finalA.append(normdist(listmed[5],vstdev[5],ssp))
finalB.append(normdist(listmed[6],vstdev[6],ssp))
finalC.append(normdist(listmed[7],vstdev[7],ssp))
finalX.append(normdist(listmed[8],vstdev[8],ssp))
finalY.append(normdist(listmed[9],vstdev[9],ssp))

vdv=[finalA,finalB,finalC,finalX,finalY]

for i in range(0,len(vdv)):
    for j in range(0,len(vdv[i])):
        vdv[i][j]=math.log10(vdv[i][j])

for i in range(0,len(vdv)):
    totales.append(sum(vdv[i]))

for i in range(0,len(totales)):
    nuevos.append(10**(totales[i]))

prediccion=max(totales)
porc=max(nuevos)/sum(nuevos)
final=totales.index(max(totales))
with open("registrosProcesados.txt","a") as myfile:
    if final==0:
        print("Usted deberia tomar la droga A")
         myfile.write(str(age)+"--"+str(sodium)+"--"+str(potasium)+"--"+str(sex)+"--"+bloodpressure+"--"+cholesterol+"--DRUGA--"+"\n")
    elif final==1:
        print("Usted deberia tomar la droga B")
        myfile.write(str(age)+"--"+str(sodium)+"--"+str(potasium)+"--"+str(sex)+"--"+bloodpressure+"--"+cholesterol+"--DRUGB--"+"\n")
    elif final==2:
        print("Usted deberia tomar la droga C")
         myfile.write(str(age)+"--"+str(sodium)+"--"+str(potasium)+"--"+str(sex)+"--"+bloodpressure+"--"+cholesterol+"--DRUGC--"+"\n")
    elif final==3:
        print("Usted deberia tomar la droga X")
        myfile.write(str(age)+"--"+str(sodium)+"--"+str(potasium)+"--"+str(sex)+"--"+bloodpressure+"--"+cholesterol+"--DRUGX--"+"\n")
    elif final==4:
        print("Usted deberia tomar la droga Y")
         myfile.write(str(age)+"--"+str(sodium)+"--"+str(potasium)+"--"+str(sex)+"--"+bloodpressure+"--"+cholesterol+"--DRUGY--"+"\n")
    else:
        print("Fuera de rango")
         myfile.write(str(age)+"--"+str(sodium)+"--"+str(potasium)+"--"+str(sex)+"--"+bloodpressure+"--"+cholesterol+"--DRUGOut--"+"\n")
