#!/usr/bin/env python
# coding: utf-8

# In[10]:


##Modelo de ahorro
import random, math
import matplotlib.pyplot as plt
import numpy as np
import PIL
#Función ahorro:
def deuda(mon, x, d1, d, debtmax,N):
    aux1=0.25*int(random.uniform(0,200))
    if(mon[x]-aux1>=debtmax):
        mon[x]=mon[x]-aux1
        mon[d1]=mon[d1]+aux1
    return mon        
#Condiciones iniciales:
GINI=[0 for i in range(81)]
rango=[0 for i in range(81)]
for i in range(81):
    rango[i]+=i*0.25
#Para cada elmento en rango():
for del_mon in rango:
    N=1000
    rep=160
#Cada elemento de rango es una list:
    
    Din=[0 for i in range(rep)]
    for i in range (rep):
        Din[i]=[ 10 for i in range(N)]
        n_trials=10**5
    images=[]   
    debtmax=-del_mon-30
    delx=N/2
    total=np.sum(Din[0])
    f=[0 for i in range(rep)]
    del_x=[0 for i in range(rep)]

    for i in range(n_trials):
        for j in range(rep):
            f[j]=int(random.uniform(0,N))
            del_x[j]=int(random.uniform(0, N))
            deuda(Din[j],f[j],del_x[j],del_mon, debtmax,N) 

# calculo del coeficiente de gini
    listaux1=[0 for i in range(rep)]    
    hist=[0 for i in range(rep)]
    bins1=[0 for i in range (600)]
    for i in range (rep):
        #Ordenar:
        listaux1[i]=np.sort(Din[i])
        #hist[i]=Contiene todos las personas en una barra
        #bins1=División del histograma
        hist[i], bins1=np.histogram(Din[i], bins =[debtmax+i*0.25 for i in range(601)])
        sum=0
        for aja in hist[i]:
          sum+=aja
        hist[i]=hist[i]/(sum*0.25)
    listaux=[0 for i in range(N)]
    histaux=[0 for i in range(601)]
    for i in range(N):
        for j in range(rep):
            listaux[i]+=listaux1[j][i]
        
        listaux[i]/=rep
    
    for i in range(600):
        for j in range(rep):
            histaux[i]+=hist[j][i]
        histaux[i]/=rep
    result=[0 for i in range(N)]
    bins=[(i+1)/10 for i in range(N)]
    for i in range(N):
        for j in range (i+1):
            result[i]+=listaux[j]/total*100
    pe_area = 0
    lorenz_area = 0
    a=np.sort(result)
    Copia=[a[i] for i in range(len(result))]
    for i in range(N):
        lorenz_area+=abs(result[i]-bins[i])/10
        pe_area+=bins[i]/10
    pe_area-=Copia[0]*100
    #pe_area=pe_area+(N-1)*100**2*(-debtmax)/(10*N)-100**2/(2*N)
    gini_val = (lorenz_area)/pe_area
    GINI[int((del_mon)*4)]=gini_val
    print("Area máxima=",pe_area,"Area lorenz=",lorenz_area)
    #print(bins1)
    #print(histaux)
    EFE=[Copia[0] for i in range(1000)]
    EFE[0]=0
    EFE[999]=100
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(bins, result, color="darkblue",label="Curva de Lorenz")
    plt.plot(bins, bins, color="k", label="Igualdad perfecta")
    plt.plot(bins,EFE, color="r", label="Curva mínima riqueza")
    plt.xlabel("Porcentaje de la poblacion")
    plt.ylabel("Porcentaje de riqueza")
    plt.legend()    
    plt.title("GINI: %.4f" %(gini_val))
    plt.subplot(2, 1, 2)
    plt.plot(bins1, histaux, color="r", label="distribucion de la riqueza")
    a=1/(10-debtmax)*np.exp(-(bins1-debtmax)/(10-debtmax))
    plt.plot(bins1,a, color='b',label="Distribución exacta P(x)=(1/"+str(10-debtmax)+")exp(-(x+"+str(-debtmax)+")/"+str(10-debtmax)+")") 
    plt.xlabel("Dinero")
    plt.ylabel("Probabilidad")
    plt.legend()
    plt.tight_layout()
    filename='distr_final2_Ahorro%.2f.png' %(del_mon)
    plt.savefig(filename)
    images.append(filename)
    filename='GINI%DEUDAS.png'
    plt.savefig(filename)
    plt.show()
print(GINI)
Base_monetaria_eje=[0.25*i for i in range(81)]
plt.plot(Base_monetaria_eje,GINI, label="Coeficiente Gini")
plt.xlabel("Base monetaria")
plt.ylabel("Coeficiente Gini")
plt.show()


# In[ ]:





# In[ ]:




