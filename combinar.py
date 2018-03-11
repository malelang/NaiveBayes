import sys
import math
import shutil
import os
#p =  int(sys.argv[1])

def modelos(nombre,nro):
    arch=open(nombre, "r")
    cont=arch.read()
    rol=cont.splitlines()
    numero=[]
    edad=[]
    sexo=[]
    bp=[]
    colesterol=[]
    sodio=[]
    potasio=[]
    droga= []
    nak=[]
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
    contA=contB=contC=contX=contY=ps=stdv=0
    longitud=len(droga)
    for i in range (0,len(droga)):
        if droga[i]=="drugA":
            contA=contA+1
        elif droga[i]=="drugB":
            contB=contB+1
        elif droga[i]=="drugC":
            contC=contC+1
        elif droga[i]=="drugX":
            contX=contX+1
        else:
            contY=contY+1
    pa=float(contA)/len(droga)
    pb=float(contB)/len(droga)
    pc=float(contC)/len(droga)
    px=float(contX)/len(droga)
    py=float(contY)/len(droga)
    pdrugs=[pa,pb,pc,px,py]
    osfa=osma=obha=obna=obla=ocha=ocna=ocla=0
    osfb=osmb=obhb=obnb=oblb=ochb=ocnb=oclb=0
    osfc=osmc=obhc=obnc=oblc=ochc=ocnc=oclc=0
    osfx=osmx=obhx=obnx=oblx=ochx=ocnx=oclx=0
    osfy=osmy=obhy=obny=obly=ochy=ocny=ocly=0
    veda=[]
    vedb=[]
    vedc=[]
    vedx=[]
    vedy=[]
    vnaa=[]
    vnab=[]
    vnac=[]
    vnax=[]
    vnay=[]
    vka=[]
    vkb=[]
    vkc=[]
    vkx=[]
    vky=[]
    pred=[]
    prna=[]
    prk=[]
    for i in range (0,len(edad)):
        pred.append(edad[i])
        prna.append(sodio[i])
        prk.append(potasio[i])
    pred.sort()
    prna.sort()
    prk.sort()
    sumprec=distict=precisionedad=precisionna=precisionk=0

    for i in range(0, (len(pred)-1)):
        sumprec=sumprec+abs(float(pred[i+1])-float(pred[i]))
        if (abs(float(pred[i+1])-float(pred[i]))!=0):
            distict=distict+1
    precisionedad=sumprec/distict
    distict=sumprec=0
    for i in range(0, (len(prna)-1)):
        sumprec=sumprec+abs(float(prna[i+1])-float(prna[i]))
        if (abs(float(prna[i+1])-float(prna[i]))!=0):
            distict=distict+1
    precisionna=sumprec/distict
    distict=sumprec=0

    for i in range(0, (len(prk)-1)):
        sumprec=sumprec+abs(float(prk[i+1])-float(prk[i]))
        if (abs(float(prk[i+1])-float(prk[i]))!=0):
            distict=distict+1
    precisionk=sumprec/distict
    for i in range(0, len(edad)):
        edad[i]=round(float(edad[i])/precisionedad)*precisionedad
        sodio[i]=round(float(sodio[i])/precisionna)*precisionna
        potasio[i]=round(float(potasio[i])/precisionk)*precisionk
    for i in range (0, len(droga)):
        if droga[i]=="drugA":
            veda.append(float(edad[i]))
            vnaa.append(float(sodio[i]))
            vka.append(float(potasio[i]))
            ppa=condicionaldiscreta(sexo,bp,colesterol,i)
            osfa=osfa+ppa[0]
            osma=osma+ppa[1]
            obha=obha+ppa[2]
            obna=obna+ppa[3]
            obla=obla+ppa[4]
            ocha=ocha+ppa[5]
            ocna=ocna+ppa[6]
            ocla=ocla+ppa[7]
        elif droga[i]=="drugB":
            vedb.append(float(edad[i]))
            vnab.append(float(sodio[i]))
            vkb.append(float(potasio[i]))
            ppb=condicionaldiscreta(sexo,bp,colesterol,i)
            osfb=osfb+ppb[0]
            osmb=osmb+ppb[1]
            obhb=obhb+ppb[2]
            obnb=obnb+ppb[3]
            oblb=oblb+ppb[4]
            ochb=ochb+ppb[5]
            ocnb=ocnb+ppb[6]
            oclb=oclb+ppb[7]
        elif droga[i]=="drugC":
            vedc.append(float(edad[i]))
            vnac.append(float(sodio[i]))
            vkc.append(float(potasio[i]))
            ppc=condicionaldiscreta(sexo,bp,colesterol,i)
            osfc=osfc+ppc[0]
            osmc=osmc+ppc[1]
            obhc=obhc+ppc[2]
            obnc=obnc+ppc[3]
            oblc=oblc+ppc[4]
            ochc=ochc+ppc[5]
            ocnc=ocnc+ppc[6]
            oclc=oclc+ppc[7]
        elif droga[i]=="drugX":
            vedx.append(float(edad[i]))
            vnax.append(float(sodio[i]))
            vkx.append(float(potasio[i]))
            ppx=condicionaldiscreta(sexo,bp,colesterol,i)
            osfx=osfx+ppx[0]
            osmx=osmx+ppx[1]
            obhx=obhx+ppx[2]
            obnx=obnx+ppx[3]
            oblx=oblx+ppx[4]
            ochx=ochx+ppx[5]
            ocnx=ocnx+ppx[6]
            oclx=oclx+ppx[7]
        elif droga[i]=="drugY":
            vedy.append(float(edad[i]))
            vnay.append(float(sodio[i]))
            vky.append(float(potasio[i]))
            ppy=condicionaldiscreta(sexo,bp,colesterol,i)
            osfy=osfy+ppy[0]
            osmy=osmy+ppy[1]
            obhy=obhy+ppy[2]
            obny=obny+ppy[3]
            obly=obly+ppy[4]
            ochy=ochy+ppy[5]
            ocny=ocny+ppy[6]
            ocly=ocly+ppy[7]

    #CALCULAMOS LA PROBABILIDAD PARA CADA SITUACION CONDICIONAL SUAVIZANDO CON LAPLACE
    probsfda=float(osfa+1)/(contA+2)
    probsmda=float(osma+1)/(contA+2)
    probsfdb=float(osfb+1)/(contB+2)
    probsmdb=float(osmb+1)/(contB+2)
    probsfdc=float(osfc+1)/(contC+2)
    probsmdc=float(osmc+1)/(contC+2)
    probsfdx=float(osfx+1)/(contX+2)
    probsmdx=float(osmx+1)/(contX+2)
    probsfdy=float(osfy+1)/(contY+2)
    probsmdy=float(osmy+1)/(contY+2)
    probbhda=float(obha+1)/(contA+3)
    probbnda=float(obna+1)/(contA+3)
    probblda=float(obla+1)/(contA+3)
    probbhdb=float(obhb+1)/(contB+3)
    probbndb=float(obnb+1)/(contB+3)
    probbldb=float(oblb+1)/(contB+3)
    probbhdc=float(obhc+1)/(contC+3)
    probbndc=float(obnc+1)/(contC+3)
    probbldc=float(oblc+1)/(contC+3)
    probbhdx=float(obhx+1)/(contX+3)
    probbndx=float(obnx+1)/(contX+3)
    probbldx=float(oblx+1)/(contX+3)
    probbhdy=float(obhy+1)/(contY+3)
    probbndy=float(obny+1)/(contY+3)
    probbldy=float(obly+1)/(contY+3)
    probchda=float(ocha+1)/(contA+3)
    probcnda=float(ocna+1)/(contA+3)
    probclda=float(ocla+1)/(contA+3)
    probchdb=float(ochb+1)/(contB+3)
    probcndb=float(ocnb+1)/(contB+3)
    probcldb=float(oclb+1)/(contB+3)
    probchdc=float(ochc+1)/(contC+3)
    probcndc=float(ocnc+1)/(contC+3)
    probcldc=float(oclc+1)/(contC+3)
    probchdx=float(ochx+1)/(contX+3)
    probcndx=float(ocnx+1)/(contX+3)
    probcldx=float(oclx+1)/(contX+3)
    probchdy=float(ochy+1)/(contY+3)
    probcndy=float(ocny+1)/(contY+3)
    probcldy=float(ocly+1)/(contY+3)
    mediaedda= float(sum(veda))/len(veda)
    mediaeddb= float(sum(vedb))/len(vedb)
    mediaeddc= float(sum(vedc))/len(vedc)
    mediaeddx= float(sum(vedx))/len(vedx)
    mediaeddy= float(sum(vedy))/len(vedy)
    medianada= float(sum(vnaa))/len(vnaa)
    medianadb= float(sum(vnab))/len(vnab)
    medianadc= float(sum(vnac))/len(vnac)
    medianadx= float(sum(vnax))/len(vnax)
    medianady= float(sum(vnay))/len(vnay)
    mediakda= float(sum(vka))/len(vka)
    mediakdb= float(sum(vkb))/len(vkb)
    mediakdc= float(sum(vkc))/len(vkc)
    mediakdx= float(sum(vkx))/len(vkx)
    mediakdy= float(sum(vky))/len(vky)
    vstdev=[]
    listprob=[veda,vedb,vedc,vedx,vedy,vnaa,vnab,vnac,vnax,vnay,vka,vkb,vkc,vkx,vky]
    listmed=[mediaedda,mediaeddb,mediaeddc,mediaeddx,mediaeddy,medianada,medianadb,medianadc,medianadx,medianady,mediakda,mediakdb,mediakdc,mediakdx,mediakdy]
    for i in range(0,len(listprob)):
        for j in range(0,len(listprob[i])):
            ps=ps+((listprob[i][j]-listmed[i])**2)
        stdv=math.sqrt(ps/len(listprob[i]))
        vstdev.append(stdv)
        ps=0
    print nro
    if (nro==1):
        with open("modelo1.txt","w") as modelo:
            modelo.write(str(pa)+" "+str(pb)+" "+str(pc)+" "+str(px)+" "+str(py)+"\n")
            modelo.close()
        modelo=open("modelo1.txt","a")
        modelo.write(str(probbhda)+" "+str(probbnda)+" "+str(probblda)+" "+str(probbhdb)+" "+str(probbndb)+" "+str(probbldb)+" "+str(probbhdc)+" "+str(probbndc)+" "+str(probbldc)+" "+str(probbhdx)+" "+str(probbndx)+" "+str(probbldx)+" "+str(probbhdy)+" "+str(probbndy)+" "+str(probbldy)+"\n")
        modelo.write(str(probchda)+" "+str(probcnda)+" "+str(probclda)+" "+str(probchdb)+" "+str(probcndb)+" "+str(probcldb)+" "+str(probchdc)+" "+str(probcndc)+" "+str(probcldc)+" "+str(probchdx)+" "+str(probcndx)+" "+str(probcldx)+" "+str(probchdy)+" "+str(probcndy)+" "+str(probcldy)+"\n")
        modelo.write(str(probsfda)+" "+str(probsmda)+" "+str(probsfdb)+" "+str(probsmdb)+" "+str(probsfdc)+" "+str(probsmdc)+" "+str(probsfdx)+" "+str(probsmdx)+" "+str(probsfdy)+" "+str(probsmdy)+"\n")
        modelo.write(str(mediaedda)+" "+str(mediaeddb)+" "+str(mediaeddc)+" "+str(mediaeddx)+" "+str(mediaeddy)+" "+str(vstdev[0])+" "+str(vstdev[1])+" "+str(vstdev[2])+" "+str(vstdev[3])+" "+str(vstdev[4])+"\n")
        modelo.write(str(medianada)+" "+str(medianadb)+" "+str(medianadc)+" "+str(medianadx)+" "+str(medianady)+" "+str(vstdev[5])+" "+str(vstdev[6])+" "+str(vstdev[7])+" "+str(vstdev[8])+" "+str(vstdev[9])+"\n")
        modelo.write(str(mediakda)+" "+str(mediakdb)+" "+str(mediakdc)+" "+str(mediakdx)+" "+str(mediakdy)+" "+str(vstdev[10])+" "+str(vstdev[11])+" "+str(vstdev[12])+" "+str(vstdev[13])+" "+str(vstdev[14])+"\n")
        modelo.close()
    elif (nro==2):
        with open("modelo2.txt","w") as modelo:
            modelo.write(str(pa)+" "+str(pb)+" "+str(pc)+" "+str(px)+" "+str(py)+"\n")
            modelo.close()
        modelo=open("modelo2.txt","a")
        modelo.write(str(probbhda)+" "+str(probbnda)+" "+str(probblda)+" "+str(probbhdb)+" "+str(probbndb)+" "+str(probbldb)+" "+str(probbhdc)+" "+str(probbndc)+" "+str(probbldc)+" "+str(probbhdx)+" "+str(probbndx)+" "+str(probbldx)+" "+str(probbhdy)+" "+str(probbndy)+" "+str(probbldy)+"\n")
        modelo.write(str(probchda)+" "+str(probcnda)+" "+str(probclda)+" "+str(probchdb)+" "+str(probcndb)+" "+str(probcldb)+" "+str(probchdc)+" "+str(probcndc)+" "+str(probcldc)+" "+str(probchdx)+" "+str(probcndx)+" "+str(probcldx)+" "+str(probchdy)+" "+str(probcndy)+" "+str(probcldy)+"\n")
        modelo.write(str(probsfda)+" "+str(probsmda)+" "+str(probsfdb)+" "+str(probsmdb)+" "+str(probsfdc)+" "+str(probsmdc)+" "+str(probsfdx)+" "+str(probsmdx)+" "+str(probsfdy)+" "+str(probsmdy)+"\n")
        modelo.write(str(mediaedda)+" "+str(mediaeddb)+" "+str(mediaeddc)+" "+str(mediaeddx)+" "+str(mediaeddy)+" "+str(vstdev[0])+" "+str(vstdev[1])+" "+str(vstdev[2])+" "+str(vstdev[3])+" "+str(vstdev[4])+"\n")
        modelo.write(str(medianada)+" "+str(medianadb)+" "+str(medianadc)+" "+str(medianadx)+" "+str(medianady)+" "+str(vstdev[5])+" "+str(vstdev[6])+" "+str(vstdev[7])+" "+str(vstdev[8])+" "+str(vstdev[9])+"\n")
        modelo.write(str(mediakda)+" "+str(mediakdb)+" "+str(mediakdc)+" "+str(mediakdx)+" "+str(mediakdy)+" "+str(vstdev[10])+" "+str(vstdev[11])+" "+str(vstdev[12])+" "+str(vstdev[13])+" "+str(vstdev[14])+"\n")
        modelo.close()
    elif(nro==3):
        with open("modelo3.txt","w") as modelo:
            modelo.write(str(pa)+" "+str(pb)+" "+str(pc)+" "+str(px)+" "+str(py)+"\n")
            modelo.close()
        modelo=open("modelo3.txt","a")
        modelo.write(str(probbhda)+" "+str(probbnda)+" "+str(probblda)+" "+str(probbhdb)+" "+str(probbndb)+" "+str(probbldb)+" "+str(probbhdc)+" "+str(probbndc)+" "+str(probbldc)+" "+str(probbhdx)+" "+str(probbndx)+" "+str(probbldx)+" "+str(probbhdy)+" "+str(probbndy)+" "+str(probbldy)+"\n")
        modelo.write(str(probchda)+" "+str(probcnda)+" "+str(probclda)+" "+str(probchdb)+" "+str(probcndb)+" "+str(probcldb)+" "+str(probchdc)+" "+str(probcndc)+" "+str(probcldc)+" "+str(probchdx)+" "+str(probcndx)+" "+str(probcldx)+" "+str(probchdy)+" "+str(probcndy)+" "+str(probcldy)+"\n")
        modelo.write(str(probsfda)+" "+str(probsmda)+" "+str(probsfdb)+" "+str(probsmdb)+" "+str(probsfdc)+" "+str(probsmdc)+" "+str(probsfdx)+" "+str(probsmdx)+" "+str(probsfdy)+" "+str(probsmdy)+"\n")
        modelo.write(str(mediaedda)+" "+str(mediaeddb)+" "+str(mediaeddc)+" "+str(mediaeddx)+" "+str(mediaeddy)+" "+str(vstdev[0])+" "+str(vstdev[1])+" "+str(vstdev[2])+" "+str(vstdev[3])+" "+str(vstdev[4])+"\n")
        modelo.write(str(medianada)+" "+str(medianadb)+" "+str(medianadc)+" "+str(medianadx)+" "+str(medianady)+" "+str(vstdev[5])+" "+str(vstdev[6])+" "+str(vstdev[7])+" "+str(vstdev[8])+" "+str(vstdev[9])+"\n")
        modelo.write(str(mediakda)+" "+str(mediakdb)+" "+str(mediakdc)+" "+str(mediakdx)+" "+str(mediakdy)+" "+str(vstdev[10])+" "+str(vstdev[11])+" "+str(vstdev[12])+" "+str(vstdev[13])+" "+str(vstdev[14])+"\n")
        modelo.close()
    elif(nro==4):
        with open("modelo4.txt","w") as modelo:
            modelo.write(str(pa)+" "+str(pb)+" "+str(pc)+" "+str(px)+" "+str(py)+"\n")
            modelo.close()
        modelo=open("modelo4.txt","a")
        modelo.write(str(probbhda)+" "+str(probbnda)+" "+str(probblda)+" "+str(probbhdb)+" "+str(probbndb)+" "+str(probbldb)+" "+str(probbhdc)+" "+str(probbndc)+" "+str(probbldc)+" "+str(probbhdx)+" "+str(probbndx)+" "+str(probbldx)+" "+str(probbhdy)+" "+str(probbndy)+" "+str(probbldy)+"\n")
        modelo.write(str(probchda)+" "+str(probcnda)+" "+str(probclda)+" "+str(probchdb)+" "+str(probcndb)+" "+str(probcldb)+" "+str(probchdc)+" "+str(probcndc)+" "+str(probcldc)+" "+str(probchdx)+" "+str(probcndx)+" "+str(probcldx)+" "+str(probchdy)+" "+str(probcndy)+" "+str(probcldy)+"\n")
        modelo.write(str(probsfda)+" "+str(probsmda)+" "+str(probsfdb)+" "+str(probsmdb)+" "+str(probsfdc)+" "+str(probsmdc)+" "+str(probsfdx)+" "+str(probsmdx)+" "+str(probsfdy)+" "+str(probsmdy)+"\n")
        modelo.write(str(mediaedda)+" "+str(mediaeddb)+" "+str(mediaeddc)+" "+str(mediaeddx)+" "+str(mediaeddy)+" "+str(vstdev[0])+" "+str(vstdev[1])+" "+str(vstdev[2])+" "+str(vstdev[3])+" "+str(vstdev[4])+"\n")
        modelo.write(str(medianada)+" "+str(medianadb)+" "+str(medianadc)+" "+str(medianadx)+" "+str(medianady)+" "+str(vstdev[5])+" "+str(vstdev[6])+" "+str(vstdev[7])+" "+str(vstdev[8])+" "+str(vstdev[9])+"\n")
        modelo.write(str(mediakda)+" "+str(mediakdb)+" "+str(mediakdc)+" "+str(mediakdx)+" "+str(mediakdy)+" "+str(vstdev[10])+" "+str(vstdev[11])+" "+str(vstdev[12])+" "+str(vstdev[13])+" "+str(vstdev[14])+"\n")
        modelo.close()
    elif(nro==5):
        with open("modelo5.txt","w") as modelo:
            modelo.write(str(pa)+" "+str(pb)+" "+str(pc)+" "+str(px)+" "+str(py)+"\n")
            modelo.close()
        modelo=open("modelo5.txt","a")
        modelo.write(str(probbhda)+" "+str(probbnda)+" "+str(probblda)+" "+str(probbhdb)+" "+str(probbndb)+" "+str(probbldb)+" "+str(probbhdc)+" "+str(probbndc)+" "+str(probbldc)+" "+str(probbhdx)+" "+str(probbndx)+" "+str(probbldx)+" "+str(probbhdy)+" "+str(probbndy)+" "+str(probbldy)+"\n")
        modelo.write(str(probchda)+" "+str(probcnda)+" "+str(probclda)+" "+str(probchdb)+" "+str(probcndb)+" "+str(probcldb)+" "+str(probchdc)+" "+str(probcndc)+" "+str(probcldc)+" "+str(probchdx)+" "+str(probcndx)+" "+str(probcldx)+" "+str(probchdy)+" "+str(probcndy)+" "+str(probcldy)+"\n")
        modelo.write(str(probsfda)+" "+str(probsmda)+" "+str(probsfdb)+" "+str(probsmdb)+" "+str(probsfdc)+" "+str(probsmdc)+" "+str(probsfdx)+" "+str(probsmdx)+" "+str(probsfdy)+" "+str(probsmdy)+"\n")
        modelo.write(str(mediaedda)+" "+str(mediaeddb)+" "+str(mediaeddc)+" "+str(mediaeddx)+" "+str(mediaeddy)+" "+str(vstdev[0])+" "+str(vstdev[1])+" "+str(vstdev[2])+" "+str(vstdev[3])+" "+str(vstdev[4])+"\n")
        modelo.write(str(medianada)+" "+str(medianadb)+" "+str(medianadc)+" "+str(medianadx)+" "+str(medianady)+" "+str(vstdev[5])+" "+str(vstdev[6])+" "+str(vstdev[7])+" "+str(vstdev[8])+" "+str(vstdev[9])+"\n")
        modelo.write(str(mediakda)+" "+str(mediakdb)+" "+str(mediakdc)+" "+str(mediakdx)+" "+str(mediakdy)+" "+str(vstdev[10])+" "+str(vstdev[11])+" "+str(vstdev[12])+" "+str(vstdev[13])+" "+str(vstdev[14])+"\n")
        modelo.close()
    elif(nro==6):
        with open("modelo6.txt","w") as modelo:
            modelo.write(str(pa)+" "+str(pb)+" "+str(pc)+" "+str(px)+" "+str(py)+"\n")
            modelo.close()
        modelo=open("modelo6.txt","a")
        modelo.write(str(probbhda)+" "+str(probbnda)+" "+str(probblda)+" "+str(probbhdb)+" "+str(probbndb)+" "+str(probbldb)+" "+str(probbhdc)+" "+str(probbndc)+" "+str(probbldc)+" "+str(probbhdx)+" "+str(probbndx)+" "+str(probbldx)+" "+str(probbhdy)+" "+str(probbndy)+" "+str(probbldy)+"\n")
        modelo.write(str(probchda)+" "+str(probcnda)+" "+str(probclda)+" "+str(probchdb)+" "+str(probcndb)+" "+str(probcldb)+" "+str(probchdc)+" "+str(probcndc)+" "+str(probcldc)+" "+str(probchdx)+" "+str(probcndx)+" "+str(probcldx)+" "+str(probchdy)+" "+str(probcndy)+" "+str(probcldy)+"\n")
        modelo.write(str(probsfda)+" "+str(probsmda)+" "+str(probsfdb)+" "+str(probsmdb)+" "+str(probsfdc)+" "+str(probsmdc)+" "+str(probsfdx)+" "+str(probsmdx)+" "+str(probsfdy)+" "+str(probsmdy)+"\n")
        modelo.write(str(mediaedda)+" "+str(mediaeddb)+" "+str(mediaeddc)+" "+str(mediaeddx)+" "+str(mediaeddy)+" "+str(vstdev[0])+" "+str(vstdev[1])+" "+str(vstdev[2])+" "+str(vstdev[3])+" "+str(vstdev[4])+"\n")
        modelo.write(str(medianada)+" "+str(medianadb)+" "+str(medianadc)+" "+str(medianadx)+" "+str(medianady)+" "+str(vstdev[5])+" "+str(vstdev[6])+" "+str(vstdev[7])+" "+str(vstdev[8])+" "+str(vstdev[9])+"\n")
        modelo.write(str(mediakda)+" "+str(mediakdb)+" "+str(mediakdc)+" "+str(mediakdx)+" "+str(mediakdy)+" "+str(vstdev[10])+" "+str(vstdev[11])+" "+str(vstdev[12])+" "+str(vstdev[13])+" "+str(vstdev[14])+"\n")
        modelo.close()
    elif(nro==7):
        with open("modelo7.txt","w") as modelo:
            modelo.write(str(pa)+" "+str(pb)+" "+str(pc)+" "+str(px)+" "+str(py)+"\n")
            modelo.close()
        modelo=open("modelo7.txt","a")
        modelo.write(str(probbhda)+" "+str(probbnda)+" "+str(probblda)+" "+str(probbhdb)+" "+str(probbndb)+" "+str(probbldb)+" "+str(probbhdc)+" "+str(probbndc)+" "+str(probbldc)+" "+str(probbhdx)+" "+str(probbndx)+" "+str(probbldx)+" "+str(probbhdy)+" "+str(probbndy)+" "+str(probbldy)+"\n")
        modelo.write(str(probchda)+" "+str(probcnda)+" "+str(probclda)+" "+str(probchdb)+" "+str(probcndb)+" "+str(probcldb)+" "+str(probchdc)+" "+str(probcndc)+" "+str(probcldc)+" "+str(probchdx)+" "+str(probcndx)+" "+str(probcldx)+" "+str(probchdy)+" "+str(probcndy)+" "+str(probcldy)+"\n")
        modelo.write(str(probsfda)+" "+str(probsmda)+" "+str(probsfdb)+" "+str(probsmdb)+" "+str(probsfdc)+" "+str(probsmdc)+" "+str(probsfdx)+" "+str(probsmdx)+" "+str(probsfdy)+" "+str(probsmdy)+"\n")
        modelo.write(str(mediaedda)+" "+str(mediaeddb)+" "+str(mediaeddc)+" "+str(mediaeddx)+" "+str(mediaeddy)+" "+str(vstdev[0])+" "+str(vstdev[1])+" "+str(vstdev[2])+" "+str(vstdev[3])+" "+str(vstdev[4])+"\n")
        modelo.write(str(medianada)+" "+str(medianadb)+" "+str(medianadc)+" "+str(medianadx)+" "+str(medianady)+" "+str(vstdev[5])+" "+str(vstdev[6])+" "+str(vstdev[7])+" "+str(vstdev[8])+" "+str(vstdev[9])+"\n")
        modelo.write(str(mediakda)+" "+str(mediakdb)+" "+str(mediakdc)+" "+str(mediakdx)+" "+str(mediakdy)+" "+str(vstdev[10])+" "+str(vstdev[11])+" "+str(vstdev[12])+" "+str(vstdev[13])+" "+str(vstdev[14])+"\n")
        modelo.close()
    elif(nro==8):
        with open("modelo8.txt","w") as modelo:
            modelo.write(str(pa)+" "+str(pb)+" "+str(pc)+" "+str(px)+" "+str(py)+"\n")
            modelo.close()
        modelo=open("modelo8.txt","a")
        modelo.write(str(probbhda)+" "+str(probbnda)+" "+str(probblda)+" "+str(probbhdb)+" "+str(probbndb)+" "+str(probbldb)+" "+str(probbhdc)+" "+str(probbndc)+" "+str(probbldc)+" "+str(probbhdx)+" "+str(probbndx)+" "+str(probbldx)+" "+str(probbhdy)+" "+str(probbndy)+" "+str(probbldy)+"\n")
        modelo.write(str(probchda)+" "+str(probcnda)+" "+str(probclda)+" "+str(probchdb)+" "+str(probcndb)+" "+str(probcldb)+" "+str(probchdc)+" "+str(probcndc)+" "+str(probcldc)+" "+str(probchdx)+" "+str(probcndx)+" "+str(probcldx)+" "+str(probchdy)+" "+str(probcndy)+" "+str(probcldy)+"\n")
        modelo.write(str(probsfda)+" "+str(probsmda)+" "+str(probsfdb)+" "+str(probsmdb)+" "+str(probsfdc)+" "+str(probsmdc)+" "+str(probsfdx)+" "+str(probsmdx)+" "+str(probsfdy)+" "+str(probsmdy)+"\n")
        modelo.write(str(mediaedda)+" "+str(mediaeddb)+" "+str(mediaeddc)+" "+str(mediaeddx)+" "+str(mediaeddy)+" "+str(vstdev[0])+" "+str(vstdev[1])+" "+str(vstdev[2])+" "+str(vstdev[3])+" "+str(vstdev[4])+"\n")
        modelo.write(str(medianada)+" "+str(medianadb)+" "+str(medianadc)+" "+str(medianadx)+" "+str(medianady)+" "+str(vstdev[5])+" "+str(vstdev[6])+" "+str(vstdev[7])+" "+str(vstdev[8])+" "+str(vstdev[9])+"\n")
        modelo.write(str(mediakda)+" "+str(mediakdb)+" "+str(mediakdc)+" "+str(mediakdx)+" "+str(mediakdy)+" "+str(vstdev[10])+" "+str(vstdev[11])+" "+str(vstdev[12])+" "+str(vstdev[13])+" "+str(vstdev[14])+"\n")
        modelo.close()
    elif(nro==9):
        with open("modelo9.txt","w") as modelo:
            modelo.write(str(pa)+" "+str(pb)+" "+str(pc)+" "+str(px)+" "+str(py)+"\n")
            modelo.close()
        modelo=open("modelo9.txt","a")
        modelo.write(str(probbhda)+" "+str(probbnda)+" "+str(probblda)+" "+str(probbhdb)+" "+str(probbndb)+" "+str(probbldb)+" "+str(probbhdc)+" "+str(probbndc)+" "+str(probbldc)+" "+str(probbhdx)+" "+str(probbndx)+" "+str(probbldx)+" "+str(probbhdy)+" "+str(probbndy)+" "+str(probbldy)+"\n")
        modelo.write(str(probchda)+" "+str(probcnda)+" "+str(probclda)+" "+str(probchdb)+" "+str(probcndb)+" "+str(probcldb)+" "+str(probchdc)+" "+str(probcndc)+" "+str(probcldc)+" "+str(probchdx)+" "+str(probcndx)+" "+str(probcldx)+" "+str(probchdy)+" "+str(probcndy)+" "+str(probcldy)+"\n")
        modelo.write(str(probsfda)+" "+str(probsmda)+" "+str(probsfdb)+" "+str(probsmdb)+" "+str(probsfdc)+" "+str(probsmdc)+" "+str(probsfdx)+" "+str(probsmdx)+" "+str(probsfdy)+" "+str(probsmdy)+"\n")
        modelo.write(str(mediaedda)+" "+str(mediaeddb)+" "+str(mediaeddc)+" "+str(mediaeddx)+" "+str(mediaeddy)+" "+str(vstdev[0])+" "+str(vstdev[1])+" "+str(vstdev[2])+" "+str(vstdev[3])+" "+str(vstdev[4])+"\n")
        modelo.write(str(medianada)+" "+str(medianadb)+" "+str(medianadc)+" "+str(medianadx)+" "+str(medianady)+" "+str(vstdev[5])+" "+str(vstdev[6])+" "+str(vstdev[7])+" "+str(vstdev[8])+" "+str(vstdev[9])+"\n")
        modelo.write(str(mediakda)+" "+str(mediakdb)+" "+str(mediakdc)+" "+str(mediakdx)+" "+str(mediakdy)+" "+str(vstdev[10])+" "+str(vstdev[11])+" "+str(vstdev[12])+" "+str(vstdev[13])+" "+str(vstdev[14])+"\n")
        modelo.close()
    elif(nro==10):
        with open("modelo10.txt","w") as modelo:
            modelo.write(str(pa)+" "+str(pb)+" "+str(pc)+" "+str(px)+" "+str(py)+"\n")
            modelo.close()
        modelo=open("modelo10.txt","a")
        modelo.write(str(probbhda)+" "+str(probbnda)+" "+str(probblda)+" "+str(probbhdb)+" "+str(probbndb)+" "+str(probbldb)+" "+str(probbhdc)+" "+str(probbndc)+" "+str(probbldc)+" "+str(probbhdx)+" "+str(probbndx)+" "+str(probbldx)+" "+str(probbhdy)+" "+str(probbndy)+" "+str(probbldy)+"\n")
        modelo.write(str(probchda)+" "+str(probcnda)+" "+str(probclda)+" "+str(probchdb)+" "+str(probcndb)+" "+str(probcldb)+" "+str(probchdc)+" "+str(probcndc)+" "+str(probcldc)+" "+str(probchdx)+" "+str(probcndx)+" "+str(probcldx)+" "+str(probchdy)+" "+str(probcndy)+" "+str(probcldy)+"\n")
        modelo.write(str(probsfda)+" "+str(probsmda)+" "+str(probsfdb)+" "+str(probsmdb)+" "+str(probsfdc)+" "+str(probsmdc)+" "+str(probsfdx)+" "+str(probsmdx)+" "+str(probsfdy)+" "+str(probsmdy)+"\n")
        modelo.write(str(mediaedda)+" "+str(mediaeddb)+" "+str(mediaeddc)+" "+str(mediaeddx)+" "+str(mediaeddy)+" "+str(vstdev[0])+" "+str(vstdev[1])+" "+str(vstdev[2])+" "+str(vstdev[3])+" "+str(vstdev[4])+"\n")
        modelo.write(str(medianada)+" "+str(medianadb)+" "+str(medianadc)+" "+str(medianadx)+" "+str(medianady)+" "+str(vstdev[5])+" "+str(vstdev[6])+" "+str(vstdev[7])+" "+str(vstdev[8])+" "+str(vstdev[9])+"\n")
        modelo.write(str(mediakda)+" "+str(mediakdb)+" "+str(mediakdc)+" "+str(mediakdx)+" "+str(mediakdy)+" "+str(vstdev[10])+" "+str(vstdev[11])+" "+str(vstdev[12])+" "+str(vstdev[13])+" "+str(vstdev[14])+"\n")
        modelo.close()
    arch.close()

def condicionaldiscreta(se,bl,ch,index):
    contsef=contsem=contblh=contbln=contbll=contchh=contchn=contchl=0
    if se[index]=="F":
        contsef=contsef+1
    elif se[index]=="M":
        contsem=contsem+1

    if bl[index]=="HIGH":
        contblh=contblh+1
    elif bl[index]=="NORMAL":
        contbln=contbln+1
    elif bl[index]=="LOW":
        contbll=contbll+1

    if ch[index]=="HIGH":
        contchh=contchh+1
    elif ch[index]=="NORMAL":
        contchn=contchn+1
    elif ch[index]=="LOW":
        contchl=contchl+1

    vcd=[contsef,contsem, contblh, contbln, contbll, contchh, contchn, contchl]
    return vcd

def sort(p,a,vdf):
    cont=0
    j=0
    for i in range(0,len(vdf)):
        with open(vdf[i],"w") as myfile:
            myfile.seek(0)
            myfile.truncate()
            myfile.write("EDAD  --  SEXO  --  BP  --  CHOLESTEROL --  \n")
            myfile.close()
    print len(a)
    while(cont<len(a)):
        if(len(a)%p!=0):
            m=len(a)-(len(a)%p)
            for k in range(m+1,len(a)):
                nuevofolder=open(vdf[j],"a")
                nuevofolder.write(str(a[k][0])+"\t"+str(a[k][1])+"\t"+str(a[k][2])+"\t"+str(a[k][3])+"\t"+str(a[k][4])+"\t"+str(a[k][5])+"\t"+str(a[k][6])+"\t"+str(a[k][7])+"\n")
                j=j+1
            for k in range(m,200):
                a.pop()
            j=0
        elif(p==2):
            if (j==2):
                j=0
            nuevofolder=open(vdf[j],"a")
            nuevofolder.write(str(a[cont][0])+"\t"+str(a[cont][1])+"\t"+str(a[cont][2])+"\t"+str(a[cont][3])+"\t"+str(a[cont][4])+"\t"+str(a[cont][5])+"\t"+str(a[cont][6])+"\t"+str(a[cont][7])+"\n")
            print("escribi este valor: "+str(cont))
            cont=cont+1
            j=j+1
        elif(p==3):
            if (j==3):
                j=0
            nuevofolder=open(vdf[j],"a")
            nuevofolder.write(str(a[cont][0])+"\t"+str(a[cont][1])+"\t"+str(a[cont][2])+"\t"+str(a[cont][3])+"\t"+str(a[cont][4])+"\t"+str(a[cont][5])+"\t"+str(a[cont][6])+"\t"+str(a[cont][7])+"\n")
            print("escribi este valor: "+str(cont))
            cont=cont+1
            j=j+1
        elif(p==4):
            if (j==4):
                j=0
            nuevofolder=open(vdf[j],"a")
            nuevofolder.write(str(a[cont][0])+"\t"+str(a[cont][1])+"\t"+str(a[cont][2])+"\t"+str(a[cont][3])+"\t"+str(a[cont][4])+"\t"+str(a[cont][5])+"\t"+str(a[cont][6])+"\t"+str(a[cont][7])+"\n")
            print("escribi este valor: "+str(cont))
            cont=cont+1
            j=j+1
        elif(p==5):
            if (j==5):
                j=0
            nuevofolder=open(vdf[j],"a")
            nuevofolder.write(str(a[cont][0])+"\t"+str(a[cont][1])+"\t"+str(a[cont][2])+"\t"+str(a[cont][3])+"\t"+str(a[cont][4])+"\t"+str(a[cont][5])+"\t"+str(a[cont][6])+"\t"+str(a[cont][7])+"\n")
            print("escribi este valor: "+str(cont))
            cont=cont+1
            j=j+1
        elif(p==6):
            if (j==6):
                j=0
            nuevofolder=open(vdf[j],"a")
            nuevofolder.write(str(a[cont][0])+"\t"+str(a[cont][1])+"\t"+str(a[cont][2])+"\t"+str(a[cont][3])+"\t"+str(a[cont][4])+"\t"+str(a[cont][5])+"\t"+str(a[cont][6])+"\t"+str(a[cont][7])+"\n")
            print("escribi este valor: "+str(cont))
            cont=cont+1
            j=j+1
        elif(p==7):
            if (j==7):
                j=0
            nuevofolder=open(vdf[j],"a")
            nuevofolder.write(str(a[cont][0])+"\t"+str(a[cont][1])+"\t"+str(a[cont][2])+"\t"+str(a[cont][3])+"\t"+str(a[cont][4])+"\t"+str(a[cont][5])+"\t"+str(a[cont][6])+"\t"+str(a[cont][7])+"\n")
            print("escribi este valor: "+str(cont))
            cont=cont+1
            j=j+1
        elif(p==8):
            if (j==8):
                j=0
            nuevofolder=open(vdf[j],"a")
            nuevofolder.write(str(a[cont][0])+"\t"+str(a[cont][1])+"\t"+str(a[cont][2])+"\t"+str(a[cont][3])+"\t"+str(a[cont][4])+"\t"+str(a[cont][5])+"\t"+str(a[cont][6])+"\t"+str(a[cont][7])+"\n")
            print("escribi este valor: "+str(cont))
            cont=cont+1
            j=j+1
        elif(p==9):
            if (j==9):
                j=0
            nuevofolder=open(vdf[j],"a")
            nuevofolder.write(str(a[cont][0])+"\t"+str(a[cont][1])+"\t"+str(a[cont][2])+"\t"+str(a[cont][3])+"\t"+str(a[cont][4])+"\t"+str(a[cont][5])+"\t"+str(a[cont][6])+"\t"+str(a[cont][7])+"\n")
            print("escribi este valor: "+str(cont))
            cont=cont+1
            j=j+1
        elif(p==10):
            if (j==10):
                j=0
            nuevofolder=open(vdf[j],"a")
            nuevofolder.write(str(a[cont][0])+"\t"+str(a[cont][1])+"\t"+str(a[cont][2])+"\t"+str(a[cont][3])+"\t"+str(a[cont][4])+"\t"+str(a[cont][5])+"\t"+str(a[cont][6])+"\t"+str(a[cont][7])+"\n")
            print("escribi este valor: "+str(cont))
            cont=cont+1
            j=j+1

p= int(input("ingrese el numero de pliegues entre 2 y 10: "))
data=open("database.txt","r")
cont=data.read()
rol=cont.splitlines()
vector=[]
a=[]
for i in range (1,len(rol)):
    vector.append(rol[i].split("\t"))
for i in range(len(vector)):
    if(vector[i][-1]=="drugA"):
        a.append(vector[i])
for i in range(len(vector)):
    if(vector[i][-1]=="drugB"):
        a.append(vector[i])
for i in range(len(vector)):
    if(vector[i][-1]=="drugC"):
        a.append(vector[i])
for i in range(len(vector)):
    if(vector[i][-1]=="drugX"):
        a.append(vector[i])
for i in range(len(vector)):
    if(vector[i][-1]=="drugY"):
        a.append(vector[i])

#ORGANIZAMOS LAS CARPETAS DEPENDIENDO DEL NUMERO DE FOLDERS QUE SE HAGAN
if(p==2):
    vdf=["feed1.txt","feed2.txt"]
    sort(p,a,vdf)
elif(p==3):
    vdf=["feed1.txt","feed2.txt","feed3.txt"]
    sort(p,a,vdf)
elif(p==4):
    vdf=["feed1.txt","feed2.txt","feed3.txt","feed4.txt"]
    sort(p,a,vdf)
elif(p==5):
    vdf=["feed1.txt","feed2.txt","feed3.txt","feed4.txt","feed5.txt"]
    sort(p,a,vdf)
elif(p==6):
    vdf=["feed1.txt","feed2.txt","feed3.txt","feed4.txt","feed5.txt","feed6.txt"]
    sort(p,a,vdf)
elif(p==7):
    vdf=["feed1.txt","feed2.txt","feed3.txt","feed4.txt","feed5.txt","feed6.txt","feed7.txt"]
    sort(p,a,vdf)
elif(p==8):
    vdf=["feed1.txt","feed2.txt","feed3.txt","feed4.txt","feed5.txt","feed6.txt","feed7.txt","feed8.txt"]
    sort(p,a,vdf)
elif(p==9):
    vdf=["feed1.txt","feed2.txt","feed3.txt","feed4.txt","feed5.txt","feed6.txt","feed7.txt","feed8.txt","feed9.txt"]
    sort(p,a,vdf)
elif(p==10):
    vdf=["feed1.txt","feed2.txt","feed3.txt","feed4.txt","feed5.txt","feed6.txt","feed7.txt","feed8.txt","feed9.txt","feed10.txt"]
    sort(p,a,vdf)

for i in range(0,len(vdf)):
    modelos(vdf[i],i+1)
    print vdf[i]
    print i
